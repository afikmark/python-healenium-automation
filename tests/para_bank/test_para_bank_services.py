import pytest


@pytest.mark.parametrize('service_table_data', (['bookstore_content', 'bookstore_v2_content']), indirect=True)
def test_services_table(para_bank_ui, service_table_data):
    """This test verifies the content of the services table in parabank/services"""
    services_page = para_bank_ui.services_page
    services_page.open()
    row, expected_text = service_table_data
    bookstore_content_cell = services_page.services_table.get_cell(row_index=row, col_index=1)
    assert bookstore_content_cell.text == expected_text
