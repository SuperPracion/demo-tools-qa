import allure
import requests


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    @allure.step('send get request')
    def get(url):
        res = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return res

    @staticmethod
    @allure.step('send post request')
    def post(url, body):
        res = requests.post(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
        return res

    @staticmethod
    @allure.step('send put request')
    def put(url, body):
        res = requests.put(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
        return res

    @staticmethod
    @allure.step('send delete request')
    def delete(url, body):
        res = requests.delete(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie, json=body)
        return res