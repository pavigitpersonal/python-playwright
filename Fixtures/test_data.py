from enum import Enum

class FormData(str, Enum):
  page_heading = "Personal Registration Form"
  step1_page_name = "Step 1 of 4"
  step2_page_name = "Step 2 of 4"
  step3_page_name = "Step 3 of 4"
  step4_page_name = "Step 4 of 4"
  name = "John Doe"
  id_number = "123456789"
  email = "a@b.com"
  date_of_birth = "11/11/2001",
  department = "Information Technology"
  skills = "Java, Python, C++, C#"
  next_button = "Next"
  submit_button = "Confirm and Submit"
  confirmation_message = "Form submitted successfully!"