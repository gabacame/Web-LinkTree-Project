import reflex as rx
from Web_LinkTree_Project.components.navbar import navbar
from Web_LinkTree_Project.components.footer import footer
from Web_LinkTree_Project.views.header.header import header
from Web_LinkTree_Project.views.links.links import links

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack( 
        navbar(),
        header(),
        links(),
        footer()
    )

app = rx.App()
app.add_page(index)