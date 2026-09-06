from pathlib import Path

import pytest


@pytest.mark.quality
def test_missing_empty_lines() -> None:
    questions_dir = Path().parent / "questions_academy_dataset_opentriviaqa/data/flat"
    assert questions_dir.is_dir(), f"Could not find questions directory {questions_dir.absolute()}"

    for category in questions_dir.glob("**/*"):
        lines = category.read_text().splitlines()
        for line_index, line in enumerate(lines):
            if line_index == 0:
                continue

            previous_line = lines[line_index-1]

            if line.startswith("* ID: "):
                assert len(previous_line) == 0, (
                    "\n"
                    f"Missing an empty line before a new question in {category} line {line_index+1}\n"
                    "VS Code shortcut:\n"
                    f'code --goto "{category}:{line_index+1}"\n'
                )
