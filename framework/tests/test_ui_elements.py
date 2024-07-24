import pytest
from selenium.webdriver.common.by import By
from framework.ui_elements import TextInput, Locator, Button, HyperLink, DropDown


@pytest.fixture
def mock_driver(mocker):
    return mocker.Mock()


@pytest.fixture
def text_input(mock_driver):
    return TextInput('#input', mock_driver, By.CSS_SELECTOR)


@pytest.fixture
def button(mock_driver):
    return Button('#button', mock_driver, By.CSS_SELECTOR)


@pytest.fixture
def dropdown(mock_driver):
    return DropDown('#dropdown', mock_driver, By.CSS_SELECTOR)


@pytest.fixture
def hyperlink(mock_driver):
    return HyperLink('#link', mock_driver, By.CSS_SELECTOR)


def test_text_input_enter_text(text_input, mock_driver, mocker):
    mock_element = mocker.Mock()

    mock_driver.find_element.return_value = mock_element

    text_input.enter_text("hello")

    # Verify that the clear method was called once on the mock element
    mock_element.clear.assert_called_once()
    # Verify that the send_keys method was called once with the argument "hello"
    mock_element.send_keys.assert_called_once_with("hello")


def test_text_input_value(text_input, mock_driver, mocker):
    mock_element = mocker.Mock()

    mock_driver.find_element.return_value = mock_element
    # Mock the execute_script method to return a test value
    mock_driver.execute_script.return_value = "test value"

    # Call the method under test
    value = text_input.value

    # Assert that the value is as expected
    assert value == "test value"
    # Verify the interactions with the mock object
    mock_driver.find_element.assert_called_once_with(Locator(By.CSS_SELECTOR, '#input'))
    mock_driver.execute_script.assert_called_once_with("return arguments[0].value", mock_element)


def test_button_click(button, mock_driver, mocker):
    mock_element = mocker.Mock()
    mock_driver.find_element.return_value = mock_element
    button.click()
    # Verify the click method was called once on the mock element
    mock_driver.click.assert_called_once_with(Locator(By.CSS_SELECTOR, '#button'))


def test_button_text(button, mock_driver, mocker):
    mock_element = mocker.Mock()
    mock_driver.find_element.return_value = mock_element
    mock_driver.get_text.return_value = "Submit"

    text = button.text

    # Assert the text value is as expected
    assert text == "Submit"
    # Verify the get_text method was called once
    mock_driver.get_text.assert_called_once_with(Locator(By.CSS_SELECTOR, '#button'))






