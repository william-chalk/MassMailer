import smtplib,ssl # Imports (Simple Mail Transfer Protocol -smtplib) and (Secure Socket Layers -ssl)
from email.mime.text import MIMEText # Imports the Multipurpose Internet Mail Extensions(MIME) Text for handling the emails text 
from email.mime.multipart import MIMEMultipart # Imports the Multipurpose Internet Mail Extensions(MIME) Multipart, which will combine our Plain Text and HTML into a single message with two alternative renderings
# Not all email providers display HTML content by default so we will include both "Plain Text" and "HTML" versions of the email

sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "this is a test"
message["From"] = sender_email
message["To"] = receiver_email

# Creates the Plain Text and HTML versions of the message
text="""\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turns the variables into plain/html MIMEtext objects
part1 = MIMEText(text,"plain")
part2 = MIMEText(html,"html")

# Adds HTML/Plain-text to MIMEMultipart message
# The email provider will try to render the last part first 

