import unittest
from tasks import check_brackets


class TestCheckBrackets(unittest.TestCase):
    def test_check_brackets(self):
        test_data = [
            ("((([])))", "Сбалансированно"),
            ("[([])((([[[]]])))]{}", "Сбалансированно"),
            ("{{[()]}}", "Сбалансированно"),
            ("}{(})", "Несбалансированно"),
            ("{[(])]}}", "Несбалансированно"),
            ("[[{()}]", "Несбалансированно"),
            ("", "Сбалансированно"),
        ]

        for i, (input_string, expected) in enumerate(test_data):
            with self.subTest(input_string=input_string):
                self.assertTrue(check_brackets(input_string), expected)
