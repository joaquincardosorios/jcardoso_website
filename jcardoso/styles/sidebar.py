from .colors import Color as Color
from .colors import TextColor as TextColor
from .styles import Size
from .fonts import Font as Font

header_tags_style = dict(
    font_weight= 'normal',
    text_align=['center','center','center','start','start',]
)

header_title_styles = dict(
    color=Color.SECODARY.value,
    font_size=Size.BIGGER.value,
    font_family=Font.LOGO.value,
    text_align=['center', 'center', 'center', 'start', 'start', ]
)

space_style = dict(
    width=['100%','100%','100%','45%','45%'],
)

header_style = dict(
    position='sticky',
    top='0',
    left='0',
    padding_top = Size.HUGE.value,
    padding_bottom = [Size.DEFAULT.value, Size.DEFAULT.value, Size.DEFAULT.value, Size.HUGE.value, Size.HUGE.value],
    width='100%',
    height=['100%','100%','100%','100vh','100vh'],
    align_items=['center','center','center','start','start',],
)

header_links_style = dict(
    justify_content=['center', 'center', 'center','start', 'start'],
    width='100%'
)