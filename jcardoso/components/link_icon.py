import reflex as rx
import jcardoso.styles.styles as styles

def link_icon(url:str, img:str) -> rx.Component:
    return rx.link(
        rx.image(src=f'icons/{img}.svg', style=styles.icons_style),
        href=url,
        is_external=True,
    )