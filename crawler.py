import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import requests
import time

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your email provider's SMTP server
SMTP_PORT = 587
EMAIL_USER = ''  # Your email address
EMAIL_PASS = ''  # Your email password
TO_EMAIL = 'farmerlesheng@gmail.com'  # Recipient's email address

# Binance URL
BINANCE_URL = 'https://www.binance.com/en/support/announcement/new-cryptocurrency-listing?c=48&navId=48'

# File to store the last fetched announcement title
LAST_ANNOUNCEMENT_FILE = 'last_announcement.txt'

def fetch_announcements():
    """Fetch announcements from Binance."""
    try:
        response = requests.get(BINANCE_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Adjust the selector to match Binance's announcement titles
        titles = soup.select('.css-6f91y1 .css-1ej4hfo')  
        return [title.text.strip() for title in titles]
    except Exception as e:
        print(f"Error fetching announcements: {e}")
        return []

def send_email(subject, body):
    """Send an email notification."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = TO_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, TO_EMAIL, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    try:
        # Load the last announcement title
        try:
            with open(LAST_ANNOUNCEMENT_FILE, 'r') as file:
                last_announcement = file.read().strip()
        except FileNotFoundError:
            last_announcement = ''
        
        # Fetch current announcements
        announcements = fetch_announcements()
        if not announcements:
            print("No announcements found.")
            return
        
        # Compare the latest announcement with the stored one
        latest_announcement = announcements[0]
        if latest_announcement != last_announcement:
            print(f"New announcement detected: {latest_announcement}")
            send_email(
                subject="New Binance Announcement",
                body=f"A new announcement has been posted: {latest_announcement}\n\nCheck it out here: {BINANCE_URL}"
            )
            # Update the last announcement file
            with open(LAST_ANNOUNCEMENT_FILE, 'w') as file:
                file.write(latest_announcement)
        else:
            print("No new announcements.")
    
    except Exception as e:
        print(f"Error in main function: {e}")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(300)  # Check every 5 minutes
