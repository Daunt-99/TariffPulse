from lag_classifier import classify_lag


def test_classify_lagged() -> None:
    assert classify_lag(0.1, 0.2, 1.1) == "lagged"
