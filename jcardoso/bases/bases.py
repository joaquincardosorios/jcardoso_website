import reflex as rx
from typing import List, Dict

class Labels(rx.Model):
    items_menu: List[List[str]]
    # about: str
    # work_experience: str
    # we_description :str
    # we_skills: str
    # education: str
    # projects: str
    # others: str

class Navbar(rx.Base):
    description_list: List[str]

class About(rx.Base):
    description_list: List[str]

class WorkExperienceCard(rx.Base):
    icon: str
    company:str
    date_from: str
    date_to: str
    position:str
    location:str
    website:str
    description:str
    skills: List[str]