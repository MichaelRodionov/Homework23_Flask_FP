from flask import abort

from utils.constants import SORT_PARAMS


# ----------------------------------------------------------------
# class FileHandler to handle file
class FileHandler:
    def __init__(self, file, params: dict, result=None) -> None:
        """
        CConstructor for FileHandler
        :param file: file to handle with
        :param params: collection of params (commands, values)
        :param result: result of handle
        """
        self.__file = file
        self.__params = params
        self.__result = result

    @property
    def params(self) -> dict:
        """
        Getter for params
        :return: private attribute __params
        """
        return self.__params

    @property
    def file(self):
        """
        Getter for file
        :return: private attribute __file
        """
        return self.__file

    @property
    def result(self):
        """
        Getter for result
        :return: private attribute __result
        """
        return self.__result

    @result.setter
    def result(self, result) -> None:
        """
        Setter for result
        :param result: new data to overwrite private attribute __result
        :return: overwritten attribute __result
        """
        self.__result = result

    def get_result(self):
        """
        Method to start execution and get final result
        :return: result of handle
        """
        self.execute()
        return self.result

    def execute(self) -> None:
        """
        Main method of file handle. Runs first command with first value, then - second with second value.
        Finally, used setter to overwrite private attribute __result
        :return: None
        """
        result = map(lambda v: v.strip(), self.file)
        command_1, value_1 = self.params.get('request_1')
        command_2, value_2 = self.params.get('request_2')
        result = self.get_command().get(command_1)(result, value_1)
        result = self.get_command().get(command_2)(result, value_2)
        self.result = result

    def get_command(self) -> dict:
        """
        Method forms dictionary where keys are commands names and values are methods to handle file
        :return: dict with commands
        """
        commands: dict = {
            'filter': self.__filter,
            'map': self.__map,
            'unique': self.__unique,
            'sort': self.__sort,
            'limit': self.__limit
        }
        return commands

    @staticmethod
    def __filter(res, value: str):
        """
        Method to filter data by given value
        :param res: our data
        :param value: filter value
        :return: filter object
        """
        return filter(lambda text: value in text, res)

    @staticmethod
    def __map(res, column: str) -> map:
        """
        Method to map data by given column
        :param res: our data
        :param column: column number to map
        :return: map object
        """
        try:
            column = int(column)
        except ValueError:
            column = 0
        return map(lambda text: text.split(' ')[column], res)

    @staticmethod
    def __unique(res, value='') -> iter:
        """
        Method to get unique data
        :param res: our data
        :param value: ''
        :return: iterator object of unique data
        """
        return iter(set(res))

    @staticmethod
    def __sort(res, value_order: str) -> sorted:
        """
        Method to sort data by asc or desc
        :param res: our data
        :param value_order: asc or desc
        :return: sorted object
        """
        if value_order not in SORT_PARAMS:
            abort(400, 'You must point asc or desc sorting parameters')
        return sorted(res, reverse=False if value_order == 'asc' else True)

    @staticmethod
    def __limit(res, value_limit: str) -> list:
        """
        Method to limit the output of the final result
        :param res: our data
        :param value_limit: limit of data size
        :return: limited list of data
        """
        try:
            limit = int(value_limit)
        except ValueError:
            limit = 0
        return list(res)[:limit]
