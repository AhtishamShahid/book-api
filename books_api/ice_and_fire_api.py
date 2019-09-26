import requests


class IceAndFireAPI:
    base_url = 'https://www.anapioficeandfire.com/api/'

    def get_books(self, query):
        return self.__get('books', params=query)

    def __get(self, path, params):
        url = self.base_url + path
        data = requests.get(url, params=params)
        return Response(data)


class Response:
    status = ''
    status_code = ''
    data = []
    initial_data = None

    def __init__(self, data):
        self.initial_data = data
        self.status_code = data.status_code
        self.data = self.__make_data()

    def __make_data(self):
        if self.initial_data:
            return self.initial_data.json()
        else:
            return dict()
