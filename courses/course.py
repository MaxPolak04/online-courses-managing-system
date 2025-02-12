from abc import ABC, abstractmethod
from statistics import mean


class Course(ABC):
    """
    An abstract base class for courses.

    Attributes:
    -----------
    course_name : str
        Course name.
    instructor : str
        Course instructor
    total_hours : int
        Total hours of the Course
    ratings : list
        Ratings of the Course
    total_courses : int
        Total number of Courses
    all_courses : list
        List of all Courses
    """
    total_courses = 0
    all_courses = []

    def __init__(self, course_name, instructor, total_hours):
        """
        Initializes a new instance of the Course class.

        :param course_name: str
        :param instructor: str
        :param total_hours: int
        """
        self.course_name = course_name
        self.instructor = instructor
        self.total_hours = total_hours
        self.ratings = []
        Course.total_courses += 1
        Course.all_courses.append(self)

    def __str__(self):
        return f'"{self.course_name}" by {self.instructor} (Rating: {self.display_ratings()})'

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.course_name}")'

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Wrong data type, name must be str type.')
        if name in self.all_courses:
            raise DuplicateCourseError('There is already a course with this name.')
        self._course_name = name

    @property
    def instructor(self):
        return self._instructor

    @instructor.setter
    def instructor(self, full_name: str):
        if not isinstance(full_name, str):
            raise TypeError('Wrong data type, full_name must be str type.')
        self._instructor = full_name

    @property
    def total_hours(self):
        return self._total_hours

    @total_hours.setter
    def total_hours(self, value: (int, float)):
        if not isinstance(value, (int, float)):
            raise TypeError('Wrong data type, value must be int or float type.')
        self._total_hours = value

    def display_ratings(self):
        """Returns the arithmetic average of all grades"""
        return round(mean(self.ratings), 1) if len(self.ratings) > 0 else 0


    def add_rating(self, rating: (int, float)):
        """Adds a grade to the course"""
        if not isinstance(rating, (int, float)):
            raise TypeError('Wrong data type, rating must be int or float type.')
        if rating < 0.5 or rating > 5:
            raise InvalidGradeError('Rating must be > 0 and <= 5.')
        self.ratings.append(round(rating, 1))

    @abstractmethod
    def get_details(self):
        pass

    def update_course(self, course_name=None, instructor=None, total_hours=None):
        """Updates a course parameters"""
        if course_name:
            self.course_name = course_name
        if instructor:
            self.instructor = instructor
        if total_hours:
            self.total_hours = total_hours


    @classmethod
    def delete_course(cls, course_name: str):
        if not isinstance(course_name, str):
            raise TypeError('Wrong data type, course_name must be str type.')
        for course in cls.all_courses:
            if course.course_name == course_name:
                cls.all_courses.remove(course)
                cls.total_courses -= 1
                del course
                return f'Course "{course_name}" has been removed.'
        return f'Course "{course_name}" not found.'

    @classmethod
    def display_number_of_total_courses(cls):
        print(f'Number of total courses: {cls.total_courses}.')

    @classmethod
    def display_all_courses(cls):
        print(f'All courses: ')
        for idx, course in enumerate(cls.all_courses):
            print(f'{idx}. {course}')


class DuplicateCourseError(Exception):
    pass

class InvalidGradeError(Exception):
    pass
