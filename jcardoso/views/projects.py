import reflex as rx
from jcardoso.styles.styles import title_card_styles
from jcardoso.components.project_card import project_card

def projects() -> rx.Component:
    return rx.vstack(
        rx.text('Proyectos', id='projects', style=title_card_styles),
        project_card(),
        spacing='4',
        style={'padding_x':'5px'}
    )