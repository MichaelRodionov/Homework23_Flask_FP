import os

from utils.constants import QUERY_KEYS


# ----------------------------------------------------------------
# class Validator to validate input values
class Validator:
    @staticmethod
    def is_correct(args: dict) -> bool:
        """
        Check input values method
        :param args: dict of input values
        :return: True if input values are correct and not empty
        """
        if not args:
            return False
        elif args.keys() != QUERY_KEYS:
            return False
        return True

    @staticmethod
    def check_file_exists(file_path) -> bool:
        """
        Check if file exists
        :param file_path: path to directory with some data
        :return: True if file exists, else False
        """
        return False if not os.path.exists(file_path) else True
