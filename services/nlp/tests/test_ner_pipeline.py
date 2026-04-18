from ner_pipeline import extract_entities


def test_extract_entities() -> None:
    result = extract_entities("The United States may levy 15% tariffs on steel imports from China.")
    assert "United States" in result["countries"]
    assert result["tariff_rate"] == 15.0
