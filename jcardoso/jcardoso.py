import reflex as rx
# Styles
import jcardoso.styles.styles as styles
from jcardoso.styles.styles import Size as Size
from jcardoso.styles.styles import container_style, flex_container_style
from jcardoso.constants import FONTS_URL as FONTS_URL
#Views
from jcardoso.views.sidebar import sidebar
from jcardoso.views.main import main

from jcardoso.states.GlobalState import GlobalState

@rx.page(on_load=GlobalState.get_data)
def index() -> rx.Component:
    return rx.box(
        rx.script("""
            function scrollToElement(elementId) {
                var element = document.getElementById(elementId);
                elementId.scrollIntoView({ behavior: 'smooth' });
            }
        """),
        rx.flex(
            sidebar(),
            main(),
            style=flex_container_style,
            spacing='4'
        ),
        style=container_style
    )

app = rx.App(
    theme=rx.theme(appearance='dark'),
    style=styles.BASE_STYLE,
    stylesheets=[
        FONTS_URL,
    ],
)
app.add_page(index)
