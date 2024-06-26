import reflex as rx
from typing import List
from jcardoso.states.GlobalState import GlobalState
from jcardoso.styles.styles import work_card_style, title_card_style, work_card_body
from jcardoso.bases.bases import EducationExperience
from jcardoso.components.custom_badge import custom_badge

class EducationCardState(rx.State):
    skills:List[str] = []

    @classmethod
    def update_listskills(cls, new_name: List[str]):
        cls.skills = new_name


def education_card(study:EducationExperience) -> rx.Component:
    EducationCardState.update_listskills(study.skills)
    return rx.flex(
        rx.box(
            rx.vstack(
                rx.hstack(
                    # Logo
                    rx.box(
                        rx.flex(
                            rx.avatar(src=f'logos/logo_{study.icon}'),
                            width='100%',
                        ),
                        align_items='center'
                    ),
                    # Titulo e institución
                    rx.vstack(
                        rx.flex(
                            rx.text.strong(study.title, **title_card_style),
                            rx.text(f'({study.year_start} - {study.year_end})'),
                            justify='between',
                            align='center',
                            width='100%',
                            wrap='wrap',
                            spacing='1'
                        ),
                        rx.text(study.institution),
                        spacing='1',
                        width='100%'
                    ),
                    spacing='3',
                    width='100%'
                    # align='center'
                ),
                rx.flex(
                    # Estado
                    rx.hstack(
                        rx.text.strong(f'{GlobalState.labels.work_card[3]}: '),
                        rx.text(study.status),
                        spacing='1'
                    ),
                    # Link de certificados (si hay)
                    rx.cond(
                        study.link,
                        rx.hover_card.root(
                            rx.hover_card.trigger(
                                rx.link(
                                    rx.icon('external-link', style={'height': '16px', 'color':'#FFFFFF'}),
                                    href=study.link, 
                                    is_external=True
                                )
                            ),
                            rx.hover_card.content(
                                rx.text(GlobalState.labels.work_card[6])
                            )
                        ),
                        
                    ), 
                    spacing='0'
                ),
                # Datos adicionales (si hay)
                rx.cond(
                    study.other != '',
                    rx.text(rx.text.strong(f'{study.other_title}: '),study.other)
                ),
                
                # Lista de skills (si hay)
                rx.cond(
                    EducationCardState.skills,
                    rx.box(
                        rx.text.strong(f'{GlobalState.labels.work_card[2]}: '),
                        rx.flex(
                            rx.foreach(
                                study.skills,
                                lambda skill: custom_badge(skill)
                            ),
                            spacing='2',
                            margin_top='5px',
                            wrap='wrap'
                        ),
                        spacing=0
                    ),
                ),
                            
                spacing='3'         
            ),
            style=work_card_body
        ),
        style=work_card_style,
        spacing='2'
    )