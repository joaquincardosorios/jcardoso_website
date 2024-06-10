import reflex as rx
from typing import List, Dict, Callable

class Labels(rx.Model):
    items_menu: List[List[str]]
    work_card: List[str]

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
    description:List[str]
    skills: List[str]

class EducationExperience(rx.Base):
    year_start: int
    year_end: int
    icon: str
    title: str
    institution: str
    other_title: str = ''
    other: str = ''
