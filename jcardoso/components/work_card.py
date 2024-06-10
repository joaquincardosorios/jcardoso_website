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
          
def word_card(job: WorkExperienceCard) -> rx.Component:
    WorkCardState.update_listskills(job.skills)
    return rx.flex(
        rx.box(
            rx.text(f'{job.date_from} / {job.date_to}'),
            style=work_card_date
        ),
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.flex(
                            rx.avatar(src=f'logos/logo_{job.icon}'),
                            width='100%',
                        ),
                    ),
                    rx.vstack(
                        rx.text.strong(job.position, **title_card_style),
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
                        spacing='1'
                    ),
                    spacing='3',
                    align='center'
                ),
                rx.text.strong(f'{GlobalState.labels.work_card[1]}: '),
                rx.foreach(
                    job.description,
                    lambda item: rx.text(item)
                ),
                rx.cond(
                    WorkCardState.skills,
                    rx.fragment(
                        rx.text.strong(f'{GlobalState.labels.work_card[2]}: '),
                        rx.flex(
                            rx.foreach(
                                job.skills,
                                lambda skill: custom_badge(skill)
                            ),
                            spacing='3',
                            margin_top='5px',
                            wrap='wrap'
                        )
                    )
                ),
                spacing='1'
            ),
            style=work_card_body
        ),
        style=work_card_style,
        spacing='3',
    )