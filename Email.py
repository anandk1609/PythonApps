import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Email and app-specific password
email_user = "krish@gmail.com"
email_password = "efui"


def send_email():
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = "akrish@gmail.com"
    msg['Subject'] = "First automated email"

    # Email body
    body = "Hey Anand, This is the body. \nThanking You, Ash"
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
