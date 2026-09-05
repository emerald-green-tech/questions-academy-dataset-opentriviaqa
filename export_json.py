import json
from dataclasses import asdict
from pathlib import Path

from questions_academy_dataset_opentriviaqa.parser import parse_dataset


def export_json() -> Path:
    export_path = Path(__file__).resolve().parent / "questions_academy_dataset_opentriviaqa/data/json/dataset.json"
    dataset = parse_dataset()
    export_path.write_text(json.dumps(asdict(dataset), indent=2))
    return export_path


if __name__ == "__main__":
    export_path = export_json()
    print(f"Exported JSON at: {export_path.absolute()}")
