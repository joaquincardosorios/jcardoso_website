import reflex as rx
from typing import List
from jcardoso.states.GlobalState import GlobalState
from jcardoso.bases.bases import WorkExperienceCard
from jcardoso.styles.styles import work_card_style, work_card_date, work_card_body, title_card_style
from jcardoso.components.custom_badge import custom_badge

class WorkCardState(rx.State):
    skills:List[str] = []

    @classmethod
    def update_listskills(cls, new_name: List[str]):
        cls.skills = new_name


# Fechas
        # rx.box(
        #     rx.text(f'{job.date_from} / {job.date_to}'),
        #     style=work_card_date
        # ),
def word_card(job: WorkExperienceCard) -> rx.Component:
    WorkCardState.update_listskills(job.skills)
    return rx.flex(
        rx.box(
            rx.vstack(
                rx.hstack(
                    # Logo
                    rx.flex(
                        rx.avatar(src=f'logos/logo_{job.icon}', height='100%'),
                        height='100%',
                        flex='1'
                    ),
                    # Titulo, Empresa y Ubicacion
                    rx.vstack(
                        rx.flex(
                            rx.text.strong(job.position, **title_card_style),
                            rx.text(f'({job.date_from} - {job.date_to})'),
                            justify='between',
                            align='center',
                            width='100%',
                            wrap='wrap',
                            spacing='1'
                        ),
                        rx.hstack(
                            rx.text(
                                job.company,
                            ),
                            rx.link(
                                rx.icon('external-link', style={'height': '16px', 'color':'#FFFFFF'}),
                                href=job.website,
                                is_external=True
                            ),
                            rx.text(job.location),
                            spacing='1',
                            align='center'
                        ),
                        spacing='1',
                        width='100%'
                    ),
                    spacing='2',
                    align='center',
                    width='100%'
                ),
                # Descripcion
                rx.box(
                    rx.text.strong(f'{GlobalState.labels.work_card[1]}: '),
                        rx.foreach(
                            job.description,
                            lambda item: rx.text(item, style={'text_align':'justify'})
                        ),
                    spacing='1'
                ),
                # Habilidades
                rx.cond(
                    WorkCardState.skills,
                    rx.box(
                        rx.text.strong(f'{GlobalState.labels.work_card[2]}: '),
                        rx.flex(
                            rx.foreach(
                                job.skills,
                                lambda skill: custom_badge(skill)
                            ),
                            spacing='2',
                            margin_top='5px',
                            wrap='wrap'
                        ),
                        spacing='1'
                    )
                ),
                spacing='3'
            ),
            style=work_card_body
        ),
        style=work_card_style,
        spacing='3',
    )