import reflex as rx
from typing import List, Dict

class ColorSkill(rx.State):
    badge_colors: Dict[str, List[str]] = {
        'python':['#306998','#FFFFFF'],
        'js':['#F7DF1E','#000000'],
        'java':['#007396', '#FFFFFF'],
        'svelte':['#FF3E00', '#FFFFFF'],
        'react':['#61DAFB','#000000'],
        'postgressql':['#FFCC00','#000000'],
        'php':['#4F5B93','#FFFFFF'],
        'express':['#000000','#FFFFFF'],
        'figma':['#0ACF83','#FFFFFF'],
        'linkedin':['#0A66C2','#FFFFFF'],
        'github':['#181717','#FFFFFF'],
        'email':['#DB4437','#FFFFFF'],
        'normal':['#DB4437','#FFFFFF'],
    }
    background: Dict[str, str] = {
        'python':'#306998',
        'js':'#F7DF1E',
        'java':'#007396',
        'svelte':'#FF3E00',
        'react':'#61DAFB',
        'postgressql':'#FFCC00',
        'php':'#4F5B93',
        'express':'#000000',
        'figma':'#0ACF83',
        'linkedin':'#0A66C2',
        'github':'#181717',
        'email':'#DB4437',
        
    }

    text: Dict[str, str] = {
        'python':'#FFFFFF',
        'js':'#000000',
        'java':'#FFFFFF',
        'svelte':'#FFFFFF',
        'react':'#000000',
        'postgressql':'#000000',
        'php':'#FFFFFF',
        'express':'#FFFFFF',
        'figma':'#FFFFFF',
    }
