from courses.admin_course import AdminCourse
from courses.programming_course import ProgrammingCourse


def display_menu():
    print('''
    
    Choose one option:
        1. Create course.
        2. Choose one of the courses
        3. Display number of all courses.
        4. Display all courses
        5. Exit.
        
    ''')


def create_course():
    try:
        choice = int(input('What kind of course you want to create: for administrators (1) or programmers (2): '))
    except TypeError as error:
        print(error)
    if choice is not 1 or 2:
        raise ValueError('Your choice must be 1 or 2.')

    course_name = input('Your course name: ')
    instructor = input('Who is the course instructor: ')
    try:
        total_hours = float(input('How many hours does your course last? '))
    except TypeError as error:
        print(error)
    if choice == 1:
        tools = input('Tools required to pass the course (coma separated): ').split(', ')
        return AdminCourse(course_name=course_name, instructor=instructor, total_hours=total_hours, tools=tools)
    elif choice == 2:
        language = input('Programming language: ')
        level = input('Course level (Beginner, Intermediate, Advanced): ')
        prerequisites = input('Prerequisites to take the course: ').split(', ')
        return ProgrammingCourse(course_name=course_name, instructor=instructor, total_hours=total_hours,
                                 language=language, level=level, prerequisites=prerequisites)
