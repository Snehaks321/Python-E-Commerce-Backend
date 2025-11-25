import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.hero import hero
from app.components.featured_products import featured_products
from app.pages.product_list import men_page, women_page, new_arrivals_page, sale_page
from app.pages.product_detail import product_detail
from app.pages.cart import cart_page
from app.pages.auth import login_page, signup_page
from app.pages.profile import profile_page
from app.pages.checkout import checkout_page
from app.pages.admin import admin_dashboard


def index() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(hero(), featured_products(), class_name="pt-20"),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(men_page, route="/men")
app.add_page(women_page, route="/women")
app.add_page(product_detail, route="/product/[id]")
app.add_page(cart_page, route="/cart")
app.add_page(new_arrivals_page, route="/new-arrivals")
app.add_page(sale_page, route="/sale")
app.add_page(login_page, route="/login")
app.add_page(signup_page, route="/signup")
app.add_page(profile_page, route="/profile")
app.add_page(checkout_page, route="/checkout")
app.add_page(admin_dashboard, route="/admin")