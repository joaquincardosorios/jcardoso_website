import reflex as rx
import datetime
from jcardoso.styles.styles import Size as Size
from jcardoso.styles.styles import TextColor as TextColor
from jcardoso.styles.styles import Color as Color


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src='favicon.ico'),
        rx.link(
            f"{datetime.date.today().year} Sitio web creado por Joaquin Rios con Reflex",
            href='#',
            is_external=True,
            width='auto',
            font_size=Size.MEDIUM.value
            ),
        rx.text(
            'Que la fuerza los acompañe.', 
            font_size=Size.MEDIUM.value
        ),
        align='center',
        padding_y=Size.DEFAULT.value,
        gap='0',
        color=TextColor.FOOTER.value,
        width='100%'
    )