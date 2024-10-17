import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP settings (example for Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "your_email@gmail.com"
smtp_pass = "your_password"

def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, to_email, msg.as_string())
        print(f"Email sent to {to_email}")

# Example: Send personalized email
with open("contacts.txt", "r") as file:
    for line in file.readlines():
        name, email = line.strip().split(',')
        subject = "Hello, " + name
        body = f"Dear {name},\n\nThis is a personalized message just for you!\nBest regards."
        send_email(email, subject, body)
