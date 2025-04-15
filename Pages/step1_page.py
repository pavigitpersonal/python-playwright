from playwright.sync_api import Page, expect
from Pages.base_page import BasePage
# from Helpers.json_loader import load_data
from datetime import datetime
from Helpers.page_helper import Helper
# from Context.test_context import TestContext
from Fixtures.test_data import FormData

class Step1Page(BasePage):

  def __init__(self, page: Page):
    super().__init__(page)
    self._step_info = page.locator("#stepInfo")
    self._name = page.locator("input#name")
    self._id_number = page.locator("input#idNum")
    self._email = page.locator("input#email")
    self._date_of_birth = page.locator("input#birthdate")

  def enter_name(self, name):
    self.page.get_by_role("textbox", name = "Name").fill(name, timeout = 5000)

  def enter_id_number(self, id_number):
    self._id_number.fill(id_number)

  def enter_email(self, email):
    self._email.fill(email)

  # def get_page_title(self):
  #   return self.page.locator("h1").text_content()

  # def get_step_info(self):
  #   return self._step_info.text_content()

  def enter_date_of_birth(self, date_of_birth: str):
    self._date_of_birth.click()
    extracted_date = datetime.strptime(date_of_birth, "%d/%m/%Y")
    extracted_day = str(extracted_date.day)
    extratced_month = str(extracted_date.month)
    extracted_year = str(extracted_date.year)
    self._date_of_birth.press_sequentially(extracted_day, delay = 300)
    self._date_of_birth.press_sequentially(extratced_month, delay = 300)
    self._date_of_birth.press_sequentially(extracted_year)

  def fill_step1_form(self):
    assert (Helper.get_page_title(self.page)).__eq__(FormData.page_heading)
    assert (Helper.get_step_info(self.page)).__eq__(FormData.step1_page_name)
    self.enter_name(FormData.name)
    self.enter_id_number(FormData.id_number)
    self.enter_email(FormData.email)
    self.enter_date_of_birth(FormData.date_of_birth)
    Helper.click_button(self.page, FormData.next_button)


