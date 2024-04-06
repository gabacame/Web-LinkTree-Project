import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="GB", variant="solid", size="7"),
        rx.text("@gabacame"),
        rx.text("Hola mi nombre es Guillermo Alvarez"),
        rx.text("""Este es un clone de linktree hecho 
                con el framework de REFLEX con Python puro""")

    )