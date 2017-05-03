import sys
import time
import smtplib
from time import sleep
from random import randint
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Function should be called as follows
# main.py recipient@email.com login@email.com loginpw subj body
# Example
# python main.py friend@gmail.com myemail@gmail.com mypassword emailsubject emailbody



timestall = randint(0, 14400) #14400 (random time between call start and 4 hours)
sleep(timestall)


fromaddr = sys.argv[2]
toaddr = sys.argv[1]
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = time.strftime("%m/%d/%y") # sys.argv[4] (Swapping out argv[4] for the current time for the Nintendo Switch giveaway)

body = "Zachary Mueller"# sys.argv[5] (Swapping out argv[5] for my name for the Nintendo Switch giveaway)
msg.attach(MIMEText(body, 'plain'))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sys.argv[2], sys.argv[3])
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

