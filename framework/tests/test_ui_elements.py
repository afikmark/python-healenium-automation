import pytest
from selenium.webdriver.common.by import By
from framework.ui_elements import TextInput, Locator, Button, HyperLink, DropDown, Table


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


@pytest.fixture
def table(mock_driver):
    return Table('//table', mock_driver)


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


def test_table_get_all_rows(table, mock_driver, mocker):
    mock_row1 = mocker.Mock()
    mock_row2 = mocker.Mock()
    mock_driver.find_elements.return_value = [mock_row1, mock_row2]

    rows = table.get_all_rows()
    assert len(rows) == 2
    assert rows[0] == mock_row1
    assert rows[1] == mock_row2


def test_table_get_row(table, mock_driver, mocker):
    mock_row = mocker.Mock()
    mock_cell1 = mocker.Mock()
    mock_cell2 = mocker.Mock()
    mock_row.find_elements.return_value = [mock_cell1, mock_cell2]
    mock_driver.find_elements.return_value = [mock_row]

    row = table.get_row(0)
    assert len(row) == 2
    assert row[0] == mock_cell1
    assert row[1] == mock_cell2


def test_table_get_cell(table, mock_driver, mocker):
    mock_row = mocker.Mock()
    mock_cell = mocker.Mock()
    mock_row.find_elements.return_value = [mock_cell]
    mock_driver.find_elements.return_value = [mock_row]

    cell = table.get_cell(0, 0)
    assert cell == mock_cell
