from .colors import Color as Color
from .colors import TextColor as TextColor
from .sizes import Size

shadow = '0 4px 8px rgba(0, 0, 0, 0.3), 0 6px 20px rgba(0, 0, 0, 0.19)'

work_card_style = dict(
    width='100%',
    padding = [Size.MEDIUM.value, Size.MEDIUM.value, Size.MEDIUM.value, Size.BIG.value, Size.BIG.value],
    border_radius = '15px',
    transition= 'background-color 0.5s ease',
    font_size = [Size.DEFAULT.value,Size.DEFAULT.value,Size.DEFAULT.value,Size.MEDIUM.value,Size.MEDIUM.value],
    flexDirection = ['column', 'column', 'column', 'row', 'row', ],
    background_color = [Color.CONTENT.value, Color.CONTENT.value, Color.CONTENT.value, Color.BACKGROUND.value, Color.BACKGROUND.value],
    box_shadow= '0 4px 8px rgba(0, 0, 0, 0.3), 0 6px 20px rgba(0, 0, 0, 0.19)',
    gap=['4px','4px','4px','12px','12px'],
    _hover = {
        'background_color' : Color.CONTENT.value,
    }
)

work_card_date = dict(
    width=['100%', '100%', '100%', '20%','20%'],
    text_align=['start', 'start', 'start', 'center', 'center']
)

work_card_body = dict(
    width=['100%', '100%', '100%', '80%','80%'],
)