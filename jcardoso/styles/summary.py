from .colors import Color as Color
from .colors import TextColor as TextColor
from .sizes import Size

summary_style = dict(
    text_align='justify',
    padding_top =  [Size.DEFAULT.value, Size.DEFAULT.value, Size.DEFAULT.value, Size.HUGE.value, Size.HUGE.value]
)

summary_content_style = dict(
    padding_x = [Size.ZERO.value, Size.ZERO.value, Size.ZERO.value, Size.BIG.value, Size.BIG.value],
    font_size=Size.MEDIUM.value
)