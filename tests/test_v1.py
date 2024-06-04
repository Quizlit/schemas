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
                {"productId": 1, "productName": "name_1", "price": 0.01},
            ),
            (
                "name of test -- example 2",
                {"productId": 2, "productName": "name_2", "price": 1},
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
                "Price is zero",
                {"productId": 1, "productName": "name_1", "price": 0},
            ),
            (
                "missing ProductName",
                {"productId": 2, "price": 1},
            ),
        ]

    def test_v1(self):
        for name, data in self.get_test_cases():
            with self.subTest(msg=name):
                with self.assertRaises(ValidationError):
                    validate(instance=data, schema=self.schema)


if __name__ == "__main__":
    unittest.main()
