"""
This module provides a class to run the 'kitty' command in test code.
"""

import subprocess
import os
import re


class TestHelper:
    """Class to run the 'kitty' command in test code."""

    def __init__(self):
        self._path_to_data = os.path.join('tests', 'data')
        self._path_to_kitty = os.path.join('..', '..', 'sh', 'kitty')

    def run_kitty(self, *args):
        """Run 'kitty' executable with command line arguments."""
        kitty_arguments = list(args)

        search_result = subprocess.run([self._path_to_kitty] + kitty_arguments, \
            stdout=subprocess.PIPE, \
            cwd=self._path_to_data, \
            check=True) \
            .stdout.decode('utf-8').strip()

        return self.remove_ansi_color_escape_codes(search_result).split(os.linesep)

    @staticmethod
    def remove_ansi_color_escape_codes(search_result):
        """Remove ANSI color escape codes from 'kitty' search result."""
        ansi_color_escape_codes = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_color_escape_codes.sub('', search_result)
