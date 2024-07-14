import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_emails(sender_email, sender_password, recipient_list, subject, message):
  """
  Sends email messages to a list of email addresses.

  Args:
      sender_email (str): Email address of the sender.
      sender_password (str): Password for the sender's email account.
      recipient_list (list): List of recipient email addresses.
      subject (str): Subject of the email.
      message (str): Content of the email message (plain text).
  """

  # Create the email object
  email = MIMEMultipart()
  email["From"] = sender_email
  email["To"] = ", ".join(recipient_list)  # Join recipients with comma
  email["Subject"] = subject

  # Attach the plain text message
  email.attach(MIMEText(message, "plain"))

  # Connect to the SMTP server (replace with your mail server)
  with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, sender_password)

    # Send email to each recipient
    for recipient in recipient_list:
      server.sendmail(sender_email, recipient, email.as_string())

# Example usage
sender_email = "wealthyjunior01@gmail.com"
sender_password = "Centrillion01@"
recipient_list = ["recipient1@example.com", "recipient2@example.com"]
subject = "Test Email"
message = "This is a test email sent from Python."

send_emails(sender_email, sender_password, recipient_list, subject, message)

print("Emails sent successfully!")
