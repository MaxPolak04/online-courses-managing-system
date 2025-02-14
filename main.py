from courses.course import Course
from courses.programming_course import ProgrammingCourse
from courses.admin_course import AdminCourse
from utils import display_menu, create_course
from sys import exit


if __name__ == '__main__':
# wyświetlanie liczby wszystkich kursów (display_number_of_total_courses)
# wyświetlanie wszystkich kursów (display_all_courses)

# tworzenie podanych obiektów
# wyświetlanie ocen (display_ratings)
# dodanie oceny (add_rating)
# wyswietlamie informacji na temat kursu (get_details)
# aktualizacja kursu (update_course)
# usuniecie kursu (delete_course)
#       wyświetlanie projektów w kursie (display_projects)
#       dodawanie projektów do kursu (add_project)
    courses = []

    while True:
        display_menu()
        try:
            option = int(input('Your choice: '))
        except TypeError as error:
            print(error)
        if option not in range(1, 6):
            raise ValueError('Your option must be between 1 and 5.')

        if option == 1:
            course = create_course()
            courses.append(course)
        elif option == 2:
            Course.display_all_courses()
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            exit()
