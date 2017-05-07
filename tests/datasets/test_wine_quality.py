import pytest

import reprod as rr
from reprod.datasets import WineQuality

@pytest.mark.skipif(rr.internet.is_off(), reason='no internet')
def test_download():
    expected_csv_head = [
        '"fixed acidity";"volatile acidity";"citric acid";"residual sugar";"chlorides";'
        '"free sulfur dioxide";"total sulfur dioxide";"density";"pH";"sulphates";'
        '"alcohol";"quality"',
        '7.4;0.7;0;1.9;0.076;11;34;0.9978;3.51;0.56;9.4;5',
        '7.8;0.88;0;2.6;0.098;25;67;0.9968;3.2;0.68;9.8;5',
        '7.8;0.76;0.04;2.3;0.092;15;54;0.997;3.26;0.65;9.8;5',
        '11.2;0.28;0.56;1.9;0.075;17;60;0.998;3.16;0.58;9.8;6',
        '7.4;0.7;0;1.9;0.076;11;34;0.9978;3.51;0.56;9.4;5'
        ]

    wine = WineQuality()
    csv = wine.download()
    csv_head = csv.split('\n')[:6]
    assert expected_csv_head == csv_head, 'Downloaded data not as expected.'