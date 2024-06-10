from jcardoso.bases.bases import Labels, Navbar, About, WorkExperienceCard, EducationExperience
from typing import List

labels: Labels = Labels(
    items_menu =[
        ['about', 'About me', 'A little about me'], 
        ['work_experience', 'Experience', 'Work Experience'], 
        ['education','Education','Education'], 
        ['projects' , 'Projects','My projects'], 
        ['others','Others']
    ],
    work_card=['Position', 'Job description', 'Skills']
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
        '''I graduated as a Mechanical Engineer in 2014 and worked as such for 2 years.
        After a couple of years living abroad, I decided to make a change in my life
        and studied what truly fascinates me: Programming. It always called to me,
        from assisting with Matlab while studying engineering, my thesis related to robotics,
        to learning to program in VBA in Excel while working.''',

        '''While studying my Programmer Analyst degree, I started working as a web programmer and have been there ever since.
        I have learned to use various frameworks like React and Svelte, although I try to specialize in using Python.
        In fact, this site was created with the Reflex framework :P.''',
        
        '''I aim to specialize in Data Science, and that's it :P''',
        
        '''I enjoy traveling and role-playing games.'''
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
            'test solo 1 lalalalalal alalalal llaalal',
            'test 2 lalalal alalala lalalal'
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
        title='Technical Programmer Analyst',
        institution='Instituto Profesional Virginio Gomez, Concepción, Chile',
    ),
    EducationExperience(
        year_start=2008,
        year_end=2014,
        icon='udec.jpg',
        title='Mechanical Engineering',
        institution='Universidad de Concepción, Concepción, Chile',
        other_title='Thesis',
        other='''""Construction of an Inverted Pendulum and Implementation of a 
        Microcontroller-Based Control System for its Vertical Positioning"'''
    ),
    EducationExperience(
        year_start=2008,
        year_end=2013,
        icon='udec.jpg',
        title='Bachelor of Science in Engineering',
        institution='Universidad de Concepción, Concepción, Chile',
    ),
]