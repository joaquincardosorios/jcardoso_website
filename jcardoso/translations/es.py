from typing import List
import reflex as rx
from jcardoso.bases.bases import Labels, Navbar, About, WorkExperienceCard, EducationExperience

labels: Labels = Labels(
    items_menu=[
        ['about', 'Sobre mi', 'Un poco sobre mi'], 
        ['work_experience', 'Laboral', 'Experiencia Laboral'], 
        ['education','Estudios', 'Estudios'], 
        ['projects' , 'Proyectos', 'Mis proyectos'], 
        ['others','Otros', 'Otros']
    ],
    work_card=['Cargo', 'Descripción de cargo', 'Habilidades relevantes']
)

navbar: Navbar = Navbar(
    description_list= [
        'Estudiante de Ciencia de Datos',
        'Analista Programador',
        'Licenciado en Ciencia de la Ingenieria',
        'Ingeniero Civil Mecánico',
        'Alma errante'
    ]
)

about: About = About(
    description_list= [
        '''Me titulé de Ingeniero Mecánico el año 2014, y trabajé como tal durante 2 años. 
        Luego de un par de años viviendo en el extranjero decidí dar un vuelco a mi vida, 
        y estudíe lo que realmente me apaciona: Programación. Siempre me llamó, 
        desde hacer ayudantias de Matlab mientras estudiaba ingenieria, mi examen de grado relacionado con robótica,
        hasta aprender a programar en VBA en excel mientras trabajaba.''',

        '''Mientras estudiaba mi carrera de Analista Programador comencé a trabajar como programador web y he estado ahí hasta la actualidad,
        he aprendido a utilizar diversos frameworks como React y Svele, aunque intento especializarme utilizando Python,
        de hecho este sitio fué creado con el framework Reflex :P.''',

        '''Busco especializarme en Ciencia de Datos, y eso :P''',

        '''Me gusta viajar y los juegos de rol'''
    ]
)

work_experience: List[WorkExperienceCard] = [
    WorkExperienceCard(
        icon='crecic.jpg',
        company='Crecic S.A.',
        date_from='Ene-2023',
        date_to='Actualidad',
        position='Analista Programador',
        location='Concepcion, Chile',
        website='https://www.crecic.cl',
        description=[
            'prueba solo 1 lalalalalal alalalal llaalal',
            'prueba 2 lalalal alalala lalalal'
        ],
        skills=['Javascript', 'PHP', 'Svelte', 'Gitlab', 'Express','HTML', 'CSS']
    ),
    WorkExperienceCard(
        icon='ccu.jpg',
        company='Cervecera CCU S.A.',
        date_from='May-2016',
        date_to='Ene-2018',
        position='Ingeniero de Procesos',
        location='Temuco, Chile',
        website='https://www.ccu.cl',
        description=[
            'prueba solo 1 lalalalalal alalalal llaalal',
            'prueba 2 lalalal alalala lalalal'
        ],
        skills=['Excel', 'InforEAM', 'Kronos']
    ),
    WorkExperienceCard(
        icon='iansa.png',
        company='Iansa S.A.',
        date_from='Dic-2020',
        date_to='Feb-2021',
        position='Práctica profesional',
        location='San Carlos, Chile',
        website='https://empresasiansa.cl/azucar-iansa/',
        description=[
            'prueba solo 1 lalalalalal alalalal llaalal',
            'prueba 2 lalalal alalala lalalal'
        ],
        skills=[]
    ),
]

education: List[EducationExperience] = [
    EducationExperience(
        year_start=2022,
        year_end=2023,
        icon='virginio.png',
        title='Técnico Analista Programador',
        institution='Instituto Profesional Virginio Gomez, Concepción, Chile',
    ),
    EducationExperience(
        year_start=2008,
        year_end=2014,
        icon='udec.jpg',
        title='Ingeniería Civil Mecánica',
        institution='Universidad de Concepción, Concepción, Chile',
        other_title='Memoria de título',
        other='''"Construcción de péndulo invertido e implementacion de un sistema de control basado en 
        microcontrolador para su posicionamiento vertical."''',
    ),
    EducationExperience(
        year_start=2008,
        year_end=2013,
        icon='udec.jpg',
        title='Licenciatura en Ciencias de la Ingeniería',
        institution='Universidad de Concepción, Concepción, Chile',
    ),
]