from __future__ import annotations

class Foil:
    def __init__(self):
        self.coordinates = []

    def coordinates(self):
        return self.coordinates


class FoilReader:
    def __init__(self):
        self.text = None

    def get(self, filelike):
        self.text = filelike.read()
        return self.best(
            self.as_airfoiltoolscom_csv(),
            self.as_uiucedu_txt(),
        )

    def as_airfoiltoolscom_csv(self):
        pass

    def as_uiucedu_txt(self):
        pass
