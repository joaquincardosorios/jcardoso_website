import reflex as rx

import jcardoso.constants as constants
from jcardoso.styles.sidebar import header_style, header_links_style
from jcardoso.components.header_title import header_title
from jcardoso.components.link_icon import link_icon
from jcardoso.components.navbar_menu_item import navbar_menu_item
from jcardoso.components.language_switch import language_switch
from jcardoso.components.footer import footer

from jcardoso.states.GlobalState import GlobalState

def sidebar() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_title(),
            rx.flex(
                rx.hstack(
                    link_icon(constants.LINKEDIN_URL, 'linkedin'),
                    link_icon(constants.GITHUB_URL, 'github'),
                    link_icon(constants.EMAIL_URL, 'email'),
                    spacing='4',
                    style=header_links_style,
                ),
                rx.desktop_only(
                    language_switch(),
                ),
                justify='between',
                width='100%',
            ),
            rx.desktop_only(
                rx.tabs.root(
                    rx.tabs.list(
                        rx.foreach(
                            GlobalState.labels.items_menu,
                            lambda item: (navbar_menu_item(item[1], item[0]))
                        ),
                        justify_content='start',
                    ),
                    default_value="about",
                    orientation='horizontal',
                ),
                align_self='center',
            ),  
            width='100%'
        ),
        rx.desktop_only(
            footer(),
            width='100%'
        ),
        style=header_style,
        justify='between'
    )

