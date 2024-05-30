import reflex as rx
from jcardoso.styles.styles import work_card_style

def education_car(
        start:str,
        end:str,
        career:str,
        location:str,
        others:str = '',
        icon:str = 'crecic.jpg',
) -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text(f'{start} - {end}', align='center'),
            width='20%',
        ),
        rx.box(
            rx.flex(
                rx.avatar(src=f'logos/logo_{icon}'),
                width='100%'
            ),
            width='10%',
        ),
        rx.box(
            rx.vstack(
                rx.text(career),
                rx.text(location),
                rx.cond(
                    others != '',
                    rx.text(others)
                ),
                spacing='1'
            ),
            width='70%',
        ),
        style=work_card_style,
        spacing='2'
    )