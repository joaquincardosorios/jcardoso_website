from .colors import Color as Color
from .colors import TextColor as TextColor
from .sizes import Size


other_card_style = dict(
    font_size = [Size.DEFAULT.value,Size.DEFAULT.value,Size.DEFAULT.value,Size.MEDIUM.value,Size.MEDIUM.value],
    background_color = [Color.CONTENT.value, Color.CONTENT.value, Color.CONTENT.value, Color.BACKGROUND.value, Color.BACKGROUND.value],
    padding = [Size.BIG.value, Size.BIG.value, Size.DEFAULT.value, Size.DEFAULT.value, Size.DEFAULT.value],
    width='100%',
    border_radius = '15px',
    transition= 'background-color 0.5s ease',
    flexDirection = ['column', 'column', 'column', 'row', 'row', ],
    box_shadow= '0 4px 8px rgba(0, 0, 0, 0.3), 0 6px 20px rgba(0, 0, 0, 0.19)',
    gap=['4px','4px','4px','12px','12px'],
    cursor='pointer',
    _hover = {
        'background_color' : Color.CONTENT.value,
        "& > img:last-of-type" :{
            "transform": "translate(-50%, -50%) scale(1.2)"
        }
    }
)