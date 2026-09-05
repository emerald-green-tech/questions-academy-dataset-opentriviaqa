import csv
from pathlib import Path

from questions_academy_dataset_opentriviaqa.parser import parse_dataset


def export_csv() -> Path:
    export_path = Path(__file__).resolve().parent / "questions_academy_dataset_opentriviaqa/data/csv/dataset.csv"
    field_names = ["Number", "Category", "Question", "Correct", "Answer A", "Answer B", "Answer C", "Answer D"]
    number = 1
    dataset = parse_dataset()

    with open(export_path, "w") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        csv_writer.writeheader()

        for category in dataset.categories:
            for question in category.questions:
                answers = ["", "", "", ""]
                for answer_index, answer in enumerate(question.answers):
                    answers[answer_index] = answer.text

                csv_writer.writerow(
                    {
                        "Number": number,
                        "Category": category.name,
                        "Question": question.text,
                        "Correct": [answer.text for answer in question.answers if answer.correct][0],
                        "Answer A": answers[0],
                        "Answer B": answers[1],
                        "Answer C": answers[2],
                        "Answer D": answers[3],
                    }
                )

    return export_path


if __name__ == "__main__":
    export_path = export_csv()
    print(f"Exported CSV at: {export_path.absolute()}")
