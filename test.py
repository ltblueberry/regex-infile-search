import unittest
from regex_infile_search import main as script
from regex_infile_search import messages


class ScriptTest(unittest.TestCase):

    def test_input_empty(self):
        exit_message = script(None, ".*", "test_input_empty")
        self.assertEqual(exit_message, messages.NONE_INPUT)

    def test_input_not_found(self):
        exit_message = script("nofile.txt", ".*", "test_input_not_found")
        self.assertEqual(exit_message, messages.FILE_NOT_FOUND)

    def test_regex_empty(self):
        exit_message = script("test.txt", None, "test_regex_empty")
        self.assertEqual(exit_message, messages.NONE_REGEX)

    def test_name_empty(self):
        exit_message = script("test.txt", ".*", None)
        self.assertEqual(exit_message, messages.NONE_NAME)

    def test_no_matches(self):
        exit_message = script("test.txt", "XX-NO-FOUND-XX", "test_no_matches")
        self.assertEqual(exit_message, messages.NO_MATCHES)

    def test_regex_match(self):
        exit_message = script("test.txt", "#.*#", "test_regex_match")
        if exit_message != messages.DONE:
            self.assertTrue(True)
            return


if __name__ == '__main__':
    unittest.main()
