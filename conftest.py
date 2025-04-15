import pytest
import os
from config import Config
from playwright.sync_api import sync_playwright
from datetime import datetime
from pytest_html import extras
import base64


def pytest_addoption(parser):
  parser.addoption("--browser", action="store", default=Config.DEFAULT_BROWSER, help="chromium|firefox|webkit")
  parser.addoption("--headless", action="store", default=str(Config.HEADLESS), help="true|false")
  parser.addoption("--slowmo", action="store", default=str(Config.SLOW_MO), help="Milliseconds to slow down")

@pytest.fixture(scope="session")
def base_url():
  index_path = os.path.abspath(Config.BASE_URL)
  file_url = f"file://{index_path}"
  return file_url

@pytest.fixture(scope="session")
def browser_config(pytestconfig):
  return {
      "name": pytestconfig.getoption("browser"),
      "headless": pytestconfig.getoption("headless").lower() == "true",
      "slow_mo": int(pytestconfig.getoption("slowmo"))
  }

@pytest.fixture(scope="function")
def browser_context(browser_config):
  with sync_playwright() as p:
    browser_type = {
        "chromium": p.chromium,
        "firefox": p.firefox,
        "webkit": p.webkit,
    }[browser_config["name"]]

    browser = browser_type.launch(
        headless=browser_config["headless"],
        slow_mo=browser_config["slow_mo"]
    )
    context = browser.new_context()
    yield context
    browser.close()

@pytest.fixture(scope="function")
def page(browser_context, base_url):
  print("Setting up page fixture")
  page = browser_context.new_page()
  page.set_default_timeout(Config.DEFAULT_TIMEOUT)
  page.goto(base_url)
  print("Going to base URL: ", base_url)
  yield page
  page.close()
  print("Page fixture completed")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
  outcome = yield
  report = outcome.get_result()

  if report.when == "call" and report.failed:
    page = item.funcargs.get("page", None)
    if page:
      try:
        # Create screenshots directory
        screenshots_dir = os.path.join("TestResults", "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        # Generate filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{item.name}_{timestamp}.png"
        filepath = os.path.join(screenshots_dir, filename)

        # Take screenshot
        page.screenshot(path=filepath, full_page=True)

        # Encode as base64
        with open(filepath, "rb") as image_file:
          encoded = base64.b64encode(image_file.read()).decode()

        # Embed clickable thumbnail
        html = (
          f'<a href="file://{os.path.abspath(filepath)}" target="_blank">'
          f'<img src="data:image/png;base64,{encoded}" '
          f'style="max-width:400px; border:1px solid #ccc;"/></a>'
        )

        report.extras = getattr(report, 'extras', [])
        report.extras.append(extras.html(html))

      except Exception as e:
        print(f"⚠️ Screenshot capture failed: {e}")