from playwright.sync_api import Page, expect
from Pages.base_page import BasePage
from Helpers.page_helper import Helper
from Fixtures.test_data import FormData

class Step2Page(BasePage):

  def __init__(self, page: Page):
    super().__init__(page)
    self._file_input_selector = "input#document"
    self._department_dropdown = page.locator("select#department")

  def upload_file(self):
    Helper.upload_file(self.page, self._file_input_selector, "Resources/sample_pdf_file.pdf")

  def select_department(self, department: str):
    self._department_dropdown.select_option(department)

  def fill_step2_form(self):
    assert (Helper.get_page_title(self.page)).__eq__(FormData.page_heading)
    assert (Helper.get_step_info(self.page)).__eq__(FormData.step2_page_name)
    self.upload_file()
    self.select_department(FormData.department)
    Helper.click_button(self.page, FormData.next_button)


