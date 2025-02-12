from courses.programming_course import ProgrammingCourse
from courses.admin_course import AdminCourse


if __name__ == '__main__':
    programming_course = ProgrammingCourse('Scripting in Python', 'John Smith', 10,
                        'Python', 'Intermediate', ['Python basics', 'Bash scripting basics'])

    admin_course = AdminCourse('Linux - Command Prompt for Beginners', 'Jan Kowalski',
                               20, ['computer/laptop',])


    ProgrammingCourse.display_number_of_total_courses()
    ProgrammingCourse.delete_course('Scripting in Python')
    ProgrammingCourse.display_number_of_total_courses()

    print(programming_course)
    ProgrammingCourse.display_all_courses()





