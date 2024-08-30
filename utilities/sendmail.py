
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment_path):
    try:
        # Create a multipart message and set headers
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add body to email
        msg.attach(MIMEText(body, 'plain'))

        # Open the file to be sent
        with open(attachment_path, "rb") as attachment:
            # MIMEBase is a base class for all MIME-specific subtypes
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        # Encode the file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(attachment_path)}",
        )

        # Attach the file to the message
        msg.attach(part)

        # Log in to server using the sender's email and password
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            # Send email
            server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    # Set the email details
    sender_email = "assessbill5@gmail.com"
    sender_password = "gwae jcuq csgu irpe"
    recipient_email = "abill2363@gmail.com"
    subject = "Test Automation Report"
    body = "Please find the attached HTML report."

    # Use absolute path to the report file
    project_root = os.path.dirname(os.path.abspath(__file__))  # Path to the directory containing this script
    attachment_path = os.path.join(project_root, '..', 'report', 'report.html')
    # Resolve absolute path
    attachment_path = os.path.abspath(attachment_path)

    # attachment_path = "../report/report.html"

    # Invoke the send email method
    send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment_path)


