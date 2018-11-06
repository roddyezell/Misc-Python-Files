# Test scores

import names
import random

def testscores():
    students = [names.get_first_name() for x in range(1,1001,1)]
    grades = [random.randrange(50,100,1) for x in range(len(students))]
    combined = dict(zip(students,grades))
    class_average = (sum(grades)/len(grades))
    #print(combined)
    #print(class_average)
    return(students, class_average)

get_grades = 'y'



while get_grades == 'y':
    get_grades = input("Get grades? (Y/N): ")
    students, average = testscores()
    unique = (len(set(students))/len(students))
    print('\n'.join(students))
    print("\nPercentage of unique student names: {}".format(unique))
    print("The class average is: {}\n".format(average))
