from playwright.sync_api import Page
from Pages.step1_page import Step1Page
from Pages.step2_page import Step2Page
from Pages.step3_page import Step3Page
from Pages.step4_page import Step4Page

class SubmitForm:
  def __init__(self, page: Page):
    self.page = page

  def submit_form_successfully(self):
    Step1Page(self.page).fill_step1_form()
    Step2Page(self.page).fill_step2_form()
    Step3Page(self.page).fill_step3_form()
    Step4Page(self.page).submit_form()