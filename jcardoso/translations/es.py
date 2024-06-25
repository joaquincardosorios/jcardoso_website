from typing import List
import reflex as rx
from jcardoso.bases.bases import *

labels: Labels = Labels(
    items_menu=[
        ['about', 'Sobre mi', 'Un poco sobre mi'], 
        ['work_experience', 'Laboral', 'Experiencia Laboral'], 
        ['education','Estudios', 'Estudios'],
        ['courses', 'Cursos', 'Cursos y certificaciones'],
        ['projects' , 'Proyectos', 'Mis proyectos'], 
        ['others','Otros', 'Otros']
    ],
    work_card=['Cargo', 'Descripción de cargo', 'Habilidades relevantes', 'Estado', 'Repositorio', 'Tecnologias', 'Ver certificado']
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
        '''Me gradué como Ingeniero Mecánico en 2014 y trabajé en ese campo durante 2 años. 
        Después de vivir en el extranjero por un tiempo, decidí cambiar mi rumbo y seguir mi 
        verdadera pasión: la programación. Desde mis días como asistente en MATLAB durante 
        mis estudios de ingeniería, hasta mi proyecto de grado en robótica y aprender a 
        programar en VBA para Excel mientras trabajaba, siempre he estado involucrado en 
        el mundo de la programación.''',

        '''Durante mis estudios como Analista Programador, comencé a trabajar como programador 
        web y he continuado en este campo hasta hoy. He aprendido a utilizar varios frameworks 
        como React y Svelte, pero mi enfoque principal ahora es especializarme en Python. De hecho, 
        este sitio web lo desarrollé usando el framework Reflex.''',

        '''Actualmente, estoy inmerso en un bootcamp de Ciencia de Datos, 
        lo cual refleja mi fuerte interés en esta área. Disfruto explorando y 
        analizando datos para lograr entender lo que tratan de contar. Mi meta es fusionar mis habilidades 
        de programación con técnicas avanzadas de análisis de datos para abordar desafíos complejos de manera innovadora.''',

        '''Además de la programación y la Ciencia de Datos, me apasiona viajar, 
        los libros de fantasia, los juegos de mesa y de rol.'''
    ]
)

work_experience: List[WorkExperienceCard] = [
    WorkExperienceCard(
        icon='crecic.jpg',
        company='Crecic S.A.',
        date_from='01/2023',
        date_to='Actualidad',
        position='Analista Programador',
        location='Concepcion, Chile',
        website='https://www.crecic.cl',
        description=[
            '''Actualmente formo parte del equipo tanto del equipo de asistencia al cliente, 
            resolviendo problemas de la plataforma SGM (Sistema de Gestión Municipal) que se encuentra en producción, 
            como en el equipo de desarrollo, diseñando una nueva versión de este, utlizando tecnologias
            actuales y en función de las nuevas normativas.
            '''
        ],
        skills=['Javascript', 'PHP', 'Svelte', 'Gitlab', 'Express','HTML', 'CSS']
    ),
    WorkExperienceCard(
        icon='ccu.jpg',
        company='Cervecera CCU S.A.',
        date_from='05/2016',
        date_to='01/2018',
        position='Ingeniero de Procesos',
        location='Temuco, Chile',
        website='https://www.ccu.cl',
        description=[
            '''Estuve a cargo del mantenimiento mecánico dentro del área de Elaboración, 
            donde mis principales tareas se centraban en la gesión de las actividades de mantenimiento
            predictivo/preventivo, gestión de respuestos y liderar las iniciativas de mejora continua.
            ''',
        ],
        skills=['Excel', 'InforEAM', 'Kronos']
    ),
    WorkExperienceCard(
        icon='iansa.png',
        company='Iansa S.A.',
        date_from='12/2020',
        date_to='02/2021',
        position='Práctica profesional',
        location='San Carlos, Chile',
        website='https://empresasiansa.cl/azucar-iansa/',
        description=[
            '''
            Mi tarea principal fué el levantamiento de datos de equipos criticos dentro del area
            de producción, para posteriormente realizar un plan de mantenimiento preventivo basado en
            el analisis de lubricación y temperatura de los equipos.
            '''
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
        status='Titulado'
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
        status='Titulado'
    ),
    EducationExperience(
        year_start=2008,
        year_end=2013,
        icon='udec.jpg',
        title='Licenciatura en Ciencias de la Ingeniería',
        institution='Universidad de Concepción, Concepción, Chile',
        status='Titulado'
    ),
]

other_studies: List[EducationExperience] = [
    EducationExperience(
        year_start=2024,
        year_end=2024,
        icon='tripleten.png',
        title='Bootcamp en Ciencia de Datos',
        institution='TripleTen',
        skills=['Python', 'SQL', 'Pandas', 'Scikit-learn', 'Catboost', 'LightGBM'],
        status='En curso'
    ),
    EducationExperience(
        year_start=2023,
        year_end=2023,
        icon='alura.png',
        title='Formación Frontend con React',
        institution='Alura Latam',
        link_title='Certificado',
        link='https://app.aluracursos.com/degree/certificate/17ee41c9-a847-4fdf-837e-7127320245da',
        skills=['HTML', 'CSS', 'Javascript', 'React', 'Github'],
        status='Finalizado'
    ),
    EducationExperience(
        year_start=2023,
        year_end=2023,
        icon='udemy.png',
        title='Node.js - Desarrollo Web, MVC y REST APIs',
        institution='Udemy',
        other_title='Información adicional',
        other='''Curso de 43 horas teoricas y prácticas, dirigidas por Juan Pablo de la Torre''',
        link_title='Certificado',
        link='https://www.udemy.com/certificate/UC-27fef825-1369-4e27-8eb3-78e2b924a604/',
        skills=['Javascript', 'Rest API', 'MongoDB'],
        status='Finalizado'
    ),
    EducationExperience(
        year_start=2023,
        year_end=2023,
        icon='udemy.png',
        title='Javascript Moderno Guia Definitiva',
        institution='Udemy',
        other_title='Información adicional',
        other='''Curso de 52 horas teoricas y prácticas, dirigidas por Juan Pablo de la Torre''',
        link_title='Certificado',
        link='https://www.udemy.com/certificate/UC-c37656db-ea03-4a48-b74c-a3efab69fcae/',
        skills=['Javascript','Node.js', 'React', 'Rest API', 'MongoDB'],
        status='Finalizado'
    ),
]

projects: List[Project] = [
    Project(
        title='Mi Portafolio',
        date='06/2024',
        description='Mi sitio personal con mis proyectos (la página en la que estas ahora)',
        technologies=['Python','Reflex'],
        link='https://jcardoso.reflex.run/',
        img='jcardoso.png',
        repository='https://github.com/joaquincardosorios/jcardoso_website'
    ),
    Project(
        title='Analisis de sentimientos, ML aplicado a textos',
        date='05/2024',
        description='Este repositorio contiene un proyecto en Python que entrena varios modelos de machine learning para clasificar reseñas de películas como positivas o negativas. Los modelos se basan en técnicas de procesamiento de lenguaje natural.',
        technologies=['Python','Pandas', 'Numpy','Matplotlib', 'Seaborn', 'tqdm', 'Scikit-learn', 'NLTK', 'Spacy', 'LightGBM'],
        img='not_image.png',
        repository='https://github.com/joaquincardosorios/jcardoso_website'
    ),
    Project(
        title='Analisis de ML de caso con series temporales',
        date='05/2024',
        description='Se realiza analisis y entrenamiento de modelo para predecir número de taxis requeridos por una flota en un aeropuerto',
        technologies=['Python','Pandas', 'Numpy', 'Scikit-learn', 'Catboost', 'LightGBM'],
        img='not_image.png',
        repository='https://github.com/joaquincardosorios/jcardoso_website'
    ),
    Project(
        title='PG Estudio',
        date='08/2023',
        description='Sitio web para muestra de papeles murales',
        technologies=['HTML', 'React', 'Tailwind', 'Vercel'],
        link='https://pg-estudio.vercel.app/',
        img='pg_estudio.png'
    ),
]