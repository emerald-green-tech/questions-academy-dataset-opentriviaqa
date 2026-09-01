from pathlib import Path


def test_consecutive_whitespace() -> None:
    questions_dir = Path().parent / "questions"
    for category in questions_dir.glob("**/*"):
        for line_index, line in enumerate(category.read_bytes().splitlines()):
            assert not b"  " in line, (
            "\n"
            "https://github.com/emerald-green-tech/questions-academy-dataset-opentriviaqa/blob/main/"
            f"{category}#L{line_index+1}"
        )