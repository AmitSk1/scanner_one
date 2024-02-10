import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body, recipient_email, sender_email, sender_password):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Setup the SMTP server connection
    server = smtplib.SMTP('smtp.gmail.com',
                          587)  # Example using Gmail SMTP server
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(msg)
    server.quit()
