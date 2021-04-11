questions={"Dünyada 195 ülke vardır":"Yes",
           "En büyük gezegen Jüpiterdir":"Yes",
	   "Görelilik teorisi Albert Einstein'a aittir":"Yes",
           "Termodinamiğin ilk yasası -Enerji yokken var, varken yok edilemez. Ancak bu enerjinin biçimi değiştirilebilir-dir":"Yes",
           "Periyodik cetveli Dmitriy Mendeleyev bulmuştur?": "Yes",
           "450° C sıcaklık ile Güneş sisteminin en sıcak gezegeni Venüstür":"Yes",
           "Şu ana kadar keşfedilmiş evrendeki en büyük yıldızın ismi UY Scuti dir":"Yes",
           "Türkiye’de kadınlar ilk kez 1930 seçme 1934 seçilme hakkına sahip olmuşturç":"Yes",
           "Dünyada ilk kez 5 farklı kıtanın ülkelerinin savaştığı savaşın ismi Yedi Gün Savaşıdır":"Yes",
           "İnterentin babası olarak bilinen, sağır olan karısı için interneti icat eden, kişi Vinton Cerf tir":"Yes"}  #Dict shows all questions and answers. All true answer is shown by Yes.

comp1 = [str(comp1) for comp1 in input("Enter all answers with upper letter: ").upper().split()]   # Comp1 means competitor1. It is asked for user enter the answers with upper letter.

print("Answer list for competitor1: ", comp1) 

comp2 = [str(comp2) for comp2 in input("Enter all answers with upper letter: ").upper().split()]    # Comp2 means competitor2. It is asked for user enter the answers with upper letter.

print("Answer list for competitor2: ", comp2)


comp3 = [str(comp3) for comp3 in input("Enter all answers with upper letter: ").upper().split()]    # Comp3 means competitor1. It is asked for user enter the answers with upper letter.

print("Answer list for competitor3: ", comp3)

comp4 = [str(comp4) for comp4 in input("Enter all answers with upper letter: ").upper().split()]    # Comp4 means competitor1. It is asked for user enter the answers with upper letter.

print("Answer list for competitor4: ", comp4)

point_list=[10,10,10,10,10,10,10,10,10,10] #Shows all answer's point.

trueforcomp1 = comp1.count('YES')
print('The total true answer is: ', trueforcomp1)   #In this part, all true answers are counted for each competitors.

trueforcomp2 = comp2.count('YES')
print('The total true answer is: ', trueforcomp2)

trueforcomp3 = comp3.count('YES')
print('The total true answer is: ', trueforcomp3)

trueforcomp4 = comp4.count('YES')
print('The total true answer is: ', trueforcomp4)

true_list=[]   #list is created
true_list.extend((trueforcomp1,trueforcomp2,trueforcomp3,trueforcomp4))   #all counted true's are collected in true_list



competitors=[comp1,comp2,comp3,comp4]     #shows competitors list

j=0  
for i in range(len(true_list)):   # For all true_list elements (i=0,1,2,3), if the value is less than 5 or equal to 5, the competitor will be successful. If not, the reverse is true.
    if true_list[i]>5:
        print(competitors[j]," :You are successful")
        j+=1
    else: 
        print(competitors[j],": You are not successful")
     

