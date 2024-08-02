from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from typing import NamedTuple


class Locator(NamedTuple):
    """ Locator object """
    by: str
    selector: str


class Component:
    """Basic UI Component"""

    def __init__(self, root_selector, driver, by: str = By.CSS_SELECTOR):
        self._driver = driver
        self._locator = Locator(by, root_selector)


class TextInput(Component):
    """ TextInput object """

    def __init__(self, root_selector, driver, by: str = By.CSS_SELECTOR):
        super().__init__(root_selector, driver, by)
        self.root_selector = root_selector
        self._driver = driver
        self._locator = Locator(by, self.root_selector)

    @property
    def value(self) -> str:
        """
        returns the current value in input
        :return: str
        """
        element = self._driver.find_element(self._locator)
        return self._driver.execute_script(f"return arguments[0].value", element)

    def enter_text(self, text: str) -> None:
        """ enters text to element """
        element = self._driver.find_element(self._locator)
        element.clear()
        element.send_keys(text)

    def clear_text(self) -> None:
        """
        clears text
        :return:None
        """
        element = self._driver.find_element(self._locator)
        element.clear()


class Button(Component):
    """ Button object """

    def __init__(self, root_selector, driver, by: str = By.CSS_SELECTOR):
        super().__init__(root_selector, driver, by)
        self.root_selector = root_selector
        self._driver = driver
        self._locator = Locator(by, self.root_selector)

    @property
    def text(self) -> str:
        return self._driver.get_text(self._locator)

    def click(self) -> None:
        self._driver.click(self._locator)


class DropDown(Component):
    """ DropDown Object """

    def __init__(self, root_selector, driver, by: str = By.CSS_SELECTOR):
        super().__init__(root_selector, driver, by)
        self.root_selector = f'.select_container {root_selector}'
        self._driver = driver
        self._locator = Locator(by, self.root_selector)

    @property
    def options(self) -> list:
        element = self._driver.find_element(self._locator)
        return Select(element).options

    def select_by_value(self, value: str) -> None:
        element = self._driver.find_element(self._locator)
        Select(element).select_by_value(value)

    def select_by_index(self, index: int) -> None:
        element = self._driver.find_element(self._locator)
        Select(element).select_by_index(index)


class HyperLink(Component):
    """Hyper link object"""

    def __init__(self, root_selector: str, driver, by: str = By.CSS_SELECTOR):
        super().__init__(root_selector, driver, by)
        self._driver = driver
        self._locator = Locator(by, root_selector)

    @property
    def label(self) -> str:
        """
        Returns the text label for hyperlink
        """
        return self._driver.get_text(self._locator)

    def click_link(self) -> None:
        """Clicks on hyperlink"""
        self._driver.click(self._locator)


class Table(Component):
    """ Table object """

    def __init__(self, root_selector, driver, by: str = By.XPATH):
        super().__init__(root_selector, driver, by)
        self.root_selector = root_selector
        self._driver = driver
        self._locator = Locator(by, self.root_selector)

    def get_all_rows(self) -> list:
        """
        Returns all rows of the table.
        :return: List of WebElement rows
        """
        return self._driver.find_elements(Locator(By.XPATH, f"{self.root_selector}//tr"))

    def get_row(self, row_index: int) -> list:
        """
        Returns a specific row by index.
        :param row_index: Index of the row (0-based)
        :return: List of WebElement cells in the row
        """
        rows = self.get_all_rows()
        return rows[row_index].find_elements(By.XPATH, ".//td")

    def get_cell(self, row_index: int, col_index: int):
        """
        Returns a specific cell in the table.
        :param row_index: Index of the row (0-based)
        :param col_index: Index of the column (0-based)
        :return: WebElement of the cell
        """
        row = self.get_row(row_index)
        return row[col_index]

    def get_cell_text(self, row_index: int, col_index: int) -> str:
        """
        Returns the text of a specific cell.
        :param row_index: Index of the row (0-based)
        :param col_index: Index of the column (0-based)
        :return: Text content of the cell
        """
        cell = self.get_cell(row_index, col_index)
        return cell.text

    def click_cell(self, row_index: int, col_index: int) -> None:
        """
        Clicks a specific cell.
        :param row_index: Index of the row (0-based)
        :param col_index: Index of the column (0-based)
        :return: None
        """
        cell = self.get_cell(row_index, col_index)
        cell.click()
