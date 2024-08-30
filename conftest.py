# import pytest
# import subprocess
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     # Path to the generated HTML report file
#     report_path = "report.html"  # Update this with the actual path
#
#     # Run the sendmail.py script
#     subprocess.run(["python", "./utilities/sendmail.py"])  # Update this with the correct path


import pytest
import subprocess
from utilities.sendmail import send_email_with_attachment

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    # Parameters for the email
    sender_email = "assessbill5@gmail.com"
    sender_password = "Albertbill100%"
    recipient_email = "abill2363@gmail.com"
    subject = "Test Automation Report"
    body = "Please find the attached HTML report."
    report_path = "./report/report.html"  # Update with the actual path to the report

    # Ensure the report file exists (you may want to check this)
    try:
        with open(report_path, 'r') as file:
            pass
    except FileNotFoundError:
        print(f"Report file not found: {report_path}")
        return

    # Call the function to send the email with the report attached
    send_email_with_attachment(
        sender_email=sender_email,
        sender_password=sender_password,
        recipient_email=recipient_email,
        subject=subject,
        body=body,
        attachment_path=report_path
    )
