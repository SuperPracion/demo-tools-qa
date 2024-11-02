import allure
import pytest

from api.swapi import SWAPI

@allure.title('Test people data')
class TestPeople:
    @allure.step('send valid person id')
    @pytest.mark.parametrize('id, name', [
        (1, 'Luke Skywalker'),
        (2, 'C-3PO'),
        (3, 'R2-D2'),
        (4, 'Darth Vader')
    ])
    def test_valid_people(self, id, name):
        swapi = SWAPI()
        response = swapi.people(id)
        assert response.json()['name'] == name

    @allure.step('send invalid people id')
    @pytest.mark.parametrize('id, code', [
        (0, 404),
        (-1, 404),
        ('a', 404),
        ('!', 404)
    ])
    def test_invalid_people(self, id, code):
        swapi = SWAPI()
        response = swapi.people(id)
        assert response.status_code == code