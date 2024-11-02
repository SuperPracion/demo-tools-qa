from base.http_methods import HttpMethods


class SWAPI:
    """
    Источник: https://swapi.dev/
    Описание: Класс API для работы с методами проекта
    """

    def __init__(self, base=None, key=None) -> None:
        if not base:
            self.base = 'https://swapi.dev/api/'
        if not key:
            self.key = ''

    def people(self, id):
        resource = 'people/'
        url = self.base + resource + f'{id}'
        response = HttpMethods.get(url)
        return response

    def films(self, id):
        resource = 'films/'
        url = self.base + resource + f'{id}'
        response = HttpMethods.get(url)
        return response