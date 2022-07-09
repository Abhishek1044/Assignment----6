def student_data(student_id,**kwargs):
    print("Student ID : ", student_id)
    if 'student_name' in kwargs:
        print("Student name : ",kwargs['student_name'])
    if 'student_class' in kwargs:
        print("Student class : ",kwargs['student_class'])
        
student_data(student_id= '21107091',student_name = 'Anirudh Ralhan')
print()
student_data(student_id= '21107091',student_class = 'Mechanical')
print()
student_data(student_id= '21107091',student_name = 'Anirudh Ralhan',student_class = 'Mechanical')
