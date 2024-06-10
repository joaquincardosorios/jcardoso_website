import reflex as rx
from datetime import datetime
from jcardoso.states.GlobalState import GlobalState
from jcardoso.styles.styles import summary_style, summary_content_style, title_section_styles


def summary() -> rx.Component:
    return rx.vstack(
        rx.text.strong(GlobalState.labels.items_menu[0][2], id=GlobalState.labels.items_menu[0][0], style=title_section_styles),
        rx.vstack(
            rx.foreach(
                GlobalState.about.description_list,
                lambda item: rx.text(item)
            ),
            style=summary_content_style
        ),
        spacing='4',
        style=summary_style
    )