import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender_email = "cryptotangyou@gmail.com"
receiver_email = "farmerlesheng@gmail.com"
password = "qbec uwew wwux cjpt"

# Create the email content
subject = "Test Email"
body = "Hello, this is a test email sent from Python!"

# Create the MIMEText object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the email body to the email
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection
    
    # Log in to the server
    server.login(sender_email, password)
    
    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
    
except Exception as e:
    print(f"Error: {e}")

finally:
    server.quit()  # Close the connection to the server

