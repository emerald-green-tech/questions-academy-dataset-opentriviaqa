from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


@dataclass
class Question:
    stem: bytes
    category: Path
    line_index: int


def test_duplicate_questions() -> None:
    questions_dir = Path().parent / "questions"
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

    for question in questions:
        assert len(questions[question]) < 2, (
            "\n"
            "https://github.com/emerald-green-tech/questions-academy-dataset-opentriviaqa/blob/main/"
            f"{questions[question][0].category}#L{questions[question][0].line_index+1} /n"
            "https://github.com/emerald-green-tech/questions-academy-dataset-opentriviaqa/blob/main/"
            f"{questions[question][1].category}#L{questions[question][1].line_index+1} /n"
        )
