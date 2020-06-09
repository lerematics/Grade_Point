sum_unit = 0
sum_points = 0
Name = input(">>> Enter your name: ")
Matric_number = input(">>> Enter your matric number: ")

while True:
    try:
        Courses_offered = int(input(">>> Enter the number of courses offered: "))
        break
    except:
        print('Courses offered must be an integer ...')

for num in range(Courses_offered):
    Course_code = input(">>> Enter the course code for course" + str(1 + num) + ": ")
       
    while True:
        try:
            Course_unit = int(input(">>> Enter " + Course_code + " unit(s): "))
            break
        except:
            print('..must be an integer ...')
            
    while True:
        try:
            Points_scored = int(input(">>> Enter the score attained in " + Course_code + ": "))
            break
        except:
            print('..must be an integer ...')
    
    sum_unit += Course_unit

    if (Points_scored >= 70) and (Points_scored <= 100):
        Cred = 5
    elif (Points_scored >= 60) and (Points_scored <= 69):
        Cred = 4
    elif (Points_scored >= 50) and (Points_scored <= 59):
        Cred = 3
    elif (Points_scored >= 45 and Points_scored <= 49):
        Cred = 2
    else:
        Cred = 0
    
    points = Cred * Course_unit

    sum_points += points


Gp = sum_points / sum_unit
if Gp < 1.5:
    print("Dear {}, I really don't know your purpose here in school. You better go out there and look for something okay to do.".format(Name))
elif (Gp >= 1.5) and (Gp < 2.5):
    print("Dear {}, your CGPA is {:.2f} and you are currently a third class student.".format(Name, Gp))
elif (Gp >= 2.5) and (Gp < 3.5):
    print("Dear {}, your CGPA is {:.2f} and you are currently a second class lower student.".format(Name, Gp))
elif (Gp >= 3.5) and (Gp < 4.5):
    print("Dear {}, your CGPA is {:.2f} and you are currently a second class upper student.".format(Name, Gp))
elif (Gp >= 4.5) and (Gp <= 5.0):
    print("Dear {}, your CGPA is {:.2f} and you are currently a first class student.".format(Name, Gp))

print("Thanks!!!")