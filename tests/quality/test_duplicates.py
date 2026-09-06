from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import pytest


@dataclass
class Question:
    stem: bytes
    category: Path
    line_index: int


@pytest.mark.quality
def test_duplicate_questions() -> None:
    questions_dir = Path().parent / "questions_academy_dataset_opentriviaqa/data/flat"
    assert questions_dir.is_dir(), f"Could not find questions directory {questions_dir.absolute()}"

    questions: Dict[bytes, List[Question]] = defaultdict(list)

    for category in questions_dir.glob("**/*"):
        for line_index, line in enumerate(category.read_bytes().splitlines()):
            if line.startswith(b"#Q "):
                questions[line].append(
                    Question(
                        stem=line,
                        category=category,
                        line_index=line_index,
                    )
                )

    total_duplicates = len([question for question in questions if len(questions[question]) > 1])

    for question in questions:
        assert len(questions[question]) < 2, (
            "\n"
            "Found duplicate questions:\n"
            f"{questions[question][0].category} line {questions[question][0].line_index+1}\n"
            f"{questions[question][1].category} line {questions[question][1].line_index+1}\n"
            f"(out of {total_duplicates} duplicates)\n"
        )
