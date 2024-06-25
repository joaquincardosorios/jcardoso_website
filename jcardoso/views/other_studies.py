import reflex as rx
from jcardoso.states.GlobalState import GlobalState
from jcardoso.styles.styles import title_section_styles
from jcardoso.components.education_card import education_card

def other_studies() -> rx.Component:
    return rx.vstack(
        rx.text.strong(GlobalState.labels.items_menu[3][2], id=GlobalState.labels.items_menu[3][0], style=title_section_styles),
        rx.foreach(
            GlobalState.courses,
            lambda item: education_card(item)
        ),
        # education_card(
        #     '2024',
        #     'Presente',
        #     'Bootcamp de Ciencia de Datos',
        #     'TripleTen',
        # ),
        # education_card(
        #     '2023',
        #     '2023',
        #     'Formación Front End con React',
        #     'Alura Latam',
        #     icon='alura.png'
        # ),
        # education_card(
        #     '2023',
        #     '2023',
        #     'Node.js - Bootcamp Desarrollo Web inc. MVC y REST APIs',
        #     'Udemy',
        #     icon='udemy.png'
        # ),
        # education_card(
        #     '2023',
        #     '2023',
        #     'Javascript Moderno Guia Definitiva, por Juan Pablo de la Torre',
        #     'Udemy',
        #     icon='udemy.png'
        # ),
        spacing='4',
        style={
            'width':'100%',
        }
    )