import pytest

from app import calculate_average, classify_score


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20


def test_classify_score():
    assert classify_score(75) == "hyväksytty"


def test_classify_score_boundary():
    assert classify_score(50) == "hyväksytty"
    assert classify_score(80) == "erinomainen"


def test_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])
