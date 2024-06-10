import reflex as rx
from typing import List, Callable
from jcardoso.styles.styles import work_card_style, title_card_style
from jcardoso.bases.bases import EducationExperience


def education_card(study:EducationExperience) -> rx.Component:

    return rx.flex(
        rx.box(
            rx.text(f'{study.year_start} - {study.year_end}', align='center'),
            width='20%',
        ),
        rx.box(
            rx.flex(
                rx.avatar(src=f'logos/logo_{study.icon}'),
                width='100%',
                padding_top='5px'
            ),
            width='10%',
        ),
        rx.box(
            rx.vstack(
                rx.text.strong(study.title, **title_card_style),
                rx.text(study.institution),
                rx.cond(
                    study.other != '',
                    rx.text(rx.text.strong(f'{study.other_title}: '),study.other)
                ),
                spacing='1'
            ),
            width='70%',
        ),
        style=work_card_style,
        spacing='2'
    )