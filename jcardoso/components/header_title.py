import reflex as rx
import random
from jcardoso.styles.colors import Color as Color
from jcardoso.styles.styles import header_title_styles, header_tags_style

from jcardoso.states.GlobalState import GlobalState

class PhotoState(rx.State):
    pic_number: int = 1

    def change_pic(self):
        if self.pic_number == 3:
            self.pic_number = 1
        else:
            self.pic_number += 1

def header_title() -> rx.Component:
    return rx.box(
        rx.popover.root(
            rx.popover.trigger(
                rx.box(
                    rx.text(
                        "Joaquin",
                        as_='span',
                        style= {'color':Color.PRIMARY.value},
                        on_click=PhotoState.change_pic
                    ),
                    f" Cardoso",
                    style=header_title_styles,
                    
                ),
            ),
            rx.popover.content(
                rx.box(
                    rx.image(src=f'me/{PhotoState.pic_number}.jpg', width='70px', height='auto', border_radius='10%'),
                ),
                style={'width':'100%'}
            ),

        ),
        rx.foreach(
            GlobalState.navbar.description_list,
            lambda item: rx.list(item, style=header_tags_style),
        ),
        # rx.list('Estudiante de Ciencia de Datos', style=header_tags_style),
        # rx.list('Analista Programador', style=header_tags_style),
        # rx.list('Licenciado en Ciencias de la Ingenieria', style=header_tags_style),
        # rx.list('Alma errante', style=header_tags_style),
        style={'width':'100%'}
    )