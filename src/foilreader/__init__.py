from __future__ import annotations
from typing import IO

__version__ = "0.0.1"


class Foil:
    def __init__(self) -> None:
        self._coordinates: list[tuple[float, float]] = []

    def coordinates(self) -> list[tuple[float, float]]:
        return self._coordinates


class FoilReader:
    def __init__(self) -> None:
        self._text: str | None = None

    def get(self, filelike: IO[str]) -> Foil | None:
        self._text = filelike.read()
        return self.best(
            self.as_airfoiltoolscom_csv(),
            self.as_uiucedu_txt(),
        )

    def best(self, *args: Foil | None) -> Foil | None:
        best: Foil | None = None
        for result in args:
            if result is None:
                continue
            if best:
                if len(result.coordinates()) > len(best.coordinates()):
                    best = result
            else:
                best = result
        return best

    def as_airfoiltoolscom_csv(self) -> Foil | None:
        return None

    def as_uiucedu_txt(self) -> Foil | None:
        return None
