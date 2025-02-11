from abc import ABC, abstractmethod
from statistics import mean


class Course(ABC):
    total_courses = 0
    all_courses = []

    def __init__(self, course_name, instructor, total_hours):
        self.course_name = course_name
        self.instructor = instructor
        self.total_hours = total_hours
        self.ratings = []
        Course.total_courses += 1
        Course.all_courses.append(self)

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Wrong type for name')
        if name in self.all_courses:
            raise DuplicateCourseError('')
        self._course_name = name

    @property
    def instructor(self):
        return self._instructor

    @instructor.setter
    def instructor(self, full_name: str):
        if not isinstance(full_name, str):
            raise TypeError('')
        self._instructor = full_name

    @property
    def total_hours(self):
        return self._total_hours

    @total_hours.setter
    def total_hours(self, value: (int, float)):
        if not isinstance(value, (int, float)):
            raise TypeError('')
        self._total_hours = value

    def display_ratings(self):
        return mean(self.ratings)

    def add_rating(self, rating: (int, float)):
        if not isinstance(rating, (int, float)):
            raise TypeError('')
        if rating < 0.5 or rating > 5:
            raise InvalidGradeError('')
        self.ratings.append(rating)

    @abstractmethod
    def get_details(self):
        pass

    @classmethod
    def display_number_of_total_courses(cls):
        print(f'Number of total courses: {cls.total_courses}')


class DuplicateCourseError(Exception):
    pass

class InvalidGradeError(Exception):
    pass
