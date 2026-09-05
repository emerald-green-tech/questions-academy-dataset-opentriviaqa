from pathlib import Path


def test_missing_empty_lines() -> None:
    questions_dir = Path().parent / "questions_academy_dataset_opentriviaqa/data/flat"
    assert questions_dir.is_dir(), f"Could not find questions directory {questions_dir.absolute()}"

    for category in questions_dir.glob("**/*"):
        lines = category.read_text().splitlines()
        for line_index, line in enumerate(lines):
            if line_index == 0:
                continue

            previous_line = lines[line_index-1]

            if line.startswith("#Q "):
                assert len(previous_line) == 0, (
                    "\n"
                    "https://github.com/emerald-green-tech/questions-academy-dataset-opentriviaqa/blob/main/"
                    f"{category}#L{line_index+1}"
                )
