import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Email credentials (hardcoded for this example)
sender_email = "cryptotangyou@gmail.com"
receiver_email = "farmerlesheng@gmail.com"
password = "qbec uwew wwux cjpt"  # Replace with your app password

# Email send interval and duration
interval_seconds = 60  # 60 seconds between emails
max_emails = 20  # Maximum number of emails to send

# Track the number of emails sent
email_count = 0

# Create the email content
subject = "Test Email"
body = "Hello, this is a test email sent from Python every 60 seconds!"

# Create the MIMEText object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Function to send an email
def send_email():
    global email_count
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection

        # Log in to the server
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        email_count += 1  # Increment email count
        print(f"Email {email_count} sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        server.quit()  # Close the connection to the server

# Send emails every 60 seconds until the email count reaches 20
while email_count < max_emails:
    send_email()
    if email_count >= max_emails:
        print("Reached 20 emails. Exiting...")
        break  # Exit after 20 emails
    time.sleep(interval_seconds)  # Wait for 60 seconds before sending the next email

print("Completed sending emails.")
