from pathlib import Path


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
                    "https://github.com/emerald-green-tech/questions-academy-dataset-opentriviaqa/blob/main/"
                    f"{category}#L{line_index+1}"
                )
