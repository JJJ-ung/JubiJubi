import smtplib
from email.message import EmailMessage

class Mail():
    sender = '2021JubiJubi@gmail.com'
    password = 'qwer1324!@#$'
    subject = '주비주비 거래 정보'

    msg = EmailMessage()

    msg['From'] = sender
    msg['Subject'] = subject

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(sender, password)

    def SendEmail(target):
        Mail.msg['To'] = target

        # 즐찾에 있는 리스트 다 보내기
        # 코인 티커 이름 영문이름
        # 주식 코드 이름
        # 고가/저가/현재가/최근 5일 종가/거래량

        content = ""

        Mail.msg.set_content(content)

        Mail.smtp.send_message(Mail.msg)
