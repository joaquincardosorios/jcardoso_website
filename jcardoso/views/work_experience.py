import reflex as rx
from jcardoso.states.GlobalState import GlobalState
from jcardoso.styles.styles import title_card_styles
from jcardoso.components.work_card import word_card

def work_experience() -> rx.Component:
    return rx.vstack(
        rx.text(GlobalState.labels.items_menu[1][2], id=GlobalState.labels.items_menu[1][0], style=title_card_styles),
        word_card(),
        word_card(),
        word_card(),
        word_card(),
        spacing='4',
        style={'padding_x':'5px'}
    )