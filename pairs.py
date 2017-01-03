students_absent = []
students_registered = ["Abigail","Yvonne", "Alice","Jessica","Gulinazi/Naz","Molly","Maria", "SarahH","Chadapon/Mod ","Eileen", "Yenny","Angela","Elizaveta/Leeza","Shelley","Rebecca/Bekki","MaryM", "Catherine/Cat","Brianne","Natalie","Rachel","Tien/Mimi","Kyoto","MaryW", "Yu","Mali"]
students_registered.sort()
print "Students Registered in this Class",students_registered
print

number_absent = int(raw_input("How many are absent tonight? "))

while number_absent > 0:

    absentee =(raw_input("Who is absent tonight? "))
    if absentee in students_registered:       
         students_absent.append(absentee)
         number_absent -= 1
    else:
        print "That person isn't registered in the class. Try again. "

students_previously_paired = [("Gulinazi/Naz","Yu"),("Alice","Rachel"),("Jessica","Mali"),("Catherine/Cat", "Yenny"),("Elizaveta/Leeza","Yvonne"), ( "Kyoto","Maria"), ("Chadapon/Mod ","Tien/Mimi"),("Rebecca/Bekki","SarahH"),("Eileen","Shelley"),("MaryM","MaryW"),("Abigail","Natalie"),("Brianne","Molly")]
print students_previously_paired



def present(students_registered,students_absent):
    """This function is used to eliminate the students who are absent from 
    the list of students to pair in the class for lab time
    """


    while len(students_absent) > 0:
        students_registered.remove(students_absent[0])
        students_absent = students_absent[1:]

    students = students_registered
    print "Students here tonight", students
    print
    return students


def pair(students):
    """ This function make a list of all the pairs that are possible in the class"""


    student_set = set()
    for i in range(len(students)-1):
        for j in range(i+1,len(students)):           
            student_set.add((students[i],students[j]))

    print "Student Set",student_set
    print
    return student_set



def class_list(student_set,students,students_previously_paired):
    """ This function prints a class pairing list, making sure all students
    get a different partner each lab. The second list printed is a list of 
    students who couldn't be paired...may be they are the two left and they've
    been partners before or may be there are an uneven number of students
    in lab
    """


    class_dict = {}
    number_pos = len(students) - 1
    class_pairs = []

    while len(students_previously_paired) > 0:
        print students_previously_paired[0]
        
        if students_previously_paired[0] in student_set:
            student_set.remove(students_previously_paired[0])
        students_previously_paired = students_previously_paired[1:]
        



    while len(students) > 1 and student_set:
        first = student_set.pop()

        if first[0] in students and first[1] in students: 
            students.remove(first[0])
            students.remove(first[1])
            class_pairs.append(first)

    print class_pairs, students



if __name__ == "__main__":
    students = present(students_registered,students_absent)
    student_set = pair(students)
    class_list(student_set,students,students_previously_paired)








