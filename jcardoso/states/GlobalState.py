import reflex as rx
from typing import List
import jcardoso.bases.bases as bases
from jcardoso.translations import en, es

class GlobalState(rx.State):
    lang: str = 'es'
    skilled_jobs: bool= True
    labels: bases.Labels = es.labels
    navbar: bases.Navbar = es.navbar
    about: bases.About = es.about
    work_experience : List[bases.WorkExperienceCard] = es.work_experience
    education: List[bases.EducationExperience] = es.education
    courses: List[bases.EducationExperience] = es.other_studies
    projects: List[bases.Project] = es.projects
    my_engineering_project: List[bases.VideoCard] = es.my_engineering_project

    def toggle_language(self):
        if self.lang == 'en':
            self.lang = 'es'
        else:
            self.lang = 'en'
        self.get_data()
    
    def filter_jobs(self):
        self.skilled_jobs = not self.skilled_jobs
        self.get_data()

    def get_data(self):
        if self.lang == 'es':
            self.labels = es.labels
            self.work_experience = es.work_experience
            self.navbar = es.navbar
            self.about = es.about
            self.education = es.education
            self.courses = es.other_studies
            self.projects = es.projects
            self.my_engineering_project = es.my_engineering_project
            # self.others = es.others
        else:
            self.labels = en.labels
            self.work_experience = en.work_experience
            self.navbar = en.navbar
            self.about = en.about
            self.education = en.education
            self.projects = en.projects
            self.my_engineering_project = en.my_engineering_project
            # self.others = en.others
        # self.header = data.header
        # self.jobs = data.jobs if self.skilled_jobs else [job for job in self.jobs if job.get('skilled') == True]
    
    # def filter_jobs(self):
