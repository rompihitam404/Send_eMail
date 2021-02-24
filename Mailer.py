import smtplib, ssl, getpass

class Email(object):
    def __init__(self):
        self.port = 465 # ssl port
        self.smtp_server = "smtp.gmail.com"
        creds = self.login_credentials()
        self.sender_email = creds["email"]
        self.password = creds["pass"]
        # Create a secure SSL context
        self.context = ssl.create_default_context()

    def login_credentials(self):
        """ The senders login credential - password is hidden. """
        sender_email = str(input("Enter your email here : "))
        password = getpass.getpass("Enter your password here : ")
        return {"email":sender_email, "pass":password}

    def message(self):
        """ Subject and mesagge content """
        subject = str(input("Subject : "))
        message = str(input("Message : "))
        return str(f"Subject: {subject}\n"
                    f"{message}")

    def send_mail(self):
        """ Email control and forwading """
        receiver_email = str(input("Enter receivers email here : ")) # Penerima email
        message = self.message()
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, message)
                print("\nEmail succesfully sent!")
        except:
            print("\nError occurred while trying to send the email.. Please try again.")

if __name__ == "__main__":
    email = Email()
    email.send_mail()
