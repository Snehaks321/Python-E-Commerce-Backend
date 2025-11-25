import reflex as rx
from app.states.shop_state import ShopState
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.product_card import product_card
from app.components.filter_sidebar import filter_sidebar


def sort_dropdown() -> rx.Component:
    return rx.el.div(
        rx.el.label("Sort by:", class_name="text-sm text-gray-500 mr-2"),
        rx.el.select(
            rx.el.option("Featured", value="featured"),
            rx.el.option("Price: Low to High", value="price_asc"),
            rx.el.option("Price: High to Low", value="price_desc"),
            rx.el.option("Newest", value="newest"),
            rx.el.option("Popular", value="popular"),
            value=ShopState.sort_option,
            on_change=ShopState.set_sort_option,
            class_name="text-sm border-none focus:ring-0 text-gray-900 font-medium bg-transparent cursor-pointer p-0 pr-8",
        ),
        class_name="flex items-center",
    )


def product_list_template(category_title: str) -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        category_title, class_name="text-3xl font-bold text-gray-900"
                    ),
                    sort_dropdown(),
                    class_name="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-8 pb-6 border-b border-gray-200",
                ),
                rx.el.div(
                    filter_sidebar(),
                    rx.el.div(
                        rx.cond(
                            ShopState.filtered_products.length() > 0,
                            rx.el.div(
                                rx.foreach(ShopState.filtered_products, product_card),
                                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-8 gap-y-12",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "search",
                                    class_name="w-12 h-12 text-gray-300 mx-auto mb-4",
                                ),
                                rx.el.h3(
                                    "No products found",
                                    class_name="text-lg font-medium text-gray-900",
                                ),
                                rx.el.p(
                                    "Try adjusting your filters.",
                                    class_name="text-gray-500",
                                ),
                                class_name="text-center py-20 bg-gray-50 rounded-lg",
                            ),
                        ),
                        class_name="flex-1",
                    ),
                    class_name="flex flex-col md:flex-row gap-8 lg:gap-12",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8",
            ),
            class_name="pt-20 min-h-screen bg-white",
        ),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col",
    )


def men_page() -> rx.Component:
    return rx.el.div(
        product_list_template("Men's Collection"),
        on_mount=lambda: ShopState.set_category_filter("Men"),
    )


def women_page() -> rx.Component:
    return rx.el.div(
        product_list_template("Women's Collection"),
        on_mount=lambda: ShopState.set_category_filter("Women"),
    )


def new_arrivals_page() -> rx.Component:
    return rx.el.div(
        product_list_template("New Arrivals"),
        on_mount=ShopState.set_new_arrivals_filter,
    )


def sale_page() -> rx.Component:
    return rx.el.div(product_list_template("Sale"), on_mount=ShopState.set_sale_filter)