from pathlib import Path

COMMON_SPELLING_MISTAKES = [
    "arent",  # aren't
    "cant",  # can't
    "couldnt",
    "dont",  # don't
    "hes",  # he's
    "hadnt",
    # "im",  # I'm -- Comment in to check if needed, but there are false positives.
    # "id",  # I'd -- Comment in to check if needed, but there are false positives.
    "isnt",  # isn't
    "shes",  # she's
    "shouldnt",  # shouldn't
    "theres",  # there's
    "werent",  # weren't
    "wheres",  # where's
    "whos",  # who's"
    "wouldve",  # would've
    "youll",  # you'll
    "youve",  # you've
]


def test_common_spelling_mistakes() -> None:
    questions_dir = Path().parent / "questions"
    for category in questions_dir.glob("**/*"):
        for line_index, line in enumerate(category.read_text().splitlines()):
            for word in line.split():
                assert word.lower() not in COMMON_SPELLING_MISTAKES, (
                    "\n"
                    "https://github.com/emerald-green-tech/questions-academy-dataset-opentriviaqa/blob/main/"
                    f"{category}#L{line_index+1} contains misspelled word {word}"
                )