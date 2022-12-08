import smtplib,ssl,csv # Imports (Simple Mail Transfer Protocol -smtplib) and (Secure Socket Layers -ssl)
from email.mime.image import MIMEImage
from email.mime.text import MIMEText # Imports the Multipurpose Internet Mail Extensions(MIME) Text for handling the emails text 
from email.mime.multipart import MIMEMultipart # Imports the Multipurpose Internet Mail Extensions(MIME) Multipart, which will combine our Plain Text and HTML into a single message with two alternative renderings
# Not all email providers display HTML content by default so we will include both "Plain Text" and "HTML" versions of the email
from email.message import EmailMessage

sender_email = "massemaildev@gmail.com"
password = "gsitnjqofpldxdgk"

message = MIMEMultipart("alternative")

# Creates the Plain Text and HTML versions of the message
text="""\
Hi,
How are you?
"""

html = """\
<html>
  <body>
    <p>Hi, William!<br>
       How are you?
       Have you checked out Big Rig?
    </p>
    <image src="cid:image1"
  </body>
</html>
"""

# Turns the variables into plain/html MIMEtext objects
part1 = MIMEText(text,"plain")
part2 = MIMEText(html,"html")

# Adds HTML/Plain-text to MIMEMultipart message
# The email provider will try to render the last part first 
message.attach(part1)
message.attach(part2)

# Grabs the image in the current directory
fp = open("C:\\Users\\WilliamChalk\\Documents\\Code\MassMailer\\images\\BRT Logo.png","rb")
msgImg = MIMEImage(fp.read())
fp.close()

# Defines the image's ID as refrenced above
msgImg.add_header("Content-ID","<image1>")
message.attach(msgImg)

# Creates secure connection with server and sends email
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)

server.login(sender_email,password)

with open("C:\\Users\\WilliamChalk\\Documents\\Code\\MassMailer\\receiver.csv","r") as csvfile: # The file location of the CSV document 
    datareader = csv.reader(csvfile)
    for row in datareader:
        em = EmailMessage()
        em['From'] = sender_email
        em['To'] = row
        em['Subject'] = "Test Automation"
        em.set_content(message)
        server.send_message(em)
        print("Message Sent!")

server.close()

