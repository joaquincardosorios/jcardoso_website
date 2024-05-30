import reflex as rx
from jcardoso.styles.styles import title_card_styles
from jcardoso.components.education_card import education_car

def education() -> rx.Component:
    return rx.vstack(
        rx.text('Estudios Formales', id='education', style=title_card_styles),
        education_car(
            '2022',
            '2023',
            'Técnico Analista Programador',
            'Instituto Profesional Virginio Gomez, Concepción'
        ),
        education_car(
            '2007',
            '2014',
            'Ingeniería Civil Mecánica',
            'Universidad de Concepción, Concepción, Chile',
            '''Memoria de titulo: "Construcción de péndulo invertido e implementacion de un sistema de control basado en microcontrolador para su posicionamiento vertical."'''
        ),
        education_car(
            '2007',
            '2013',
            'Licenciatura en Ciencias de la Ingeniería',
            'Universidad de Concepción, Concepción, Chile',
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
        ),
        education_car(
            '2023',
            '2023',
            'Node.js - Bootcamp Desarrollo Web inc. MVC y REST APIs',
            'Udemy',
        ),
        education_car(
            '2023',
            '2023',
            'Javascript Moderno Guia Definitiva, por Juan Pablo de la Torre',
            'Udemy',
        ),
        spacing='4',
    )