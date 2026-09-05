from pathlib import Path
from typing import List

from questions_academy_dataset_opentriviaqa.models import Answer, Category, Dataset, Question


def parse_dataset() -> Dataset:
    dataset = Dataset()
    questions_path = Path(__file__).resolve().parent / "data/flat"

    assert questions_path.is_dir(), f"Questions Path not found: {questions_path.absolute()}"

    for category_path in questions_path.glob("**/*"):
        category = parse_category(category_path)
        dataset.categories.append(category)

    return dataset


def parse_category(category_path: Path) -> Category:
    category = Category(name=category_path.stem)

    question_lines: List[str] = []
    for line in category_path.read_text().splitlines():
        if len(line) == 0 or line.isspace():
            continue  # skip empty lines
        if line.startswith("#Q ") and len(question_lines) != 0:
            question = parse_question(question_lines)
            category.questions.append(question)
            question_lines = []
        question_lines.append(line)

    return category



def parse_question(question_lines: List[str]) -> Question:
    in_question_text: bool = False

    question_text: List[str] = []
    correct_answer_choice: str
    answer_choices: List[str] = []

    for line in question_lines:
        if line.startswith("#Q "):
            in_question_text = True  # the question text starts here
        elif line.startswith("^ "):
            in_question_text = False  # the question text ends here

        if in_question_text:
            question_text.append(line[3:] if line.startswith("#Q ") else line)
            continue

        if line.startswith("^ "):
            correct_answer_choice = line[2:]
        else:
            answer_choices.append(line[2:])

    question = Question(text = "\n".join(question_text))
    for answer_choice in answer_choices:
        answer = Answer(text=answer_choice, correct=answer_choice==correct_answer_choice)
        question.answers.append(answer)

    # Verify that there is 1 correct answer:
    assert len([answer for answer in question.answers if answer.correct]) == 1, (
        f"Found multiple correct answers for this question: {question}"
    )

    return question


if __name__ == "__main__":
    parse_dataset()
