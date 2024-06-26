import reflex as rx
from typing import List
from jcardoso.bases.bases import VideoCard
from jcardoso.styles.styles import other_card_style

def video_card(video: VideoCard) -> rx.Component:
    return rx.box(
        rx.dialog.root(
            rx.text(video.title, text_align='center'),
            rx.dialog.trigger(
                rx.flex(
                    rx.image(
                        src=f'others/engineering/{video.img}', 
                        max_height='180px', 
                        margin_x='auto', 
                    ),
                    rx.image(
                        src='icons/play.png',
                        width='50px',
                        height='50px',
                        style={
                            "position": "absolute", 
                            "top": "50%", 
                            "left": "50%", 
                            "transform": "translate(-50%, -50%)",
                            'transition':"transform 0.3s ease-in-out",
                        },
                        
                    ),
                    position="relative",
                    style=other_card_style,
                ),
            ),
            rx.dialog.content(
                rx.video(
                    url=video.link,
                    width='auto',
                    height='80vh'
                )
            )
        ),
    )
