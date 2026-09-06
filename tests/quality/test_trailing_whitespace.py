from pathlib import Path

import pytest

@pytest.mark.quality
def test_trailing_whitespace() -> None:
    questions_dir = Path().parent / "questions_academy_dataset_opentriviaqa/data/flat"
    assert questions_dir.is_dir(), f"Could not find questions directory {questions_dir.absolute()}"

    for category in questions_dir.glob("**/*"):
        for line_index, line in enumerate(category.read_bytes().splitlines()):
            assert not line.endswith(b" "), (
            "\n"
            f"Found trailing whitespace in {category} line {line_index+1}\n"
            "VS Code shortcut:\n"
            f'code --goto "{category}:{line_index+1}"\n'
        )
