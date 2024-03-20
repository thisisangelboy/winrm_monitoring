import time
import subprocess
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message):
    # Mailgun server login credentials
    mailgun_user = "postmaster@mailgun.org"
    mailgun_password = "password"
    # Recipient's email address
    recipient = "somemail@domain.com"
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = mailgun_user
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    try:
        # Establish a connection with the Mailgun server
        server = smtplib.SMTP('smtp.mailgun.org', 587)
        server.starttls()
        server.login(mailgun_user, mailgun_password)
        # Send the email
        server.send_message(msg)
        print("Email has been sent.")
    except Exception as e:
        print(f"Error while sending email: {str(e)}")
    finally:
        # Close the server connection
        server.quit()

def check_and_disable_winrm():
    try:
        while True:
            # Get the current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
            # Check the status of the WinRM service
            result = subprocess.run(["sc", "query", "winrm"], capture_output=True, text=True)
            output = result.stdout.lower()
            if "running" in output:
                print(f"[{current_time}] WinRM service is enabled. Disabling...")
                # Disable the WinRM service
                subprocess.run(["sc", "stop", "winrm"])
                print(f"[{current_time}] WinRM service has been disabled.")
               
                # Send an email notification about the enabled WinRM service
                subject = "WinRM Service is Enabled"
                message = f"The WinRM service was enabled at {current_time}."
                send_email(subject, message)
            else:
                print(f"[{current_time}] WinRM service is disabled.")
            # Wait for 30 seconds before the next check
            time.sleep(30)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by the user.")

# Run the script
check_and_disable_winrm()