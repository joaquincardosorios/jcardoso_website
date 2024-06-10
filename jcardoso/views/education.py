import reflex as rx
from jcardoso.states.GlobalState import GlobalState
from jcardoso.styles.styles import title_section_styles
from jcardoso.components.education_card import education_card

def education() -> rx.Component:
    return rx.vstack(
        rx.text.strong(GlobalState.labels.items_menu[2][2], id=GlobalState.labels.items_menu[2][0], style=title_section_styles),
        rx.foreach(
            GlobalState.education,
            # lambda item: rx.text('hoola')
            lambda item: education_card(item)
        ),
        # education_card(
        #     '2022',
        #     '2023',
        #     'Técnico Analista Programador',
        #     'Instituto Profesional Virginio Gomez, Concepción',
        #     icon='virginio.png'
        # ),
        # education_card(
        #     '2007',
        #     '2014',
        #     'Ingeniería Civil Mecánica',
        #     'Universidad de Concepción, Concepción, Chile',
        #     '''"Construcción de péndulo invertido e implementacion de un sistema de control basado en 
        #     microcontrolador para su posicionamiento vertical."''',
        #     icon='udec.jpg'
        # ),
        # education_card(
        #     '2007',
        #     '2013',
        #     'Licenciatura en Ciencias de la Ingeniería',
        #     'Universidad de Concepción, Concepción, Chile',
        #     icon='udec.jpg'
        # ),
        spacing='4',
        style={
            'width':'100%',
        }
    )