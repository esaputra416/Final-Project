#Final Project - Basic Python AI Indonesia_Esa Putra
#Project python untuk mengirimkan pesan melalui gmail dengan python


# Imports Library smtplib sebagai modul 
import smtplib

# Input Login Email pengirim 
email_pengirim = input(str("Masukkan akun gmail anda: "))
password_email = input(str("Masukkan password gmail anda: "))
'''
input pengirim email terdiri dari:
* email pengirim dan password email pengirim
* akun email pengirim sebelumnya harus sudah di aktifkan keamaanan bebasnya

'''


# Input email penerima, subject email dan pesan email yang akan dikirimkan
sent_from = email_pengirim
sent_to = input(str("Masukkan gmail penerima lalu akhiri dengan enter: "))
sent_subject = input(str("Masukkan  subjek atau judul lalu akhiri dengan enter: "))
sent_body = input(str("Masukkan pesan yang akan dikirim lalu akhiri dengan enter: "))

'''
input penerima pesan email terdiri dari:
* alamat email penerima
* akun email penerima sebelumnya harus sudah di aktifkan keamaanan bebasnya

'''

# Program Eksekusi 
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

#  Pemberitahuan terkiirimnya Email atau Gagal
try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(email_pengirim, password_email)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print("Email Berhasil Terkirim!")
except Exception as exception:
    print("Error: %s!\n\n" % exception)

#sumber : https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
# Detail Sumber: http://www.samlogic.net/articles/smtp-commands-reference.htmm