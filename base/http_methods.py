import allure
import requests


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        #with allure.step('Отправка GET запроса'):
            res = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            return res

    @staticmethod
    def post(url, body):
        #with allure.step('Отправка POST запроса'):
            res = requests.post(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
            return res

    @staticmethod
    def put(url, body):
        #with allure.step('Отправка PUT запроса'):
            res = requests.put(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
            return res

    @staticmethod
    def delete(url, body):
        #with allure.step('Отправка DELETE запроса'):
            res = requests.delete(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
            return res