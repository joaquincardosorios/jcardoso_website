import reflex as rx
from datetime import datetime
from jcardoso.styles.styles import summary_style, summary_content_style, title_card_styles

def summary() -> rx.Component:
    today = datetime.now()
    birthday = datetime.strptime('1990-01-09', "%Y-%m-%d")
    edad = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return rx.vstack(
        rx.text('Un poco sobre mi', id='about', style=title_card_styles),
        rx.vstack(
            rx.text(
                f'''
                Me titulé de Ingeniero Mecánico el año 2014, y trabajé como tal durante 2 años. 
                Luego de un par de años viviendo en el extranjero decidí dar un vuelco a mi vida, 
                y estudíe lo que realmente me apaciona: Programación. Siempre me llamó, 
                desde hacer ayudantias de Matlab mientras estudiaba ingenieria, mi examen de grado relacionado con robótica,
                hasta aprender a programar en VBA en excel mientras trabajaba.'''
            ),
            rx.text(
                f'''
                Mientras estudiaba mi carrera de Analista Programador comencé a trabajar como programador web y he estado ahí hasta la actualidad,
                he aprendido a utilizar diversos frameworks como React y Svele, aunque intento especializarme utilizando Python,
                de hecho este sitio fué creado con el framework Reflex :P.'''
            ),
            rx.text(
                f'''
                Busco especializarme en Ciencia de Datos, y eso :P'''
            ),
            rx.text(
                f'''
                Me gusta viajar y los juegos de rol'''
            ),
            style=summary_content_style
        ),
        spacing='4',
        style=summary_style
    )