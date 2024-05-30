import reflex as rx
from jcardoso.styles.styles import work_card_style

def word_card() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text('Ene-2023 / Actualidad'),
            width='20%',
            text_align='center'
        ),
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.flex(
                            rx.avatar(src='logos/logo_crecic.jpg'),
                            width='100%'
                        ),
                    ),
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
                        spacing='1'
                    ),
                    spacing='3',
                    align_items='center'
                ),
                rx.text('Cargo: Analista Programador'),
                rx.text('Descripción de cargo:'),
                rx.text('holaaaaaa aaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaa aaaaaa aaaaa'),
                spacing='1'
            ),
            width='80%',
        ),
        style=work_card_style,
        spacing='3'
    )