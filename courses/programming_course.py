from courses.course import Course


class ProgrammingCourse(Course):
    """
    The ProgrammingCourse class represents a course in the areas of management:
    programming, webdevelopment, data science, big data, data analysis

    Attributes:
    course_name (str): The name of the course.
    instructor (str): The name of the instructor.
    total_hours (int): The total hours of the course.
    language (str): The name of the programming language.
    level (str): The name of the skill level.
    prerequisites (list): List of requirements to start the course.
    projects (list): List of projects in course.
    """
    def __init__(self, course_name, instructor, total_hours, language, level, prerequisites):
        """
        Initializes a ProgrammingCourse object.

        Args:
        course_name (str): The name of the person.
        instructor (str): The name of the instructor.
        total_hours (int): The total hours of the course.
        language (str): The name of the programming language.
        level (str): The name of the skill level.
        prerequisites (list): List of requirements to start the course.
        projects (list): List of projects in course.
        """
        super().__init__(course_name, instructor, total_hours)
        self.language = language
        self.level = level
        self.prerequisites = prerequisites
        self.projects = []

    @property
    def language(self):
        """
        Gets the language attribute.

        Returns:
        str: The value of the attribute.
        """
        return self._language

    @language.setter
    def language(self, lang: str):
        """
        Sets the language attribute.

        Args:
        lang (str): The new value for the attribute.

        Raises:
        TypeError: User specified a value of a type other than str.
        InvalidLanguageError: If a language is specified that does not exist.
        """
        if not isinstance(lang, str):
            raise TypeError('Wrong data type, lang must be str type')
        if lang.capitalize() not in ['C', 'C++', 'C#', 'Java', 'Kotlin', 'PHP', 'Javascript', 'Typescript', 'Python',
                                     'Swift', 'Ruby', 'Go', 'Rust', 'Perl', 'Scala']:
            raise InvalidLanguageError('There is no such language.')
        self._language = lang

    @property
    def level(self):
        """
        Gets the level attribute.

        Returns:
        str: The value of the attribute.
        """
        return self._level

    @level.setter
    def level(self, lvl: str):
        """
        Sets the level attribute.

        Args:
        lvl (str): The new value for the attribute.

        Raises:
        TypeError: User specified a value of a type other than str.
        InvalidLevelError: If an incorrect level is specified.
        """
        if not isinstance(lvl, str):
            raise TypeError('Wrong data type, lvl must be str type.')
        if lvl.capitalize() not in ['Beginner', 'Intermediate', 'Advanced']:
            raise InvalidLevelError('lvl must be: "Beginner", "Intermediate" or "Advanced".')
        self._level = lvl

    @property
    def prerequisites(self):
        """
        Gets the prerequisites attribute.

        Returns:
        list: The value of the attribute.
        """
        return self._prerequisites

    @prerequisites.setter
    def prerequisites(self, requirements: list):
        """
        Sets the prerequisites attribute.

        Args:
        requirements (list): The new value for the attribute.

        Raises:
        TypeError: User specified a value of a type other than list.
        """
        if not isinstance(requirements, list):
            raise TypeError('Wrong data type, requirements must be list type.')
        self._prerequisites = ', '.join(requirements)

    def display_projects(self):
        """Displays projects in course."""
        if len(self.projects) > 0:
            print('Projects created as part of the course:')
            for idx, project in enumerate(self.projects, start=1):
                print(f'\t{idx}. {project}')
        else:
            print('No project added.')

    def add_project(self, *new_projects):
        """
        Adds new project to programming course.

        Args:
        new_project (args): Names of the projects in the course

        Raises:
        TypeError: User entered wrong data type for project name in *new_projects.
        """
        for project in new_projects:
            if not isinstance(project, str):
                raise TypeError('Wrong data type, project must be str type.')
            self.projects.append(project)

    def get_details(self):
        """Displays info about thr course."""
        print(f'This course contains content for students who want to learn issues in the fields of programming, \
webdevelopment, data science, big data, data analysis, etc.\nTitle: {self.course_name}\n\
Instructor: {self.instructor}\nTotal hours: {self.total_hours}\nLanguage: {self.language}\n\
Level: {self.level}\nPrerequisites: {self.prerequisites}\nProjects: {self.projects}')

    def update_course(self, course_name=None, instructor=None, total_hours=None, language=None, level=None, prerequisites=None):
        """Updates a course parameters."""
        super().update_course(course_name, instructor, total_hours)
        if language:
            self.language = language
        if level:
            self.level = level
        if prerequisites:
            self.prerequisites = prerequisites


class InvalidLanguageError(Exception):
    """Exception raised for errors in the input language."""
    pass


class InvalidLevelError(Exception):
    """Exception raised for errors in the input level."""
    pass
