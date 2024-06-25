import reflex as rx

from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .sizes import Size

from .main import *
from .summary import *
from .sidebar import *
from .education import *
from .work_experience import *
from .projects import *


# Style

BASE_STYLE = {
    'background_color' : Color.BACKGROUND.value,
    'color' : TextColor.BODY.value,
    'font_family' : Font.DEFAULT.value,
    'font_weight':'300',
    'scroll_behavior': 'smooth',
    
    rx.link: {
        'color' : Color.SECODARY.value
    }

}

container_style = dict(
    height= '100%',
    margin_x= 'auto',
    max_width= '1124px',
    padding_x=Size.LARGE.value
)

flex_container_style = dict(
    flex_direction=['column','column','column','row','row'],
)

title_section_styles = dict(
    scroll_margin_top = Size.HUGE.value
)

title_card_style = dict(
    font_size='1.2em',
    line_height='1.1em'
)

icons_style = dict(
    width=[Size.BIG.value, Size.BIG.value, Size.BIG.value, Size.LARGE.value, Size.LARGE.value],
    height='auto',
)


badge_style = dict(
    backgroundColor=Color.SECODARY.value,
    color=Color.BACKGROUND.value
)