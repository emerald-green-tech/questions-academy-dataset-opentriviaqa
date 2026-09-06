# Questions Academy Dataset: OpenTriviaQA #

This package contains a dataset of multiple choice questions and answers, originally forked from
[OpenTriviaQA], and updated and adapted for use in the [Questions Academy]. It also contains Python utilities to help
with using the dataset.

## Usage ##

Get the entire dataset:

```python
from questions_academy_dataset_opentriviaqa.parser import parse_dataset

dataset = parse_dataset()

for category in dataset.categories:
    print(f"Category: {category} - Number of Questions: {len(category.questions)}")
```

Each Category in the dataset has an attribute called `category.questions` that contains a list of Questions. Each
Question has an attribute called `question.answers` that contains a list of Answers. Each Answer has an attribute called
`answer.correct` that tells you if that answer is correct for that question.

## Contributions ##

If you want to add a question, the best way is to contribute it to the upstream [OpenTriviaQA] repository, and we will
port it here.

## Testing ##

To run the unit tests included with this package, simply run `pytest`. Note that there are data quality tests which
are not very robust; they often fail with false positive findings. These quality tests are excluded by default when you
run `pytest`. To run the quality tests, run `pytest -m quality`.

## License

This work is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License][CC-BY-SA-4.0].

<!-- Links -->
[OpenTriviaQA]: https://github.com/uberspot/OpenTriviaQA
[Questions Academy]: https://questions.academy/
[CC-BY-SA-4.0]: https://creativecommons.org/licenses/by-sa/4.0/
