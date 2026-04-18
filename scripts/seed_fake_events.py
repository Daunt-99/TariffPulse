import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "mock"


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    summary = {
        "events": json.loads((DATA_DIR / "events.json").read_text(encoding="utf-8")),
        "reactions": json.loads((DATA_DIR / "reactions.json").read_text(encoding="utf-8")),
        "predictions": json.loads((DATA_DIR / "predictions.json").read_text(encoding="utf-8")),
    }
    output_path = ROOT / "data" / "generated" / "seed_snapshot.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Wrote sample seed snapshot to {output_path}")


if __name__ == "__main__":
    main()

