d={"name":"John","pass":"12345"}
n=d["name"]
p=d["pass"]
username = input('Enter username: ')
password = input('Enter password: ')

if (username!= n and password==p):
    print("Kullanıcı adınız hatalı")
elif (username==n and password!= p):
    print("Password hatalı")
elif (username!=n and password!= p):
    print("Username ve password hatalıdır.")
else:
    print("Tebrikler, Başarıyla giriş yaptınız")
