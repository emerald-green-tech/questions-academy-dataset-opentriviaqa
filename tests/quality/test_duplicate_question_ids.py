from pathlib import Path

import pytest


@pytest.mark.quality
def test_duplicate_question_ids() -> None:
    questions_dir = Path().parent / "questions_academy_dataset_opentriviaqa/data/flat"
    assert questions_dir.is_dir(), f"Could not find questions directory {questions_dir.absolute()}"

    question_ids = []
    for category in questions_dir.glob("**/*"):
        lines = category.read_text().splitlines()
        for line in lines:
            if line.startswith("* ID: "):
                question_ids.append(line)

    # Very very slow:
    # for question_id in question_ids:
    #     assert question_ids.count(question_id) == 1, f"Found duplicate question ID {question_id}"

    # Very slow:
    # for question_id_index, question_id in enumerate(question_ids):
    #     first_index = question_ids.index(question_id)  # find the first time that this question_id appears
    #     assert first_index == question_id_index, f"Found duplicate question ID {question_id}"

    # Fast:
    seen_question_ids = set()
    for question_id in question_ids:
        try:
            assert question_id not in seen_question_ids, f"Found duplicate question ID {question_id}"
        except AssertionError:
            # Catch and re-raise to clean up the CLI output, otherwise it's unreadable:
            raise AssertionError(f"Found duplicate question ID {question_id}")
        else:
            seen_question_ids.add(question_id)
