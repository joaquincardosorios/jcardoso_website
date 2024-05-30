import reflex as rx
from jcardoso.states.GlobalState import GlobalState
from jcardoso.styles.styles import title_card_styles
from jcardoso.components.education_card import education_car

def education() -> rx.Component:
    return rx.vstack(
        rx.text(GlobalState.labels.items_menu[2][2], id=GlobalState.labels.items_menu[2][0], style=title_card_styles),
        education_car(
            '2022',
            '2023',
            'Técnico Analista Programador',
            'Instituto Profesional Virginio Gomez, Concepción',
            icon='virginio.png'
        ),
        education_car(
            '2007',
            '2014',
            'Ingeniería Civil Mecánica',
            'Universidad de Concepción, Concepción, Chile',
            '''Memoria de titulo: "Construcción de péndulo invertido e implementacion de un sistema de control basado en microcontrolador para su posicionamiento vertical."''',
            icon='udec.jpg'
        ),
        education_car(
            '2007',
            '2013',
            'Licenciatura en Ciencias de la Ingeniería',
            'Universidad de Concepción, Concepción, Chile',
            icon='udec.jpg'
        ),
        rx.text('Otras Formaciones', style={'font_weight':'bold'}),
        education_car(
            '2024',
            'Presente',
            'Bootcamp de Ciencia de Datos',
            'TripleTen',
        ),
        education_car(
            '2023',
            '2023',
            'Formación Front End con React',
            'Alura Latam',
            icon='alura.png'
        ),
        education_car(
            '2023',
            '2023',
            'Node.js - Bootcamp Desarrollo Web inc. MVC y REST APIs',
            'Udemy',
            icon='udemy.png'
        ),
        education_car(
            '2023',
            '2023',
            'Javascript Moderno Guia Definitiva, por Juan Pablo de la Torre',
            'Udemy',
            icon='udemy.png'
        ),
        spacing='4',
        style={
            'width':'100%',
        }
    )