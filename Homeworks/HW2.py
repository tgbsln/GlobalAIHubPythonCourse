d={"name":"John","pass":"12345"} #dictionary oluşturuldu
n=d["name"] #key element ile isim değişken bir değere atandı.
p=d["pass"] # "      "   şifre   "    "      "      "
username = input('Enter username: ') #kullanıcıdan ismini girmesi istenir.
password = input('Enter password: ') #   "         şifresini  "      "

if (username!= n and password==p):     #eğer kullanıcı adı hatalı ve şifre doğruysa alttaki print edilir.
    print("Kullanıcı adınız hatalı")   
elif (username==n and password!= p):   #eğer kullanıcı adı doğru ve şifre yanlışsa alttaki print edilir.
    print("Password hatalı")
elif (username!=n and password!= p):   #eğer kullanıcı adı ve şifre hatalı ise       "        "    " 
    print("Username ve password hatalıdır.")
else:                                   #ikiside doğruysa başarılı giriş yapılır.
    print("Tebrikler, Başarıyla giriş yaptınız")
