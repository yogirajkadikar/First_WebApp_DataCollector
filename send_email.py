from email.mime.text import MIMEText
import smtplib

def send_email(email,height, average_height, count):
    from_email = "yogiraj.u.k@gmail.com"
    from_password = "211yogikadikar"
    to_email = email

    subject = "Height Data"
    message = "Hey there, your height is <strong>%s</strong> cm. <br> The average height is <strong>%s</strong>, that is calculated from the <strong>%s</strong> number of people who logged in their height.<br> Thanks! " % (height,average_height,count)


    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)