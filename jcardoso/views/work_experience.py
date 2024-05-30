import reflex as rx
from jcardoso.styles.styles import title_card_styles
from jcardoso.components.work_card import word_card

def work_experience() -> rx.Component:
    return rx.vstack(
        rx.text('Experiencia Laboral', id='work_experience', style=title_card_styles),
        word_card(),
        word_card(),
        word_card(),
        word_card(),
        spacing='4',
        style={'padding_x':'5px'}
    )