import unittest
import TestHelper


class Kitty_Test(unittest.TestCase):
    def setUp(self):
        self.test_helper = TestHelper.Test_Helper()
        self.test_helper.change_to_test_file_system()
        
    def test_file_search(self):
        actual_search_result = self.test_helper.run_kitty('-f', 'Mouse')
        expected_search_result = ['./firstMouse.txt', './mousehole/secondMouse.txt']

        self.assertCountEqual(actual_search_result, expected_search_result)

    def test_directory_search(self):
        actual_search_result = self.test_helper.run_kitty('-d', 'hole')
        expected_search_result = ['./mousehole']

        self.assertCountEqual(actual_search_result, expected_search_result)

    def test_file_content_search(self):
        actual_search_result = self.test_helper.run_kitty('-c', 'mouse')
        self.maxDiff = None
        expected_search_result = ['./firstMouse.txt:1:This is the first mouse to catch.', '--', './mousehole/secondMouse.txt:1:This is the second mouse to catch.']

        self.assertCountEqual(actual_search_result, expected_search_result)


if __name__ == '__main__':
    unittest.main()
