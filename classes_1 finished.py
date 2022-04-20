class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_avg = 0
        
    def __str__(self):
        for grades_sub, grades_list in self.grades.items():
            if len(grades_list) != 0:
                self.grade_avg += sum(grades_list)/len(grades_list)
            else:
                print(f'No grades for {grades_sub} exist')

        text = f'Name: {self.name}\nSurname: {self.surname}\nAvg of grades: {self.grade_avg}\nFinished courses: {", ".join(self.finished_courses)}\nCourses in progress: {", ".join(self.courses_in_progress)}'
        return text
    
    def rate_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecture_courses:
                lecturer.lecture_courses[course] += [grade]
            else:
                lecturer.lecture_courses[course] = [grade]
        else:
            ( f"\nError while adding grade at \n{course.title()} for {lecturer.name} {lecturer.surname}: \nYour lecturer is class: {isinstance(lecturer, Lecturer)}, \nIs Lecturer's course: {course in lecturer.courses_attached} \nIs student's course : {course in self.courses_in_progress}. \n") 

    def __lt__(self, other):
      if isinstance(other, Student):
        return self.grade_avg < other.grade_avg
      else:
        print('Error')

    def __gt__(self, other):
      if isinstance(other, Student):
        return self.grade_avg > other.grade_avg
      else:
        print('Error') 

    def __eq__(self, other):
      if isinstance(other, Student):
        return self.grade_avg == other.grade_avg
      else:
        print('Error')

    def __ne__(self, other):
      if isinstance(other, Student):
        return self.grade_avg != other.grade_avg
      else:
        print('Error') 

    def __le__(self, other):
      if isinstance(other, Student):
        return self.grade_avg <= other.grade_avg
      else:
        print('Error')

    def __ge__(self, other):
      if isinstance(other, Student):
        return self.grade_avg >= other.grade_avg
      else:
        print('Error') 
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
        self.lecture_courses = {}
        self.grade_avg = 0

    def __str__(self):
        for grades_sub, grades_list in self.lecture_courses.items():
            if len(grades_list) != 0:
                self.grade_avg += sum(grades_list)/len(grades_list)
            else:
                print(f'No grades for {grades_sub} exist')

        text = f'Name: {self.name}\nSurname: {self.surname}\nAvg of grades: {self.grade_avg}\n'
        return text
    
    def __lt__(self, other):
      if isinstance(other, Lecturer):
        return self.grade_avg < other.grade_avg
      else:
        print('Error')

    def __gt__(self, other):
      if isinstance(other, Lecturer):
        return self.grade_avg > other.grade_avg
      else:
        print('Error') 

    def __eq__(self, other):
      if isinstance(other, Lecturer):
        return self.grade_avg == other.grade_avg
      else:
        print('Error')

    def __ne__(self, other):
      if isinstance(other, Lecturer):
        return self.grade_avg != other.grade_avg
      else:
        print('Error') 

    def __le__(self, other):
      if isinstance(other, Lecturer):
        return self.grade_avg <= other.grade_avg
      else:
        print('Error')

    def __ge__(self, other):
      if isinstance(other, Lecturer):
        return self.grade_avg >= other.grade_avg
      else:
        print('Error') 
    
class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
    
    def __str__(self):
        text = f'Name: {self.name}\nSurname: {self.surname}\n'
        return text

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print( f"\nError while adding grade at {course.title()} for {student.name} {student.surname}: \nYout student is class: {isinstance(student, Student)}, \nIs Reviewer's course: {course in self.courses_attached} \nIs student's course : {course in student.courses_in_progress}. \n" )
    

albert_reviewer = Reviewer('Альберт', 'Энштейн', ['Physics', 'Math'])
mike_student = Student('Mike', "Tayson", 'Atack Helicopter')
nate_student = Student('Nate', "Smith", 'Male')
vitaliy_student = Student('Vitaliy', "Kacheryzkin", 'Male')
tesla_lecturer = Lecturer('Nicola', 'Tesla', ['Math', 'Informatics'])
marks_lecturer = Lecturer('Carl', 'Marks', ['Math'])
jason_lecturer = Lecturer('Jason', 'Statham', ['PE', 'Security'])

mike_student.courses_in_progress += ['Math', 'Informatics', 'Physics', 'Biology']
mike_student.finished_courses += ['Kindergarden']
nate_student.courses_in_progress += ['Math', 'Physics', 'Biology', 'Security', 'PE']
nate_student.finished_courses += ['Informatics']
nate_student.grades = {"Math": [1,2,3], "Physics": [4,56,6]}
vitaliy_student.courses_in_progress += ['Literature', 'English Language']
vitaliy_student.finished_courses += ['Box']
vitaliy_student.grades = {"Literature": [9, 10, 10]}

albert_reviewer.rate_hw(mike_student, 'Math', 36)
albert_reviewer.rate_hw(mike_student, 'Math', 12)

mike_student.rate_lector(tesla_lecturer, 'Math', 55 )
mike_student.rate_lector(tesla_lecturer, 'Informatics', 10 )
nate_student.rate_lector(jason_lecturer, 'PE', 10 )
nate_student.rate_lector(jason_lecturer, 'Security', -100 )
mike_student.rate_lector(marks_lecturer, 'Math', 25 )
nate_student.rate_lector(marks_lecturer, 'Math', 13 )


# новый список из [lect1.avg_grade, lect2.avg_grade].sort()  f'[0] is greater than [1]'

# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса)
all_studs = [mike_student, nate_student, vitaliy_student]

def avg_grade_allstuds(all_students, course):
    all_grades = []
    for student in all_students:
        if course in student.grades:
            all_grades += student.grades[course]
        else:
            print(f'{student.name} {student.surname} doesn\'t have {course} ')
    if len(all_grades) != 0:
        print(f'Student\'s average for {course} is {sum(all_grades)/len(all_grades)}')
    else:
        print('No grades!')


avg_grade_allstuds(all_studs,"Math")

all_lecturers = [jason_lecturer, tesla_lecturer, marks_lecturer]

def avg_grade_alllecturers(all_lecturers, course):
    all_grades = []
    for lecturer in all_lecturers:
        if course in lecturer.lecture_courses:
            all_grades += lecturer.lecture_courses[course]
        else:
            print(f'{lecturer.name} {lecturer.surname} doesn\'t have {course} ')
    if len(all_grades) != 0:
        print(f'Lecturer\'s average for {course} is {sum(all_grades)/len(all_grades)}')
    else:
        print('No grades!')

avg_grade_alllecturers(all_lecturers,"Math")   



