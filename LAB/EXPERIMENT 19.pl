student(101, anita).
student(102, rahul).
teacher(t1, mr_kumar).
teacher(t2, ms_sharma).
student_subject(101, sub01).
student_subject(102, sub02).
teacher_subject(t1, sub01).
teacher_subject(t2, sub02).
 
class_details(StudentName, TeacherName, SubjectCode) :-
    student(StudentId, StudentName),
    student_subject(StudentId, SubjectCode),
    teacher_subject(TeacherId, SubjectCode),
    teacher(TeacherId, TeacherName).
