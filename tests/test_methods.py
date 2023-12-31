"""Test functions from the source code."""
from __future__ import annotations
from foilreader import FoilReader, Foil
import io
import pytest

sd2083_9pct = """SD2083 (9.0%)
  1.000000  0.000000
  0.996690  0.000350
  0.986860  0.001520
  0.970890  0.003740
  0.949290  0.007160
  0.922650  0.011760
  0.891580  0.017410
  0.856660  0.023840
  0.818460  0.030780
  0.777450  0.037910
  0.734120  0.044890
  0.688860  0.051460
  0.642080  0.057370
  0.594150  0.062430
  0.545460  0.066550
  0.496450  0.069640
  0.447550  0.071620
  0.399130  0.072510
  0.351680  0.072360
  0.305680  0.071210
  0.261600  0.069080
  0.219900  0.066010
  0.181010  0.062030
  0.145320  0.057180
  0.113130  0.051430
  0.084640  0.044890
  0.060040  0.037720
  0.039520  0.030100
  0.023190  0.022240
  0.011130  0.014400
  0.003380  0.006980
  0.000030  0.000600
  0.002200 -0.004370
  0.010320 -0.008530
  0.023690 -0.012130
  0.042340 -0.014910
  0.066240 -0.016960
  0.095150 -0.018440
  0.128680 -0.019370
  0.166490 -0.019770
  0.208180 -0.019700
  0.253310 -0.019210
  0.301370 -0.018370
  0.351820 -0.017250
  0.404060 -0.015920
  0.457500 -0.014390
  0.511570 -0.012740
  0.565630 -0.011050
  0.619050 -0.009390
  0.671170 -0.007820
  0.721360 -0.006370
  0.769010 -0.005090
  0.813500 -0.003970
  0.854280 -0.003040
  0.890840 -0.002260
  0.922700 -0.001570
  0.949550 -0.000940
  0.971080 -0.000440
  0.986930 -0.000150
  0.996700 -0.000040
  1.000010  0.000000
"""


def test_parser_None():
    r = FoilReader()
    assert r is not None
    with pytest.raises(ValueError):
        x = r.text
        assert x is None  # not reached
    # no .get, no initialization
    assert r.as_seligdatfile() is None
    assert r.as_uiucedu_txt() is None
    assert r.best(None, None, None, None) is None


def test_parser_sd2083():
    r = FoilReader()
    f = r.get(io.StringIO(sd2083_9pct))
    assert f is not None
    assert f.name == "SD2083 (9.0%)"
    assert len(f.coordinates) == 61


def test_parser_selig_bad():
    r = FoilReader()
    f = None

    # no name on first line
    r.text = """
 1.0000 0.0000
 0.999  0.999
"""
    f = r.as_seligdatfile()
    assert f is None

    r.text = """ Bad desc starts with space but shouldn't.
 1.0000 0.0000
 0.999  0.999
"""
    f = r.as_seligdatfile()
    assert f is None

    r.text = """Selig data file with non-numeric coords
  x1.000000  y0.000000
  0.996690  0.000350
"""
    f = r.as_seligdatfile()
    assert f is None


def test_Foil_no_name():
    f = Foil()
    assert f is not None
    with pytest.raises(ValueError):
        x = f.name
        assert x is None  # not reached
