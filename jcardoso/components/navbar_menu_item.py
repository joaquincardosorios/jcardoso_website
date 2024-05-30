import reflex as rx
import jcardoso.styles.styles as styles
from jcardoso.styles.colors import TextColor as TextColor


def navbar_menu_item(name: str, reference:str)-> rx.Component:
    return rx.tabs.trigger(
        name,
        color=TextColor.BODY,
        on_click=lambda: scroll_to_element(reference),
        value=reference
    )

def scroll_to_element(element_id: str):
    return rx.call_script(f"scrollToElement({element_id})")