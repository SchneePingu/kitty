import subprocess
import os


class Test_Helper():
    def __init__(self):
        self.path_to_tests_directory = self.__get_path_to_tests_directory()
        self.path_to_test_file_system = self.__get_path_to_test_file_system()
        self.path_to_kitty_executable = self.__get_path_to_kitty_executable()

    def __get_path_to_tests_directory(self):
        path_to_tests_directory = os.path.join(os.path.dirname(__file__), '..')

        return path_to_tests_directory

    def __get_path_to_test_file_system(self):
        name_of_test_file_system = 'data'
        path_to_test_file_system = os.path.join(self.path_to_tests_directory, name_of_test_file_system)

        return path_to_test_file_system

    def __get_path_to_kitty_executable(self):
        path_to_kitty_executable = os.path.join(self.path_to_tests_directory, '..', 'sh' ,'kitty')

        return path_to_kitty_executable

    def change_to_test_file_system(self):
        os.chdir(self.path_to_test_file_system)

    def run_kitty(self, *args):
        kitty_arguments = list(args)
        search_result = subprocess.run([self.path_to_kitty_executable] + kitty_arguments, stdout=subprocess.PIPE) \
            .stdout.decode('utf-8').strip().split(os.linesep)

        return search_result
