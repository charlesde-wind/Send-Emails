import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

sender = "" # doesn't have to be your email address it can be My Name <myname@aol.com>
receiver = "" # has to be the receiver's email address

msg = MIMEMultipart('related')
msg['Subject'] = "" # subject of email
msg['From'] = sender
msg['To'] = receiver

# Basic HTML
html = """\
<html>
  <head></head>
    <body>
      <h1>EASY HTML</h1>
      <img src="cid:image1" alt="Logo" style="width:250px;height:50px;"><br>
       <p><h4 style="font-size:15px;">Some Text.</h4></p>           
    </body>
</html>
"""
# Record the MIME types of text/html.
part2 = MIMEText(html, 'html')

# Attach parts into message container.
msg.attach(part2)

# This example assumes the image is in the current directory
fp = open('Supplies.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

# Send the message via SMTP server.
server = "smtp.gmail.com"
# server = "smtp-mail.outlook.com"
# server = "smtp.mail.yahoo.com"
# search smtp python followed by your email provider
mailsrv = smtplib.SMTP(server)

# Essentially Says Hello To Server
mailsrv.ehlo()

mailsrv.starttls()

my_email = ""
# create an app specific password so that this app doesn't have access to your real password
my_password = ""


mailsrv.login(my_email, my_password)
mailsrv.sendmail(sender, receiver, msg.as_string())
mailsrv.quit()