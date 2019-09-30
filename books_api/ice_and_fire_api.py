import requests


class Request:

    def get(self, url, params):
        """
        Send get request to url and return Response Object
        :param url:
        :param params:
        :return: Response
        """
        data = requests.get(url, params=params)
        return Response(data)


class IceAndFireAPI:
    base_url = 'https://www.anapioficeandfire.com/api/'

    def get_books(self, query):
        path = self.make_path('books')
        return Request().get(path, query)

    def make_path(self, path):
        return self.base_url + path


class Response:
    """
    Create response object for API call
    """
    def __init__(self, data):
        self.initial_data = data
        self.status_code = data.status_code
        self.data = self.__make_data()
        self.initial_data = None

    def __make_data(self):
        data = dict()
        if self.initial_data:
            data = self.initial_data.json()
        return data
