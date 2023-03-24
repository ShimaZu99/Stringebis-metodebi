#name = "nika"

#print(len(name))              #len  არის სიგრძე

#my_sentence = """გოა აკადემიაში განათლების        
#მიღება კარგია"""    #სამი """" გამოიყენება გრძელიი სთრინგების გამოსაყენებლად

#print(my_sentence)

#knows_programming = True

#if 10>5:
#    print("hello")
          #Tab ის საშუალებით მოვახდინოთ ინდენტაცია (indentation)

#full_name = ("Nika Khubua")
#print(len(full_name))

#ყველა სთრინგი შეგვიძლია მივიჩნიოთ სიად
#print(full_name[7])

#print("k" in full_name)         #ამ მეთოდით შეგვიძლია მოვძებნოთ ტექსტში რაიმე ასო ბგერა
#print("k" not in full_name)      #"K" არ არის ამ სიტყვებში მცდარი დებულებაა 

full_name = ("Nika Khubua")
# print(full_name[3:9])            #აქ შეგვიძლია გამოვიტანოთ ყოველი 3 დან 9 ის ჩათვლით ასო
# print(full_name[2:9:3])          #აქ შეგვიძლია გამოვიტანოთ ყოველი მეორე სთრინგი
# print(full_name[3:])             #აქ შეგვიძლია გამოვიტანოთ 3 ასოდან ბოლომდე სთრინგი
# print(full_name[5:])             #აქ შეგვიძლია გამოვიტანოთ პირველი ასოდან მესამე ასომდე სთრინგი

#print(full_name[-1:-5:-1])               #NEGATIVE

#string -ებს აქვთ ორი მეთოდი
# 1) სტრინგ. upper()
# 2) len(string)

#print(full_name.upper())          #upper ზრდის სტრინგის ასოებს 

name2 = ("nika khubua")
#print(name2.lower())              #lower აპატარავებს სტრინგის ასოებს

#print(name2.strip())               #Strip ჩამოჭრა ხდება სთრინგში SPACE ბის

#print(name2.replace(" ", "#"))      #replace ამ ფუნქციით შეგვიძლია ჩვენ SPACE ბის # ებად ჩანაცვლება

print(name2.replace("a", "#"))      