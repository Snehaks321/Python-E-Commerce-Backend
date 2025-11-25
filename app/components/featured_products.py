import reflex as rx
from app.states.shop_state import ShopState
from app.components.product_card import product_card


def featured_products() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Featured Collection",
                    class_name="text-2xl sm:text-3xl font-bold text-gray-900",
                ),
                rx.el.a(
                    rx.el.span("View All Products"),
                    rx.icon("arrow-right", class_name="w-4 h-4 ml-2 stroke-gray-900"),
                    href="#",
                    class_name="flex items-center text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors",
                ),
                class_name="flex justify-between items-end mb-10",
            ),
            rx.el.div(
                rx.foreach(ShopState.featured_products, product_card),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-x-8 gap-y-12",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="py-20 bg-white",
    )