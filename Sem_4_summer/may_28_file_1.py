import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "sender@xyz"
subject = "email from Python"
body = "I am sending this mail without opening Mail"

message = f"""From: {sender}
To: {receiver}
Sub: {subject}\n
Body: {body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("logged in")
    server.sendmail(sender, receiver, message)
    print("mail sent")

except smtplib.SMTPAuthenticationError:
    print("login failed")
except smtplib.SMTPServerDisconnected:
    print("Connection failed")