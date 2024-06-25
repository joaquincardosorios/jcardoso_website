import reflex as rx
from jcardoso.states.GlobalState import GlobalState
from jcardoso.styles.styles import title_section_styles
from jcardoso.components.project_card import project_card

def projects() -> rx.Component:
    return rx.vstack(
        rx.text.strong(GlobalState.labels.items_menu[4][2], id=GlobalState.labels.items_menu[4][0], **title_section_styles),
        rx.foreach(
            GlobalState.projects,
            lambda item: project_card(item)
        ),
        # project_card(),
        spacing='4',
        padding_x='5px'
    )