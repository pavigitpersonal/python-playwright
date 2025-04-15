import pytest
from playwright.sync_api import Page, expect

class Helper:
  @staticmethod
  def click_button(page: Page, button_name: str):
    page.get_by_role("button", name = button_name).click()

  @staticmethod
  def upload_file(page: Page, selector: str, file_path: str):
    page.set_input_files(selector, file_path)

  @staticmethod
  def get_page_title(page: Page):
    expect(page.locator("h1")).to_be_visible()
    text = page.locator("h1").text_content()
    return text.strip()

  @staticmethod
  def get_step_info(page: Page):
    return page.locator("#stepInfo").text_content()