from __future__ import annotations

class Foil:
    def __init__(self):
        self.coordinates: list[tuple[float, float]] = []

    def coordinates(self) -> list[tuple[float, float]]:
        return self.coordinates


class FoilReader:
    def __init__(self):
        self.text = None

    def get(self, filelike) -> Union[Foil | None]:
        self.text = filelike.read()
        return self.best(
            self.as_airfoiltoolscom_csv(),
            self.as_uiucedu_txt(),
        )

    def as_airfoiltoolscom_csv(self) -> Union[Foil | None]:
        return None

    def as_uiucedu_txt(self) -> Union[Foil | None]:
        return None
