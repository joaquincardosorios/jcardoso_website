import reflex as rx
from jcardoso.styles.styles import title_section_styles
from jcardoso.components.project_card import project_card

def projects() -> rx.Component:
    return rx.vstack(
        rx.text.strong('Proyectos', id='projects', **title_section_styles),
        project_card(),
        spacing='4',
        padding_x='5px'
    )