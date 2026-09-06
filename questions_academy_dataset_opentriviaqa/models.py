from dataclasses import dataclass, field
from typing import List


@dataclass
class Answer:
    """
    Represents one of the multiple choice answers for a question. In the flat files, these are the lines that start with
    capital letters, e.g. A, B, C, D. Here's an example of a question from the flat files:

    > #Q How does this proverb continue: The squeaking wheel gets ...
    > ^ The grease
    > A The rust
    > B Removed
    > C The broken
    > D The grease

    In this example, each of the choices "The rust", "Removed", "The broken", and "The grease" are answers. The value of
    `correct` depends on whether the answer text matches the line that starts with "^ ", which demarks the correct
    answer.
    """
    text: str
    correct: bool


@dataclass
class Question:
    """
    Represents a question. The question text may be in more than one lines.
    """
    id: str
    text: str
    answers: List[Answer] = field(default_factory=list)


@dataclass
class Category:
    """
    Represents a question category. The name of the category is taken from the name of the file that contains the
    questions.
    """
    name: str
    questions: List[Question] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name

@dataclass
class Dataset:
    """
    Represents the entire OpenTriviaQA dataset. The hierarchy is:

    Dataset
    └── Category
        └── Question
            └── Answer

    For example, this snippet from the flat files:

    > #Q How does this proverb continue: The squeaking wheel gets ...
    > ^ The grease
    > A The rust
    > B Removed
    > C The broken
    > D The grease

    ...is parsed into this hierarchy:
    
    Dataset
    └── Category: brain-teasers
        └── Question: How does this proverb continue: The squeaking wheel gets ...
            ├── Answer: The rust (correct: False)
            ├── Answer: Removed (correct: False)
            ├── Answer: The broker (correct: False)
            └── Answer: The grease (correct: True)
    """
    categories: List[Category] = field(default_factory=list)
