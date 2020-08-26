studentscore= float(input("Enter Your Score: "))
if 34 < studentscore <= 60:
    print ("You Scored E Grade.");
elif 60 < studentscore <= 70:
    print ("You Scored D Grade.");
elif 70 < studentscore <= 80:
    print ("Congratulations You Scored C Grade.");
elif 80 < studentscore <= 90:
    print ("Congratulations You Scored B Grade.");
elif 90 < studentscore <=100:
    print ("Congratulations You Scored A Grade.");
else:
    print ("Sorry, You Failed!");
