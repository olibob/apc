import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send(login, password, sender, receiver, msg):
  """Sends email securely through gmail""" 
  
  SSLPort = 465

  # Create a secure SSL context
  context = ssl.create_default_context()

  # Making sure to close socket
  with smtplib.SMTP_SSL('smtp.gmail.com', SSLPort, context=context) as server:
    server.login(login, password)
    server.sendmail(sender, receiver, msg.as_string())

def create_multipart_message(sender, receiver, subject, item, price, threshold, url):
  """Returns a multipart message ready to be emailed"""

  message = MIMEMultipart("alternative")
  message['Subject'] = subject
  message['From'] = sender
  message['To'] = receiver

  # Create text
  text = """\
  Hi,
  
  The item price has changed."""

  html = f"""\
  <html>
    <body>
      <p>Hi,</p>
      <p>
        The price has of <a href="{url}">{item}</a> has dropped to {price} € (Threshold price was set to {threshold}).
      </p>
      <p>
        --<br>
        APC
      </p>
    </body>
  </html>"""
  
  # Turn this into plain/html MIMEText objects
  part1 = MIMEText(text, 'plain')
  part2 = MIMEText(html, 'html')

  # Add HTML/plain-text parts to MIMEMultipart message
  # The email client will try to render the last part first
  message.attach(part1)
  message.attach(part2)

  return message