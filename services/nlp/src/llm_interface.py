from dataclasses import dataclass
from typing import Any


@dataclass
class LLMResponse:
    content: dict[str, Any]
    model: str


class LLMExtractor:
    """Abstraction around high-reasoning LLM calls."""

    def __init__(self, model_name: str = "gpt-placeholder") -> None:
        self.model_name = model_name

    def extract_structured_event(self, prompt: str, schema: dict[str, Any]) -> LLMResponse:
        # TODO: integrate real LLM provider with JSON-schema constrained output.
        return LLMResponse(
            model=self.model_name,
            content={
                "title": "Placeholder event",
                "summary": "LLM-refined summary placeholder.",
                "countries": ["United States", "China"],
                "goods": ["electronics"],
                "tariff_rate": 15,
                "event_date": "2026-04-14",
                "severity_score": 0.72,
                "sectors": ["Industrials", "Information Technology"],
                "event_category": "tariff_increase",
            },
        )

