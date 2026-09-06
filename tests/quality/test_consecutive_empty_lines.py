from pathlib import Path

import pytest


@pytest.mark.quality
def test_consecutive_empty_lines() -> None:
    questions_dir = Path().parent / "questions_academy_dataset_opentriviaqa/data/flat"
    assert questions_dir.is_dir(), f"Could not find questions directory {questions_dir.absolute()}"

    for category in questions_dir.glob("**/*"):
        lines = category.read_text().splitlines()
        for line_index, line in enumerate(lines):
            try:
                next_line = lines[line_index+1]
            except IndexError:
                continue

            if len(line) == 0 or line.isspace():
                assert not (len(next_line) == 0 or next_line.isspace()), (
                    "\n"
                    f"{category} contains consecutive empty lines at line {line_index+1}\n"
                    "VS Code shortcut:\n"
                    f'code --goto "{category}:{line_index+1}"\n'
                )
