#Question 1
i=[0,1,2,3,4,5] #list oluşturdum
firsthalf= i[:3] #listeyi ilk yarısından ayırıp ayrı liste yaptım
secondhalf= i[3:] #listeyi ikinci yarısından ayırıp    "      "
secondhalf.extend(firsthalf) #ikinci yarısına ilk yarısını katarak bir bütün liste oluşturdum.
print(secondhalf)


#Question 2
num = int(input("Enter a single digit integer number: ")) #kullanıcıdan tek basamaklı bir sayı girmesini istedim.
number=0 #0'dan başlaması için değer atadım.
while number<= num: #döngü 0 dan başlayıp girilen sayıya kadar(oda dahil) yazsın istiyorum.
     if(number %2 ==0): #2 ile tam bölünebiliyorsa bana çift sayıları verir.
         print("{0}".format(number)) # 0 dan itibaren if koşulunu sağlayan tüm sayıların yazdırılmasını sağlar.
     number=number+1 #her seferinde sayıya bir ekler ve while koşuluna kadar arttırır.
