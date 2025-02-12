from courses.course import Course


class ProgrammingCourse(Course):
    def __init__(self, course_name, instructor, total_hours, language, level, prerequisites):
        super().__init__(course_name, instructor, total_hours)
        self.language = language
        self.level = level
        self.prerequisites = prerequisites
        self.projects = []

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, lang: str):
        if not isinstance(lang, str):
            raise TypeError('')
        if lang.capitalize() not in ['C', 'C++', 'C#', 'Java', 'Kotlin', 'PHP', 'Javascript', 'Typescript', 'Python',
                                     'Swift', 'Ruby', 'Go', 'Rust', 'Perl', 'Scala']:
            raise InvalidLanguageError('')
        self._language = lang

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, lvl: str):
        if not isinstance(lvl, str):
            raise TypeError('')
        if lvl.capitalize() not in ['Beginner', 'Intermediate', 'Advanced']:
            raise InvalidLevelError('')
        self._level = lvl

    @property
    def prerequisites(self):
        return self._prerequisites

    @prerequisites.setter
    def prerequisites(self, requirements: list):
        if not isinstance(requirements, list):
            raise TypeError('')
        self._prerequisites = ', '.join(requirements)

    def display_projects(self):
        print('Projects created as part of the course:')
        for idx, project in enumerate(self.projects):
            print(f'\t{idx}. {project}')

    def add_project(self, new_project: str):
        if not isinstance(new_project, str):
            raise TypeError('')
        self.projects.append(new_project)

    def get_details(self):
        print(f'This course contains content for students who want to learn issues in the fields of programming, \
        webdevelopment, data science, big data, data analysis, etc.\nTitle: {self.course_name}\n\
        Instructor: {self.instructor}\nTotal hours: {self.total_hours}\nLanguage: {self.language}\n\
        Level: {self.level}\nPrerequisites: {self.prerequisites}\nProjects: {self.projects}')

    def update_course(self, course_name=None, instructor=None, total_hours=None, language=None, level=None, prerequisites=None):
        super().update_course(course_name, instructor, total_hours)
        if language:
            self.language = language
        if level:
            self.level = level
        if prerequisites:
            self.prerequisites = prerequisites


class InvalidLanguageError(Exception):
    pass


class InvalidLevelError(Exception):
    pass
