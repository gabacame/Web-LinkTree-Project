import reflex as rx
from Web_LinkTree_Project.components.navbar import navbar
from Web_LinkTree_Project.components.footer import footer
from Web_LinkTree_Project.views.header.header import header
from Web_LinkTree_Project.views.links.links import links
from Web_LinkTree_Project.styles import styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack( 
                header(),
                links(),
                max_width=styles.MAX_WIDTH,  
                width="100%",
                margin_y=styles.Size.DEFAULT.value
            )
        ),
        footer()
    )

app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)