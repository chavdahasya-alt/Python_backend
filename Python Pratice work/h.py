sname=(input("Enter student Name : "))
rno=(intput(" Enter roll no  : "))
s1=(intput("Enter marks of subject 1 : "))
s2=(intput("Enter marks of subject 2 : "))

s3=(intput("Enter marks of subject 3 : "))
total=s1+s2+s3
per=total/3

print("Student name :",sname)
print("Roll no : ",rno)
print("Total :",total)
print("Percentage : ",per)


if per>=70:
    print("distinction")
elif per>=60:
    print("first class")
elif per>=50:
    print("second class")
elif per>=40:
    print("pass class")
else:
    print("fail")
    


