import reflex as rx
from typing import List
from jcardoso.states.GlobalState import GlobalState
from jcardoso.bases.bases import Project
from jcardoso.components.custom_badge import custom_badge
from jcardoso.styles.styles import work_card_style

class ProjectCardState(rx.State):
    technologies:List[str] = []

    @classmethod
    def update_listtechnologies(cls, new_name: List[str]):
        cls.technologies = new_name


def project_card(project:Project) -> rx.Component:
    ProjectCardState.update_listtechnologies(project.technologies)
    return rx.box(
        rx.flex(
            rx.box(
                rx.cond(
                    project.link,
                    rx.link(
                        rx.image(src=f'/projects/{project.img}', max_height='100px'),
                        href=project.link,
                        is_external=True,
                        display='flex',
                        justify_content='center'
                    ),
                    rx.image(
                        src=f'/projects/{project.img}', 
                        max_height='100px',
                        display='flex',
                        justify_content='center'
                    ), 
                ),
                width='30%',
                display='flex',
                justify_content='center'
            ),
            rx.box(
                rx.vstack(
                    rx.flex(
                        rx.text.strong(project.title),
                        rx.text(f'({project.date})'),
                        justify='between',
                        width='100%'
                    ),
                    rx.text(project.description),
                    # rx.text('Host en Vercel, React, Tailwind, HTML'),
                    rx.cond(
                        project.repository,
                        rx.link(
                            rx.hstack(
                                rx.text(GlobalState.labels.work_card[4]),
                                rx.icon('external-link', style={'height': '16px', 'color':'#FFFFFF'}),
                                spacing='0'
                            ),
                            href=project.repository, 
                            is_external=True),
                        rx.text('{Repositorio privado}'),
                    ),
                    spacing='1'
                ),
                width='70%',
                padding_left='10px'
            ),
        ),
        rx.cond(
            ProjectCardState.technologies,
            rx.box(
                rx.text.strong(f'{GlobalState.labels.work_card[5]}: '),
                rx.flex(
                    rx.foreach(
                        project.technologies,
                        lambda skill: custom_badge(skill)
                    ),
                    spacing='2',
                    margin_top='5px',
                    wrap='wrap'
                ),
                margin_top='5px',
            ),
        ),
        style=work_card_style
    )