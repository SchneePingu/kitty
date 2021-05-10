"""
This module provides a class for checking the search result
of the 'kitty' command.
"""

import unittest
import test_helper


class TestSearchResult(unittest.TestCase):
    """Class to test the search result of 'kitty'."""

    def test_file_search(self):
        """Test searching a file matching a pattern."""
        actual_search_result = test_helper.run_kitty('-f', 'Mouse')
        expected_search_result = ['./firstMouse.txt', './mousehole/secondMouse.txt', \
                                  './binaryMouse']

        self.assertCountEqual(actual_search_result, expected_search_result) # pylint: disable=no-member

    def test_directory_search(self):
        """Test searching a directory matching a pattern."""
        actual_search_result = test_helper.run_kitty('-d', 'hole')
        expected_search_result = ['./mousehole']

        self.assertCountEqual(actual_search_result, expected_search_result) # pylint: disable=no-member

    def test_file_content_search(self):
        """Test searching a file content matching a pattern."""
        actual_search_result = test_helper.run_kitty('-c', 'mouse')
        self.maxDiff = None # pylint: disable=invalid-name
        expected_search_result = ['./firstMouse.txt:1:This is the first mouse to catch.', '--', \
            './mousehole/secondMouse.txt:1:This is the second mouse to catch.']

        self.assertCountEqual(actual_search_result, expected_search_result) # pylint: disable=no-member


if __name__ == '__main__':
    unittest.main()
