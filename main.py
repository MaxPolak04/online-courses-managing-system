from courses.programming_course import ProgrammingCourse
from courses.admin_course import AdminCourse


# dodanie docstringów - dokumentacji do klas i metod
# uzupełnić wywołania błędów
if __name__ == '__main__':
    admin_course = AdminCourse('Linux - Command Prompt for Beginners', 'Jan Kowalski', 20, ['computer/laptop',])
    admin_course.get_details()
    admin_course.update_course(total_hours=30)
    admin_course.get_details()
    print(admin_course.total_courses)
    print(admin_course.all_courses)
    print(admin_course)