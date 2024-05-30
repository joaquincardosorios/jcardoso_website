import reflex as rx
from jcardoso.styles.styles import header_style, header_links_style
import jcardoso.constants as constants
from jcardoso.components.header_title import header_title
from jcardoso.components.link_icon import link_icon
from jcardoso.components.navbar_menu_item import navbar_menu_item
from jcardoso.components.footer import footer

from jcardoso.states.GlobalState import GlobalState
from jcardoso.translations import en, es
from typing import List
from jcardoso.bases.bases import Labels


def sidebar(items_menu: List[List[str]] ) -> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_title(),
            rx.hstack(
                link_icon(constants.LINKEDIN_URL, 'linkedin'),
                link_icon(constants.GITHUB_URL, 'github'),
                link_icon(constants.EMAIL_URL, 'email'),
                spacing='4',
                style=header_links_style
            ),
            rx.desktop_only(
                rx.tabs.root(
                    rx.tabs.list(
                        rx.foreach(
                            items_menu,
                            lambda item: (navbar_menu_item(item[1], item[0]))
                        )
                        # navbar_menu_item('Sobre mi', "about"),
                        # navbar_menu_item('Laboral', "laboral"),
                        # navbar_menu_item('Estudios', 'estudios'),
                        # navbar_menu_item('Proyectos', "proyectos"),
                        # navbar_menu_item('Otros', "otros"),
                    ),
                    default_value="about",
                    orientation='vertical',
                ),
                
            ),
            
        ),
        footer(),
        style=header_style,
        justify='between'
    )

