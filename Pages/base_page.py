from playwright.sync_api import Page

class BasePage:
  def __init__(self, page: Page):
    self.page = page

  def goto(self, url):
    self.page.goto(url)

  def close(self):
    self.driver.quit()