import json
import unittest
from pathlib import Path

from jsonschema import ValidationError, validate


class TestBaseClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(
            Path("src/schemas/v1/quizlit.json").read_text()
        )


class TestV1HappyPath(TestBaseClass):
    @staticmethod
    def get_test_cases():
        return [
            (
                "name of test -- example 1",
                {
                    "name": "testing",
                    "questions": [
                        {
                            "question": "true or false questions",
                            "answers": {
                                "correct": {"answer": "Yessir"},
                                "incorrect": {
                                    "answer": "WRONG",
                                    "explanation": "Because I said so",
                                },
                            },
                        },
                        {
                            "question": "selection question",
                            "answers": {
                                "correct": [
                                    {"answer": "1"},
                                    {"answer": "2"},
                                    {"answer": "3"},
                                ],
                                "incorrect": [
                                    {
                                        "answer": "nope",
                                        "explanation": "Not a number",
                                    },
                                ],
                            },
                        },
                        {
                            "question": "order question",
                            "answers": {
                                "correct": [
                                    {"answer": "1"},
                                    {"answer": "2"},
                                    {"answer": "3"},
                                ],
                            },
                        },
                    ],
                },
            ),
            (
                "True and False question",
                {
                    "name": "True and False questions",
                    "questions": [
                        {
                            "question": "true or false questions",
                            "answers": {
                                "correct": {"answer": "Yessir"},
                                "incorrect": {
                                    "answer": "WRONG",
                                    "explanation": "Because I said so",
                                },
                            },
                        },
                    ],
                },
            ),
            (
                "selection questions",
                {
                    "name": "Selection questions",
                    "questions": [
                        {
                            "question": "true or false questions",
                            "answers": {
                                "correct": [{"answer": "Yessir"}],
                                "incorrect": [
                                    {
                                        "answer": "WRONG",
                                        "explanation": "Because I said so",
                                    }
                                ],
                            },
                        },
                    ],
                },
            ),
            (
                "order questions",
                {
                    "name": "Order questions",
                    "questions": [
                        {
                            "question": "true or false questions",
                            "answers": {
                                "correct": [{"answer": "1"}, {"answer": "2"}],
                            },
                        },
                    ],
                },
            ),
        ]

    def test_v1(self):
        for name, data in self.get_test_cases():
            with self.subTest(msg=name):
                validate(instance=data, schema=self.schema)


class TestV1Errors(TestBaseClass):
    @staticmethod
    def get_test_cases():
        return [
            (
                "Empty dict",
                {},
            ),
            (
                "wrong shcema",
                {"productId": 1, "productName": "name_1", "price": 0},
            ),
            (
                "question but no answers",
                {
                    "name": "Question by no answers",
                    "questions": [
                        {"question": "question"},
                    ],
                },
            ),
            (
                "Question with no correct answer -- True or false",
                {
                    "name": "question with no correct answer",
                    "questions": [
                        {
                            "question": "question",
                            "answers": {
                                "incorrect": {"answer": "answer"},
                            },
                        }
                    ],
                },
            ),
            (
                "Question with no correct answer",
                {
                    "name": "Question with no correct answer",
                    "questions": [
                        {
                            "question": "question",
                            "answer": {
                                "incorrect": [
                                    {"answer": "answer_2"},
                                    {"answer": "answer_2"},
                                ],
                            },
                        },
                    ],
                },
            ),
            (
                "Empty question",
                {
                    "name": "Empty question",
                    "questions": [
                        {
                            "question": "",
                            "answers": {
                                "correct": {"answer": "answer"},
                                "incorrect": {"answer", "answer"},
                            },
                        },
                    ],
                },
            ),
            (
                "Empty answer",
                {
                    "name": "Exmpty_answer",
                    "questions": [
                        {
                            "question": "question",
                            "answers": {
                                "correct": {"answer": ""},
                                "incorrect": {"answer": "answer"},
                            },
                        },
                    ],
                },
            ),
            (
                "Empty correct answer object",
                {
                    "name": "Emptpy correct answer object",
                    "questions": [
                        {
                            "question": "question",
                            "answers": {
                                "correct": {},
                                "incorrect": {"answer", "answer"},
                            },
                        },
                    ],
                },
            ),
        ]

    def test_v1(self):
        for name, data in self.get_test_cases():
            with self.subTest(msg=name):
                with self.assertRaises(ValidationError):
                    validate(instance=data, schema=self.schema)


if __name__ == "__main__":
    unittest.main()
