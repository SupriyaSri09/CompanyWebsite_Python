import smtplib,ssl
import os
import dotenv

dotenv.load_dotenv()


def send_email(message,receiver_email):
    sender = "supriya.prakash.ldn@gmail.com"
    print(f"**************************************")
    password = os.getenv('PASSWORD')
    print(f"**************************************{password}")
    host = "smtp.gmail.com"
    port = 456
    context = ssl.create_default_context()

    connection = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    connection.ehlo()
    connection.login(user=sender, password=password)
    connection.sendmail(from_addr=sender, to_addrs=receiver_email, msg=message)
    connection.close()






