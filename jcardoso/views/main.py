import reflex as rx
from jcardoso.styles.styles import main_style
from .summary import summary
from .work_experience import work_experience
from .education import education
from .projects import projects

def main() -> rx.Component:
    return rx.scroll_area(
        rx.vstack(
            summary(),
            work_experience(),
            education(),
            projects(),
            spacing='9',
            width='100%'
        ),
        style=main_style,
        scrollbars='vertical',
        type="hover",
    )