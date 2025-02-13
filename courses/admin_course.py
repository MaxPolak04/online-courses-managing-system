from courses.course import Course


class AdminCourse(Course):
    """
    The AdminCourse class represents a course in the areas of management:
    operating systems, databases and computer networks.

    Attributes:
    course_name (str): The name of the course.
    instructor (str): The name of the instructor.
    total_hours (int): The total hours of the course.
    tools (str): The name of the required tools.
    """
    def __init__(self, course_name, instructor, total_hours, tools):
        """
        Initializes a AdminCourse object.

        Args:
        course_name (str): The name of the person.
        instructor (str): The name of the instructor.
        total_hours (int): The total hours of the course.
        tools (str): The name of the required tools.
        """
        super().__init__(course_name, instructor, total_hours)
        self.tools = tools

    @property
    def tools(self):
        """
        Gets the tools attribute.

        Returns:
        list: The value of the attribute.
        """
        return self._tools

    @tools.setter
    def tools(self, required_tools: list):
        """
        Sets the tools attribute.

        Args:
        required_tools (list): The new value for the attribute.

        Raises:
        TypeError: User specified a value of a type other than list.
        InvalidTypeInList: if in list are values of a type other than str.
        """
        if not isinstance(required_tools, list):
            raise TypeError('Wrong data type, required_tools must be list type.')
        for tool in required_tools:
            if not isinstance(tool, str):
                raise InvalidTypeInList('In a list there can only be values of type str')
        self._tools = required_tools

    def get_details(self):
        """Displays info about thr course."""
        print(f'This course contains content for students who want to learn administration in the areas of: \
databases, operating systems and computer networks.\nTitle: {self.course_name}\nInstructor: \
{self.instructor} \nTotal hours: {self.total_hours}\nTools: {", ".join(self.tools)}')

    def update_course(self, course_name=None, instructor=None, total_hours=None, tools=None):
        """Updates a course parameters."""
        super().update_course(course_name, instructor, total_hours)
        if tools:
            self.tools = tools


class InvalidTypeInList(Exception):
    """Exception raised for errors in invalid type in list."""
    pass
