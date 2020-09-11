import random
import csv

class Student():
    """A student"""

    def __init__(self, name, gender, data_sheet, image_url):
        """Initializes a student with a name, gender, data sheet and image"""
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
    
    def get_avg_grade(self):
        """Gets average grade"""
        grades = self.data_sheet.get_grades_as_list()
        if len(grades) > 0:
            return sum(grades) / len(grades)
        else:
            return 'No grades yet'

    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.data_sheet, self.image_url)

    def __str__(self):
        return '{name} is a {gender} student. {data_sheet}. Image URL: {url}'.format(name=self.name, gender=self.gender, data_sheet=self.data_sheet, url=self.image_url)


class DataSheet():
    """A data sheet with multiple courses in particular order"""

    def __init__(self, courses):
        """Initializes a data sheet with its courses"""
        self.courses = courses

    def get_grades_as_list(self):
        """Gets grades as list"""
        lst = []
        for course in self.courses:
            lst.append(course.grade)
        return lst

    def __repr__(self):
        return 'Datasheet(%r)' % (self.courses)

    def __str__(self):
        return 'Courses attended: {courses}'.format(courses=self.courses)


class Course():
    """A course"""

    def __init__(self, name, classroom, teacher, ETCS, grade):
        """Initializes a course with a name, classroom, teacher, ETCS and optional grade if the course is taken"""
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ETCS
        self.grade = grade

    def __repr__(self):
        return 'Course(%r, %r, %r, %r, %r)' % (self.name, self.classroom, self.teacher, self.ECTS, self.grade)

    def __str__(self):
        return '{name} in {classroom} with {teacher}. ETCs for the course: {ETCS}. Grade: {grade}'.format(name=self.name, classroom=self.classroom, teacher=self.teacher, ECTS=self.ECTS, grade=self.grade)
 
# 7
def generate_students(no_students):
    """A function that can generate n number of students with random:
    name, gender, courses (from a fixed list of course names), grades, img_url

    Parameters:
    no_students: Number of random student wanted
    """
    students = []
    names = ['John', 'Jane', 'Jessica', 'Jack', 'Bob', 'Billy', 'Josephine']
    genders = ['female', 'male']
    image_urls = ['google.com', 'facebook.com']
    grades = [-3, 0, 2, 4, 7, 10, 12]
    course_names = ['Math', 'English', 'History', 'PE']
    classrooms = ['C-105', 'C-162', 'C-102', 'C-265']
    
    while len(students) < no_students:
        no_courses = random.choice(range(5)) + 1
        courses = []
        while len(courses) < no_courses:
            courses.append(Course(random.choice(course_names), 
            random.choice(classrooms), random.choice(names), ((random.choice(range(5)) + 1) * 10), random.choice(grades)))
        student = Student(random.choice(names), random.choice(genders), DataSheet(courses), random.choice(image_urls))  
        students.append(student)
    return students

# 7.A
def write_students_to_csv(students, out='students.csv'):
    """Writes a list of students to a csv file with format:
    stud_name, course_name, teacher, ects, classroom, grade, img_url

    Parameters:
    students: List of students
    """
    with open(out, 'w') as csv_file:
        fieldnames = ['stud_name', 'course_name', 'teacher', 'ects', 'classroom', 'grade', 'img_url']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            courses = student.data_sheet.courses
            for course in courses:
                writer.writerow({'stud_name': student.name, 'course_name': course.name, 'teacher': course.teacher, 'ects': course.ECTS,
                'classroom': course.classroom, 'grade': course.grade, 'img_url': student.image_url})

# students = generate_students(5)
# print(students)                          
# write_students_to_csv(students)

# 8
def read_students_from_csv(csv_file='students2.csv'):
    students = []
    with open(csv_file, 'r') as file_object:
        reader = csv.DictReader(file_object)
        student_name = ''
        courses = []
        for row in reader:
            if student_name == '':
                student_name = row['stud_name']
            if student_name == row['stud_name']:
                courses.append(Course(row['course_name'], row['classroom'], row['teacher'], row['ects'], row['grade']))
                student_name = row['stud_name']
            else:
                data_sheet = DataSheet(courses)
                students.append(Student(student_name, row['gender'], data_sheet, row['img_url']))
                courses = []
                courses.append(Course(row['course_name'], row['classroom'], row['teacher'], row['ects'], row['grade']))
                student_name = row['stud_name']
    return students

print(read_students_from_csv())

# 8.A
def print_student(students):
    for student in students:
        print('Name of student: %s. Image URL: %s. Average grade: %s' % (student.name, student.image_url, student.get_avg_grade()))

# 8.B

# 8.C


