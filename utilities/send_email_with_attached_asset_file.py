
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import zipfile

def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment_paths):
    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(body, 'plain'))

    # Attach HTML report
    with open(attachment_paths[0], "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(attachment_paths[0])}",
        )
        msg.attach(part)

    # Attach zip file with assets
    with open(attachment_paths[1], "rb") as zip_file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(zip_file.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(attachment_paths[1])}",
        )
        msg.attach(part)

    # Log in to server using the sender's email and password
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        # Send email
        server.sendmail(sender_email, recipient_email, msg.as_string())

def zip_assets_folder(folder_path, output_zip_path):
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

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
    html_report_path = "../report/report.html"
    assets_folder_path = "./report/assess"
    zip_path = "../report/asset.zip"

    zip_assets_folder(assets_folder_path, zip_path)
    attachment_paths = [html_report_path, zip_path]
    send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment_paths)


