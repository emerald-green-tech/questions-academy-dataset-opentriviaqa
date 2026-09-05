from pathlib import Path


def test_consecutive_whitespace() -> None:
    questions_dir = Path().parent / "questions_academy_dataset_opentriviaqa/data/flat"
    assert questions_dir.is_dir(), f"Could not find questions directory {questions_dir.absolute()}"

    for category in questions_dir.glob("**/*"):
        for line_index, line in enumerate(category.read_bytes().splitlines()):
            assert not b"  " in line, (
            "\n"
            "https://github.com/emerald-green-tech/questions-academy-dataset-opentriviaqa/blob/main/"
            f"{category}#L{line_index+1}"
        )
