students={"Tuğba":["Aslan",68,70,80], 
          "Ceren":["Akar",75,80,90],
          "Fatoş":["Yılmaz",78,65,75],
          "Yıldız":["Kılıç",65,80,95],
          "Zeynep":["Alşan",45,75,85]}  #Created student information with dictionary
Tuğba_midterm=students["Tuğba"][1]
Tuğba_midterm                            #Grades are taken by indexing separately for each student

Tuğba_project=students["Tuğba"][2]
Tuğba_project

Tuğba_final=students["Tuğba"][3]
Tuğba_final

per1=0.3
per2=0.3
per3=0.4
Tuğba_passgrade=(Tuğba_midterm*per1)+(Tuğba_project*per2)+(Tuğba_project*per3)  #For all students, passgrade are calculated via formula
Tuğba_passgrade

Ceren_midterm=students["Ceren"][1]
Ceren_midterm

Ceren_project=students["Ceren"][2]
Ceren_project

Ceren_final=students["Ceren"][3]
Ceren_final

Ceren_passgrade=(Ceren_midterm*per1)+(Ceren_project*per2)+(Ceren_project*per3)
Ceren_passgrade

Fatoş_midterm=students["Fatoş"][1]
Fatoş_midterm


Fatoş_project=students["Fatoş"][2]
Fatoş_project

Fatoş_final=students["Fatoş"][3]
Fatoş_final

Fatoş_passgrade=(Fatoş_midterm*per1)+(Fatoş_project*per2)+(Fatoş_project*per3)
Fatoş_passgrade

Yıldız_midterm=students["Yıldız"][1]
Yıldız_midterm

Yıldız_project=students["Yıldız"][2]
Yıldız_project
Yıldız_final=students["Yıldız"][3]
Yıldız_final

Yıldız_passgrade=(Yıldız_midterm*per1)+(Yıldız_project*per2)+(Yıldız_project*per3)
Yıldız_passgrade

Zeynep_midterm=students["Zeynep"][1]
Zeynep_midterm

Zeynep_project=students["Zeynep"][2]
Zeynep_project

Zeynep_final=students["Zeynep"][3]
Zeynep_final

Zeynep_passgrade=(Zeynep_midterm*per1)+(Zeynep_project*per2)+(Zeynep_project*per3)
Zeynep_passgrade

studentsgrade_list=[]   # list are created
studentsgrade_list.extend((Tuğba_passgrade,Ceren_passgrade,Fatoş_passgrade,Yıldız_passgrade,Zeynep_passgrade)) # grades are added to list
studentsgrade_list

students.keys() #keys are selected for student names as a dict


list(students.keys()) #dict is turned to list
names=list(students.keys()) #list assigned to a variable
names

info=input("Please enter your name:") #ask for user name

for i in range(len(names)):  # According to user input, grades are shown.
    if info==names[i]:
       print('Your passing grade is: ', studentsgrade_list[i])
       
studentsgrade_list.sort(reverse=True); # grades have ascending order.
print(studentsgrade_list)
