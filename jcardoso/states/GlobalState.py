import reflex as rx
import importlib
from typing import List
import jcardoso.bases.bases as bases

class GlobalState(rx.State):
    lang: str = 'en'
    skilled_jobs: bool= True
    labels: bases.Labels = None
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
        data = importlib.import_module(f'...translations.{self.lang}', package=__name__)
        self.labels = data.labels
        # self.header = data.header
        # self.jobs = data.jobs if self.skilled_jobs else [job for job in self.jobs if job.get('skilled') == True]
    
    # def filter_jobs(self):
