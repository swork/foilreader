"""Test functions from the source code."""
from __future__ import annotations
from foilreader import FoilReader


def test_parser_None():
    r = FoilReader()
    assert r is not None
    # no .get, no initialization
    assert r.as_airfoiltoolscom_csv() is None
    assert r.as_uiucedu_txt() is None
    assert r.best(None, None, None, None) is None
