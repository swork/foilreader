from __future__ import annotations
from typing import IO
from traceback import print_exception
import re

__version__ = "0.0.1"


class Foil:
    def __init__(self) -> None:
        self._name: str | None = None
        self._coordinates: list[tuple[float, float]] = []

    def __str__(self) -> str:
        return f"Foil<{self._name}, coords:{len(self._coordinates)}>"

    @property
    def coordinates(self) -> list[tuple[float, float]]:
        return self._coordinates

    def append_coordinate(self, x, y) -> None:
        self._coordinates.append((x, y))

    @property
    def name(self) -> str:
        if self._name is None:
            raise ValueError("Foil has no .name")
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name


class FoilReader:
    def __init__(self) -> None:
        self._text: str | None = None

    @property
    def text(self) -> str:
        if self._text is None:
            raise ValueError("FoilReader has no text. (.get()?)")
        return self._text

    @text.setter
    def text(self, text) -> None:
        self._text = text

    def get(self, filelike: IO[str]) -> Foil | None:
        self.text = filelike.read()
        return self.best(
            self.as_seligdatfile(),
            self.as_uiucedu_txt(),
        )

    def best(self, *args: Foil | None) -> Foil | None:
        best: Foil | None = None
        for result in args:
            if result is None:
                continue
            if best:
                if len(result.coordinates) > len(best.coordinates):
                    best = result
            else:
                best = result
        return best

    def as_seligdatfile(self) -> Foil | None:
        """Try to accept ._text as a Selig dat file.
        Guessing the format of the file: one line starting with
        a non-whitespace char giving the foil name,
        followed by lines of 2 float coordinates each starting with
        a whitespace char.
        """
        if self._text is None:
            return None

        r_desc = re.compile(r"(\S.*)\s*")
        r_coords = re.compile(r"\s+([\d.-]+)\s+([\d.-]+)\s*")
        r_empty = re.compile(r"^\s*$")
        lines = self.text.split("\n")
        mo = r_desc.match(lines[0])
        if not mo:
            try:
                raise ValueError(f'First line is not a description: "{lines[0]}')
            except Exception as e:
                print_exception(e, limit=3)
            return None

        f = Foil()
        f.name = mo.group(1)
        try:
            for line in lines[1:]:
                mo = r_coords.match(line)
                if not mo:
                    if r_empty.match(line):
                        continue
                    raise ValueError(f'not Selig coords: "{line}"')
                f.append_coordinate(float(mo.group(1)), float(mo.group(2)))
        except Exception as e:
            print_exception(e, limit=3)
            return None
        return f

    def as_uiucedu_txt(self) -> Foil | None:
        return None
