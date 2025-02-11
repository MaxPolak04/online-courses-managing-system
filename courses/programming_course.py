from course import Course


class ProgrammingCourse(Course):
    total_courses = 0

    def __init__(self, course_name, instructor, total_hours, language, level, prerequisites):
        super().__init__(course_name, instructor, total_hours)
        self.language = language
        self.level = level
        self.prerequisites = prerequisites
        self.projects = []

    def get_details(self):
        pass
