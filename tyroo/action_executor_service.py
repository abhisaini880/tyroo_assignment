'''
action executor service which notifies the user when rule is satisfied via Mail. 
'''
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 



def send_mail():
    '''
    send mail to user to notify against the campaign
    '''
    fromaddr = '' #Enter the Email ID of sender
    toaddr = '' # Enter the Email ID of receiver
    
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    # Email Subject
    msg['Subject'] = "Notification "
    # Email Body
    body = "Dear Sir,\n\n Kindly check your campaign, it has been paused for the day. \n\n Thanks & Regards,\nAbhishek Saini"

    msg.attach(MIMEText(body, 'plain')) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, '') # Enter password of sender Email ID inside quotes. 
    
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit() 


if __name__ == "__main__":
    pass