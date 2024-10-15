import smtplib
from email.mime.text import MIMEText

from settings import EMAIL_SENDER, EMAIL_PASSWORD

class E_mail():

    def __send_email(subject : str, body : str, recipients : str):

        msg = MIMEText(body)

        msg['Subject'] = subject
        msg['From'] = EMAIL_SENDER
        msg['To'] = ', '.join(recipients)

        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp_server.sendmail(EMAIL_SENDER, recipients, msg.as_string())

        smtp_server.quit()

        return

    def message(to : str = "test@test.com", subject : str = "test", body : str = "sample"):

        recipients = [to]

        try:
            E_mail.__send_email(subject = subject, body = body, recipients = recipients)
            return True
        except:
            print("An error occured while sending the mail")
            return False