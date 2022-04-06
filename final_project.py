#Final Project - Basic Python AI Indonesia_Esa Putra
#Project python untuk mengirimkan pesan melalui gmail dengan python
#Menggunakan smtp GMAIL, sebelumnya email pengirim di setting untuk menerima low security.

# Imports Library smtplib sebagai modul 
import smtplib

# Input Login Email pengirim 
gmail_user = input(str("Masukkan akun gmail anda: "))
gmail_app_password = input(str("Masukkan password gmail anda: "))


# Input email penerima, subject email dan pesan email yang akan dikirimkan
sent_from = gmail_user
sent_to = input(str("Masukkan gmail penerima lalu akhiri dengan enter: "))
sent_subject = input(str("Masukkan  subjek atau judul lalu akhiri dengan enter: "))
sent_body = input(str("Masukkan pesan yang akan dikirim lalu akhiri dengan enter: "))

# Program eksekusi 
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

# =============================================================================
# Mengirim Email atau Gagal
# =============================================================================

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print("Email Berhasil Terkirim!")
except Exception as exception:
    print("Error: %s!\n\n" % exception)

#sumber : https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
# Detail Sumber: http://www.samlogic.net/articles/smtp-commands-reference.htm