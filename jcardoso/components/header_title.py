import reflex as rx
from jcardoso.styles.colors import Color as Color
from jcardoso.styles.styles import header_style, header_title_styles, header_tags_style

def header_title() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                "Joaquin",
                as_='span',
                style= {'color':Color.PRIMARY.value}
            ),
            f" Cardoso",
            style=header_title_styles,
        ),
        rx.list('Estudiante de Ciencia de Datos', style=header_tags_style),
        rx.list('Analista Programador', style=header_tags_style),
        rx.list('Licenciado en Ciencias de la Ingenieria', style=header_tags_style),
        rx.list('Alma errante', style=header_tags_style),
    )