import reflex as rx
from jcardoso.states.GlobalState import GlobalState
from jcardoso.styles.styles import title_section_styles
from jcardoso.components.work_card import word_card

def work_experience() -> rx.Component:
    return rx.vstack(
        rx.text.strong(GlobalState.labels.items_menu[1][2], id=GlobalState.labels.items_menu[1][0], style=title_section_styles),
        rx.foreach(
            GlobalState.work_experience,
            lambda job: word_card(job)
        ),
        spacing='4',
        style={'width':'100%'}
    )