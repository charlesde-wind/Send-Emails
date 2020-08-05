import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

sender = "" # has to be your email address
receiver = "" # has to be the receiver's email address

# Create a text/plain message
content = "The receiver will see this message.\nBest regards"

msg = MIMEText(content)

# sender == the sender's email address
# receiver == the recipient's email address
msg['Subject'] = "" # Subject Header
msg['From'] = sender
msg['To'] = receiver

smtp_server_name = 'smtp.gmail.com'
port = "465"

# Send the message via our own SMTP server, but don't include the
# envelope header.

server = smtplib.SMTP(smtp_server_name, port)
server.ehlo()
server.starttls() # this is for secure reason

# Enter App Specific Password or Regular Password
server.login(sender, getpass(prompt="Email Password: "))
server.send_message(msg)
server.quit()