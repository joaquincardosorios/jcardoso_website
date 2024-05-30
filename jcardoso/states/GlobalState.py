import reflex as rx
import importlib
from typing import List
import jcardoso.bases.bases as bases
from jcardoso.translations import en, es

class GlobalState(rx.State):
    lang: str = 'es'
    skilled_jobs: bool= True
    labels: bases.Labels = es.labels
    navbar: bases.Navbar = None
    about: bases.About = None
    jobs: List[bases.WorkExperienceCard] = []

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
        else:
            self.labels = en.labels
        # self.header = data.header
        # self.jobs = data.jobs if self.skilled_jobs else [job for job in self.jobs if job.get('skilled') == True]
    
    # def filter_jobs(self):
