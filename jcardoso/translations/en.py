from jcardoso.bases.bases import *
from typing import List

labels: Labels = Labels(
    items_menu =[
        ['about', 'About me', 'A little about me'], 
        ['work_experience', 'Experience', 'Work Experience'], 
        ['education','Education','Education', 'Status', 'Relevant Skills'], 
        ['courses', 'Courses', 'Courses and Certifications'],
        ['projects' , 'Projects','My projects'], 
        ['others','Others']
    ],
    work_card=['Position', 'Job description', 'Skills', 'Status', 'Repository', 'Techonologies', 'Open certificate']
)

navbar: Navbar = Navbar(
    description_list= [
        'Data Science Student',
        'Programmer Analyst',
        'Bachellor of Science of Engineering',
        'Mechanical Engineer',
        'Wandering soul'
    ]
)

about: About = About(
    description_list = [
        '''I graduated as a Mechanical Engineer in 2014 and worked in that field for 2 years. 
        After living abroad for a while, I decided to change course and pursue my true passion: 
        programming. From my days as a MATLAB assistant during my engineering studies to my robotics 
        thesis project and learning VBA programming for Excel while working, I've always been involved 
        in the world of programming.''',

        '''During my studies as a Programmer Analyst, I started working as a web developer 
        and have continued in this field to this day. I've learned to use various frameworks 
        like React and Svelte, but my main focus now is specializing in Python. In fact, this website 
        was developed using the Reflex framework.''',
        
        '''Currently, I'm immersed in a Data Science bootcamp, which reflects my strong 
        interest in this area. I enjoy exploring and analyzing data to understand the stories they tell. 
        My goal is to merge my programming skills with advanced data analysis techniques to tackle 
        complex challenges in innovative ways.''',
        
        '''In addition to programming and Data Science, I'm passionate about traveling, fantasy books, 
        board games, and role-playing games.'''
    ]
)

work_experience: List[WorkExperienceCard] = [
    WorkExperienceCard(
        icon='crecic.jpg',
        company='Crecic S.A.',
        date_from='Jan-2023',
        date_to='Present',
        position='Analista Programador',
        location='Concepcion, Chile',
        website='https://www.crecic.cl',
        description=[
            '''
            Currently, I am part of the customer support team, resolving issues with the SGM 
            (Sistema de Gestión Municipal) platform in production, and also part of the development team, 
            designing a new version of it using current technologies and in compliance with new regulations
            '''
        ],
        skills=['Javascript', 'PHP', 'Svelte', 'Gitlab', 'Express','HTML', 'CSS'],
    ),
    WorkExperienceCard(
        icon='ccu.jpg',
        company='Cervecera CCU S.A.',
        date_from='May-2016',
        date_to='Jan-2018',
        position='Process Engineer',
        location='Temuco, Chile',
        website='https://www.ccu.cl',
        description=[
            '''
            I was responsible for mechanical maintenance in the Production area, 
            focusing on managing predictive/preventive maintenance activities, 
            spare parts management, and leading continuous improvement initiatives.
            '''
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
            '''
            My main task was to collect data from critical equipment within the production 
            area, and subsequently create a preventive maintenance plan based on lubrication 
            and temperature analysis of the equipment.
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
        title='Technical Programmer Analyst',
        institution='Instituto Profesional Virginio Gomez, Concepción, Chile',
        status='Graduated'
    ),
    EducationExperience(
        year_start=2008,
        year_end=2014,
        icon='udec.jpg',
        title='Mechanical Engineering',
        institution='Universidad de Concepción, Concepción, Chile',
        other_title='Thesis',
        other='''""Construction of an Inverted Pendulum and Implementation of a 
        Microcontroller-Based Control System for its Vertical Positioning"''',
        status='Graduated'
    ),
    EducationExperience(
        year_start=2008,
        year_end=2013,
        icon='udec.jpg',
        title='Bachelor of Science in Engineering',
        institution='Universidad de Concepción, Concepción, Chile',
        status='Graduated'
    ),
]

other_studies: List[EducationExperience] = [
    EducationExperience(
        year_start=2024,
        year_end=2024,
        icon='tripleten.png',
        title='Bootcamp on Data Science',
        institution='TripleTen',
        status='In progress'
    ),
    EducationExperience(
        year_start=2023,
        year_end=2023,
        icon='alura.png',
        title='Frontend Training in React',
        institution='Alura Latam',
        link_title='Certificate',
        link='https://app.aluracursos.com/degree/certificate/17ee41c9-a847-4fdf-837e-7127320245da',
        status='Completed'
    ),
    EducationExperience(
        year_start=2023,
        year_end=2023,
        icon='udemy.png',
        title='Bootcamp on Web development with Node.js',
        institution='Udemy',
        other_title='Additional information',
        other='''43-hour course, both theoretical and practical, led by Juan Pablo de la Torre''',
        link_title='Certificate',
        link='https://www.udemy.com/certificate/UC-27fef825-1369-4e27-8eb3-78e2b924a604/',
        status='Completed'
    ),
    EducationExperience(
        year_start=2023,
        year_end=2023,
        icon='udemy.png',
        title='Modern JavaScript Definitive Guide',
        institution='Udemy',
        other_title='Additional information',
        other='''52-hour course, both theoretical and practical, led by Juan Pablo de la Torre''',
        link_title='Certificate',
        link='https://www.udemy.com/certificate/UC-c37656db-ea03-4a48-b74c-a3efab69fcae/',
        status='Completed'
    ),
]

projects: List[Project] = [
    Project(
        title='My Portfolio',
        date='06/2024',
        description='My personal website with my projects (the page you are currently on)',
        technologies=['Python','Reflex'],
        link='https://jcardoso.reflex.run/',
        img='jcardoso.png',
        repository='https://github.com/joaquincardosorios/jcardoso_website'
    ),
    Project(
        title='Sentiment Analysis, ML applied to texts',
        date='05/2024',
        description='This repository contains a Python project that trains various machine learning models to classify movie reviews as positive or negative. The models are based on natural language processing techniques.',
        technologies=['Python','Pandas', 'Numpy','Matplotlib', 'Seaborn', 'tqdm', 'Scikit-learn', 'NLTK', 'Spacy', 'LightGBM'],
        img='not_image.png',
        repository='https://github.com/joaquincardosorios/jcardoso_website'
    ),
    Project(
        title='ML Analysis of case with Time Series',
        date='05/2024',
        description='Analysis and model training are conducted to predict the number of taxis required by a fleet at an airport',
        technologies=['Python','Pandas', 'Numpy', 'Scikit-learn', 'Catboost', 'LightGBM'],
        img='not_image.png',
        repository='https://github.com/joaquincardosorios/jcardoso_website'
    ),
    Project(
        title='PG Estudio',
        date='08/2023',
        description='Website for wallpaper catalog',
        technologies=['HTML', 'React', 'Tailwind', 'Vercel'],
        link='https://pg-estudio.vercel.app/',
        img='pg_estudio.png'
    ),
]