import reflex as rx
from jcardoso.styles.styles import main_scroll_area_style, main_style
from .summary import summary
from .work_experience import work_experience
from .education import education
from .other_studies import other_studies
from .projects import projects
from .others import others

def main() -> rx.Component:
    return rx.vstack(
        summary(),
        work_experience(),
        education(),
        other_studies(),
        projects(),
        others(),
        spacing='9',
        padding_x = ['0','0','0','1em','1em'], 
        **main_style
    )