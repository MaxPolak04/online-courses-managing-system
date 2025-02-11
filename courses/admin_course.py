from course import Course


class AdminCourse(Course):
    def __init__(self, course_name, instructor, total_hours, tools):
        super().__init__(course_name, instructor, total_hours)
        self.tools = tools

    @property
    def tools(self):
        return self._tools

    @tools.setter
    def tools(self, required_tools: list):
        if not isinstance(required_tools, list):
            raise TypeError('')
        for tool in required_tools:
            if not isinstance(tool, str):
                raise InvalidTypeInList('')
        self._tools = required_tools

    def get_details(self):
        print(f'This course contains content for students who want to learn administration in the areas of: \
        databases, operating systems and computer networks.\nTitle: {self.course_name}\nInstructor: \
        {self.instructor} Total hours: {self.total_courses}\nTools: {", ".join(self.tools)}')


class InvalidTypeInList(Exception):
    pass
