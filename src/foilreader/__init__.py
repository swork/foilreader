from __future__ import annotations

__version__ = "0.0.1"


class Foil:
    def __init__(self):
        self.coordinates: list[tuple[float, float]] = []

    def coordinates(self) -> list[tuple[float, float]]:
        return self.coordinates


class FoilReader:
    def __init__(self):
        self.text = None

    def get(self, filelike) -> Foil | None:
        self.text = filelike.read()
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
                if len(result.coordinates) > len(best.coordinates):
                    best = result
            else:
                best = result
        return best

    def as_airfoiltoolscom_csv(self) -> Foil | None:
        return None

    def as_uiucedu_txt(self) -> Foil | None:
        return None
