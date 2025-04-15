from playwright.sync_api import Page, expect
from Pages.base_page import BasePage
from Helpers.page_helper import Helper
from Fixtures.test_data import FormData

class Step3Page(BasePage):

  def __init__(self, page: Page):
    super().__init__(page)
    self._skills_input = page.locator("textarea#skills")
    self._terms_and_conditions = page.locator("input#terms")

  def enter_skills(self, skills: str):
    self._skills_input.fill(skills)

  def agree_to_terms_and_conditions(self):
    self._terms_and_conditions.check()

  def fill_step3_form(self):
    assert (Helper.get_page_title(self.page)).__eq__(FormData.page_heading)
    assert (Helper.get_step_info(self.page)).__eq__(FormData.step3_page_name)
    self.enter_skills(FormData.skills)
    self.agree_to_terms_and_conditions()
    Helper.click_button(self.page, FormData.next_button)


