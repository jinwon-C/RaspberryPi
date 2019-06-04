import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('jinwontoo1@gmail.com', 'cjw!1047517')

msg = MIMEText('test')
msg['Subject'] = '제목없음'

s.sendmail('jinwontoo1@gmail.com', 'jinwontoo1@gmail.com', msg.as_string())
s.quit()
