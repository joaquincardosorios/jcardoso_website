import reflex as rx
from jcardoso.states.GlobalState import GlobalState
from jcardoso.styles.styles import title_section_styles
from .others_engineering_project import others_engineering_project
def others() -> rx.Component:
    return rx.vstack(
        rx.text.strong(GlobalState.labels.items_menu[5][2], id=GlobalState.labels.items_menu[5][0], **title_section_styles),
        others_engineering_project(),
        # rx.foreach(
        #     GlobalState.projects,
        #     lambda item: project_card(item)
        # ),
        # project_card(),
        spacing='4',
        padding_x='5px',
        width='100%'
    )