import reflex as rx
from Web_LinkTree_Project.components.link_button import link_button


def links() -> rx.Component:
    return rx.center(
        rx.vstack(
            link_button("Linkedin", "https://www.linkedin.com/in/gabacame/"),
            link_button("Github", "https://github.com/gabacame"),
            width="100%",
            align="center",
            as_="div"
        )
    )   