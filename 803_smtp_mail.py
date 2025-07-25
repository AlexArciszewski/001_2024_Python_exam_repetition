import smtplib #biblioteka smtp



my_email = "aassss@gmail.com"
password = "aaaa aaaa aaaa aaaa" 
#https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4NQPL7RFt6qiE91JZLtHNR1a0e3MCxngezGAuip_pq0g3fPmVDf_V_yM4YaYTSpQ735q5F6J0x2YhypEo0FuSEOc6YGZXPzqxrO9g8jnUCZPNovhP4 w gamil tu tworzy się hasło 
connection = smtplib.SMTP("smtp.gmail.com") #obiekt gmail provider
connection.starttls()  #transport layer security jesli ktos przechwyci maila to będie on dzięki tej linii kodu zakodowany
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="ssssssssssssss@yahoo.com",
    msg="Subject:Hello\n\n Say hello to my little friend."
)
connection.close()


# bez connection.close()
with smtplib.SMTP("smtp.gmail.com") as connection:
    my_email = "aaaaaaaaa@gmail.com"
    password = "aaaa aaaa aaaa aaaa"
    connection = smtplib.SMTP("smtp.gmail.com") #obiekt gmail provider
    connection.starttls()  #transport layer security jesli ktos przechwyci maila to będie on dzięki tej linii kodu zakodowany
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="aaaaaaaaaaaaai@yahoo.com",
        msg="Subject:Hello\n\n Say hello to my little friend."
    )