import unittest
import Test_Helper


class Kitty_Test(unittest.TestCase):
    def setUp(self):
        self.test_helper = Test_Helper.Test_Helper()
        self.test_helper.change_to_test_file_system()
        
    def test_file_search(self):
        actual_search_result = self.test_helper.run_kitty('-f', 'Mouse')
        expected_search_result = './firstMouse.txt\n./mousehole/secondMouse.txt\n'

        self.assertEqual(actual_search_result, expected_search_result)

    def test_directory_search(self):
        actual_search_result = self.test_helper.run_kitty('-d', 'hole')
        expected_search_result = './mousehole\n'

        self.assertEqual(actual_search_result, expected_search_result)

    def test_file_content_search(self):
        actual_search_result = self.test_helper.run_kitty('-c', 'mouse')
        self.maxDiff = None
        expected_search_result = './firstMouse.txt:1:This is the first mouse to catch.\n--\n./mousehole/secondMouse.txt:1:This is the second mouse to catch.\n'

        self.assertEqual(actual_search_result, expected_search_result)


if __name__ == '__main__':
    unittest.main()
