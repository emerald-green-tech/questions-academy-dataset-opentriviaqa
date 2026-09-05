from pathlib import Path

COMMON_SPELLING_MISTAKES = [
    "arent",  # aren't
    "cant",  # can't
    "couldnt",
    "didnt",
    "doesnt",
    "dont",  # don't
    "hes",  # he's
    "hadnt",
    "havent",
    "hasnt",
    # "im",  # I'm -- Comment in to check if needed, but there are false positives.
    # "id",  # I'd -- Comment in to check if needed, but there are false positives.
    # "ill",  # I'll -- Comment in to check if needed, but there are false positives.
    "isnt",  # isn't
    # "ive",  # I've -- False positive with designer Jonathan Ive
    "oclock",
    "shes",  # she's
    "shouldnt",  # shouldn't
    "thats",
    "theres",  # there's
    "thered",
    "theyre",
    "theyll",
    "werent",  # weren't
    "whats",
    "wheres",  # where's
    "whos",  # who's"
    "wouldve",  # would've
    "wont",
    "youll",  # you'll
    "youve",  # you've
    "youre",
    "youd",  # you'd
]


def test_common_spelling_mistakes() -> None:
    questions_dir = Path().parent / "questions_academy_dataset_opentriviaqa/data/flat"
    assert questions_dir.is_dir(), f"Could not find questions directory {questions_dir.absolute()}"

    for category in questions_dir.glob("**/*"):
        for line_index, line in enumerate(category.read_text().splitlines()):
            for word in line.split():
                assert word.lower() not in COMMON_SPELLING_MISTAKES, (
                    "\n"
                    "https://github.com/emerald-green-tech/questions-academy-dataset-opentriviaqa/blob/main/"
                    f"{category}#L{line_index+1} contains misspelled word {word}"
                )