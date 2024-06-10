import reflex as rx

from jcardoso.styles.styles import badge_style

def custom_badge(name: str) -> rx.Component:
    return rx.badge(
        name,
        style=badge_style,
    )
