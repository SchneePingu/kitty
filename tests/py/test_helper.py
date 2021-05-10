"""
This module provides a method to run the 'kitty' command in test code.
"""

import subprocess
import os


def run_kitty(*args):
    """Run 'kitty' executable with command line arguments."""
    path_to_data = os.path.join('tests', 'data')
    path_to_kitty = os.path.join('..', '..', 'sh', 'kitty')

    kitty_arguments = list(args)

    search_result = subprocess.run([path_to_kitty] + kitty_arguments, \
        stdout=subprocess.PIPE, \
        cwd=path_to_data, \
        check=True) \
        .stdout.decode('utf-8').strip()

    return search_result.split(os.linesep)
