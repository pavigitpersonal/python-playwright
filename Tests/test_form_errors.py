import pytest
from Journeys.submit_form_successfully import SubmitForm

@pytest.mark.smoke
def test_form_error1(page):
  submit_form = SubmitForm(page)
  assert(1).__eq__(1)

@pytest.mark.regression
def test_form_error2(page):
  submit_form = SubmitForm(page)
  assert(1).__eq__(1)

@pytest.mark.regression
def test_form_error3(page):
  submit_form = SubmitForm(page)
  assert(1).__eq__(2)