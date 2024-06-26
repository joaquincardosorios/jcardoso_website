import reflex as rx
from jcardoso.states.GlobalState import GlobalState
from jcardoso.components.video_card import video_card

def others_engineering_project()-> rx.Component:
    return rx.vstack(
        rx.text('Mi proyecto de Ingenieria'),
        rx.grid(
            rx.foreach(
                GlobalState.my_engineering_project,
                lambda item: video_card(item)
            ),
            columns='3',
            width='100%',
            spacing='1'
        ),
        width='100%'
    )