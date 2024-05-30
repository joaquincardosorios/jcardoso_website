import reflex as rx
from jcardoso.styles.styles import work_card_style

def word_card() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text('Ene/2023 - Actualidad'),
            width='30%',
            align='start'
        ),
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.text('Crecic S.A.'),
                    rx.link(
                        rx.icon('external-link', style={'height': '16px', 'color':'#FFFFFF'}),
                        href='https://www.crecic.cl',
                        is_external=True
                    ),
                    spacing='1'
                ),
                rx.text('Concepcion, Chile'),
                rx.text('holaaaaaa aaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaa aaaaaa aaaaa'),
                spacing='1'
            ),
            width='70%',
        ),
        style=work_card_style
    )