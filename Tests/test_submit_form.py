import pytest
from Journeys.submit_form_successfully import SubmitForm

@pytest.mark.smoke
def test_form_submission(page):
  submit_form = SubmitForm(page)
  submit_form.submit_form_successfully()

@pytest.mark.regression
def test_sync(page):
  submit_form = SubmitForm(page)
  assert True

@pytest.mark.smoke
def test_page_fixture(page):
  submit_form = SubmitForm(page)
  assert(1).__eq__(2)