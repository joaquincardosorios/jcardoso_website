import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font


# Sizes
class Size(Enum):
    ZERO= '0px !important'
    SMALL='0.5em'
    MEDIUM='0.8em'
    DEFAULT='1em'
    LARGE='1.5em'
    BIG='2em'
    BIGGER='3em'
    HUGE='4em'

# Style

BASE_STYLE = {
    'background_color' : Color.BACKGROUND.value,
    'color' : TextColor.BODY.value,
    'font-family' : Font.DEFAULT.value,
    'font_weight':'300',
    'scroll_behavior': 'smooth',

}

container_style = dict(
    height= ['100%','100%','100%', '100vh','100vh'],
    margin_x= 'auto',
    max_width= '1124px',
    padding_x=Size.LARGE.value
)

flex_container_style = dict(
    flex_direction=['column','column','column','row','row']
)

header_style = dict(
    padding_y = Size.HUGE.value,
    width=['100%','100%','100%','45%','45%'],
    align_items=['center','center','center','start','start',],
)

header_tags_style = dict(
    font_weight= 'normal',
    text_align=['center','center','center','start','start',]
)

header_links_style = dict(
    justify='center',
)

main_style = dict(
    padding_y = [Size.DEFAULT.value,Size.DEFAULT.value,Size.DEFAULT.value,Size.ZERO.value,Size.ZERO.value],
    padding_right = [0,0,0,Size.DEFAULT.value,Size.DEFAULT.value], 
    width=['100%','100%','100%','55%','55%'],
    height=['100%','100%','100%', '100vh','100vh']
)

title_card_styles = dict(
    font_weight = 'bold',
    scroll_margin_top = Size.HUGE.value
)

header_title_styles = dict(
    color=Color.SECODARY.value,
    font_size=Size.BIGGER.value,
    font_family=Font.LOGO.value,
)

icons_style = dict(
    width=[Size.BIG.value, Size.BIG.value, Size.BIG.value, Size.LARGE.value, Size.LARGE.value],
    height='auto',
)

summary_style = dict(
    text_align='justify',
    padding_x='5px',
    padding_top = Size.HUGE.value
)

summary_content_style = dict(
    padding_x = Size.BIG.value,
)

work_card_style = dict(
    width='100%',
    padding = Size.BIG.value,
    border_radius = '15px',
    transition= 'background-color 0.5s ease',
    font_size = Size.MEDIUM.value,
    _hover = {
        'background_color' : Color.CONTENT.value,
        'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.3), 0 6px 20px rgba(0, 0, 0, 0.19)'
    }
)


## Estilos de badges

python_style = dict(
    background_color= '#306998',
    color= '#FFFFFF',
)
javascript_style = dict(
    background_color= '#F7DF1E',
    color= '#000000',
)
java_style = dict(
    background_color= '#007396',
    color= '#FFFFFF',
)
svelte_style = dict(
    background_color= '#FF3E00',
    color= '#FFFFFF',
)
react_style = dict(
    background_color= '#61DAFB',
    color= '#000000',
)
sql_style = dict(
    background_color= '#FFCC00',
    color= '#000000',
)
