from abc import ABC, abstractmethod
from statistics import mean


class Course(ABC):
    """
    The Course class represents an online course that you can enroll in.

    Attributes:
    course_name (str): The name of the course.
    instructor (str): The name of the instructor.
    total_hours (int): The total hours of the course.
    total_courses (int): Number of total courses.
    all_courses (list): A list containing the names of all courses.
    """
    total_courses = 0
    all_courses = []

    def __init__(self, course_name, instructor, total_hours):
        """
        Initializes a Course object.

        Args:
        course_name (str): The name of the person.
        instructor (str): The name of the instructor.
        total_hours (int): The total hours of the course.
        ratings (list): list of all ratings
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
        """
        Gets the course_name attribute.

        Returns:
        str: The value of the attribute.
        """
        return self._course_name

    @course_name.setter
    def course_name(self, name: str):
        """
        Sets the course_name attribute.

        Args:
        name (str): The new value for the attribute.

        Raises:
        TypeError: User specified a value of a type other than str.
        DuplicateCourseError: If the name is in all_courses.
        """
        if not isinstance(name, str):
            raise TypeError('Wrong data type, name must be str type.')
        if name in self.all_courses:
            raise DuplicateCourseError('There is already a course with this name.')
        self._course_name = name

    @property
    def instructor(self):
        """
        Gets the instructor attribute.

        Returns:
        str: The value of the attribute.
        """
        return self._instructor

    @instructor.setter
    def instructor(self, full_name: str):
        """
        Sets the instructor attribute.

        Args:
        full_name (str): The new value for the attribute.

        Raises:
        TypeError: User specified a value of a type other than str.
        """
        if not isinstance(full_name, str):
            raise TypeError('Wrong data type, full_name must be str type.')
        self._instructor = full_name

    @property
    def total_hours(self):
        """
        Gets the total_hours attribute.

        Returns:
        int: The value of the attribute.
        """
        return self._total_hours

    @total_hours.setter
    def total_hours(self, value: (int, float)):
        """
        Sets the total_hours attribute.

        Args:
        value (int, float): The new value for the attribute.

        Raises:
        TypeError: User specified a value of a type other than int or float.
        """
        if not isinstance(value, (int, float)):
            raise TypeError('Wrong data type, value must be int or float type.')
        self._total_hours = value

    def display_ratings(self):
        """Returns the arithmetic average of all grades."""
        return round(mean(self.ratings), 1) if len(self.ratings) > 0 else 0


    def add_rating(self, rating: (int, float)):
        """
        Adds a grade to the course.

        Args:
        rating (int, float): Course rating from 1 to 5.

        Raises:
        TypeError: User specified a value of a type other than int or float.
        InvalidGradeError: User specified a value other than in the range [1, 5].
        """
        if not isinstance(rating, (int, float)):
            raise TypeError('Wrong data type, rating must be int or float type.')
        if rating < 0.5 or rating > 5:
            raise InvalidGradeError('Rating must be > 0 and <= 5.')
        self.ratings.append(round(rating, 1))

    @abstractmethod
    def get_details(self):
        """Abstract Method: Displays info about the course."""
        pass

    def update_course(self, course_name=None, instructor=None, total_hours=None):
        """Updates a course parameters."""
        if course_name:
            self.course_name = course_name
        if instructor:
            self.instructor = instructor
        if total_hours:
            self.total_hours = total_hours


    @classmethod
    def delete_course(cls, course_name: str):
        """
        Removes the course from the course list and decrements the course counter.
        Adds a grade to the course.

        Args:
        course_name (str): Name of the course to delete

        Raises:
        TypeError: User specified a value of a type other than str.

        Returns:
        str: A message about whether the course has been found and deleted or not.
        """
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
        """Displays number of total courses."""
        print(f'Number of total courses: {cls.total_courses}.')

    @classmethod
    def display_all_courses(cls):
        """Displays the names of all courses."""
        print(f'All courses: ')
        for idx, course in enumerate(cls.all_courses):
            print(f'{idx}. {course}')


class DuplicateCourseError(Exception):
    """Exception raised for errors in the duplicate course_name in list."""
    pass

class InvalidGradeError(Exception):
    """Exception raised for errors in the invalid grade."""
    pass
