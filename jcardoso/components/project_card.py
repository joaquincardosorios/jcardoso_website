import reflex as rx
from jcardoso.styles.styles import work_card_style

def project_card() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.link(
                rx.image(src='/projects/pg_estudio.png'),
                href='https://pg-estudio.vercel.app/',
                is_external=True
            ),
            width='30%',
        ),
        rx.box(
            rx.vstack(
                rx.text('PG Estudio', style={'font_weight' : 'bold'},),
                rx.text('Sitio web para muestra de papeles murales'),
                rx.text('Host en Vercel, React, Tailwind, HTML'),
                rx.text('{Repositorio privado}'),
                spacing='1'
            ),
            width='70%',
            padding_left='10px'
        ),
        style=work_card_style
    )