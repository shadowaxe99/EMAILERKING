import unittest
from src.response_generator import ResponseGenerator
from src.utils import Utils


class TestEmailResponseSystem(unittest.TestCase):
    def test_generate_response(self):
        response_generator = ResponseGenerator()
        email = 'example@example.com'
        response = response_generator.generate_response(email)
        self.assertIsNotNone(response)

    def test_validate_email(self):
        utils = Utils()
        email = 'example@example.com'
        valid = utils.validate_email(email)
        self.assertTrue(valid)

    def test_validate_input(self):
        utils = Utils()
        input_data = 'example'
        valid = utils.validate_input(input_data)
        self.assertTrue(valid)


if __name__ == '__main__':
    unittest.main()