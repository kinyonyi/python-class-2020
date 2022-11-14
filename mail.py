import email, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "kinyonyidavid@gmail.com"
receiver_email = "kinyonyidavid@gmail.com"

password = input("Type your password and press enter: ")
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email
message["Bcc"] = receiver_email

text = """\
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
       i am the new message from my self.
    </p>
  </body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
#message.attach(part1)
message.attach(part2)
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, 
        [receiver_email,'davidkinyonyi@gmail.com'],
        message.as_string()
        )
    

#adding attachments
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
message = MIMEMultipart()
subject = "hello attachment"
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

"""
# Add body to email
body = "this is my body of thye text"
message.attach(MIMEText(body, "plain"))

filename = "document.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    
"""