from playwright.sync_api import Page, expect
from Pages.base_page import BasePage
from Helpers.page_helper import Helper
from Fixtures.test_data import FormData

class Step4Page(BasePage):

  def __init__(self, page: Page):
    super().__init__(page)
    self._form_summary = page.locator("section[aria-label='Form Summary']")
    self._confirmation_message = page.locator("div#form-message")
    self._name_value = page.locator("p#name-val")

  def get_sumbit_confirmation_message(self):
    message = self._confirmation_message.text_content()
    return message.strip()

  def submit_form(self):
    assert (Helper.get_page_title(self.page)).__eq__(FormData.page_heading)
    assert (Helper.get_step_info(self.page)).__eq__(FormData.step4_page_name)
    expect(self._form_summary).to_be_visible()
    expect(self._name_value).to_be_visible()
    Helper.click_button(self.page, FormData.submit_button)
    expect(self._confirmation_message).to_have_text(FormData.confirmation_message.value)



