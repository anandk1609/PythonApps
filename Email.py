import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Email and app-specific password
email_user = "krishnananand73@gmail.com"
email_password = "efui ksfm cdpj nuly"


def send_email():
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = "akrishnan1609@gmail.com"
    msg['Subject'] = "First automated email"

    # Email body
    body = "Hey Anand, I think you are falling in love with Saipriya. Take care of her. Make sure she is never sad. \nThanking You, Anand"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a connection to the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(email_user, email_password)
        text = msg.as_string()

        # Send email
        server.sendmail(email_user, "akrishnan1609@gmail.com", text)

        # Disconnect from the server
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    send_email()
