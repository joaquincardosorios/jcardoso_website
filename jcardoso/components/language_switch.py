import reflex as rx
from jcardoso.states.GlobalState import GlobalState

def language_switch()-> rx.Component:
    return rx.flex(
        rx.text('EN'),
        rx.switch(
            checked=(GlobalState.lang == 'es'),
            on_change=GlobalState.toggle_language(),
            border_color="lightgray"
        ),
        rx.text('ES'),
        align='center',
        spacing='2',
        padding_right='50px'
    ),