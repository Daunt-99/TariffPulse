import json
from pathlib import Path

from event_normalizer import normalize_event
from llm_interface import LLMExtractor
from ner_pipeline import extract_entities
from sector_mapper import map_sectors
from severity_scoring import score_severity


def build_prompt(document_text: str, ner_result: dict) -> str:
    template_path = Path(__file__).resolve().parent / "prompts" / "event_extraction_prompt.txt"
    template = template_path.read_text(encoding="utf-8")
    return template.format(document_text=document_text, ner_result=json.dumps(ner_result, indent=2))


def extract_event(document_text: str, source: str = "news") -> dict:
    ner_result = extract_entities(document_text)
    prompt = build_prompt(document_text, ner_result)
    schema_path = Path(__file__).resolve().parent / "schemas" / "event_schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    llm = LLMExtractor()
    response = llm.extract_structured_event(prompt, schema)
    enriched = response.content | {
        "sectors": map_sectors(ner_result["goods"], document_text),
        "severity_score": score_severity(
            ner_result["tariff_rate"], official_source=source in {"ustr", "wto"}, sectors=response.content["sectors"]
        ),
    }
    return normalize_event(enriched).model_dump()

