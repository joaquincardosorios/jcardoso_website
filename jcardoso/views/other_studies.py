import reflex as rx
from jcardoso.states.GlobalState import GlobalState
from jcardoso.styles.styles import title_section_styles
from jcardoso.components.education_card import education_card

def other_studies() -> rx.Component:
    return rx.vstack(
        rx.text.strong(GlobalState.labels.items_menu[3][2], id=GlobalState.labels.items_menu[3][0], style=title_section_styles),
        rx.foreach(
            GlobalState.courses,
            lambda item: education_card(item)
        ),

        spacing='4',
        style={
            'width':'100%',
        }
    )