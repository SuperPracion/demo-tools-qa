import pytest

from pages.main.main import Main
from pages.interaction.interaction import Interaction
from pages.interaction.resizable import Resizable


@pytest.fixture
def resizable(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.interaction_button_click()
    interaction = Interaction(setup_driver)
    interaction.resizable_button_click()
    resizable = Resizable(setup_driver)
    yield resizable


def test_set_size_resizable_element_in_container(resizable):
    element = resizable.get_resizable_box_with_restriction()
    resizable.set_resizable_size(element, 300, 300)
    assert element.get_attribute('style') == 'width: 300px; height: 300px;'

def test_set_size_resizable_element(resizable):
    element = resizable.get_resizable()
    resizable.set_resizable_size(element, 100, 100)
    assert element.get_attribute('style') == 'width: 100px; height: 100px;'