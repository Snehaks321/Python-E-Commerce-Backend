import reflex as rx
from app.states.shop_state import ShopState
from app.states.cart_state import CartState
from app.components.navbar import navbar
from app.components.footer import footer


def thumbnail_image(url: str, index: int) -> rx.Component:
    return rx.el.button(
        rx.image(src=url, class_name="w-full h-full object-cover"),
        on_click=lambda: ShopState.select_image(index),
        class_name=rx.cond(
            ShopState.selected_image_index == index,
            "relative aspect-square overflow-hidden rounded-md ring-2 ring-gray-900",
            "relative aspect-square overflow-hidden rounded-md hover:ring-2 hover:ring-gray-300 transition-all",
        ),
    )


def size_selector() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span("Size", class_name="text-sm font-medium text-gray-900"),
            rx.el.a(
                "Size Guide",
                href="#",
                class_name="text-sm font-medium text-blue-600 hover:text-blue-500",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.div(
            rx.foreach(
                ShopState.current_product["sizes"],
                lambda size: rx.el.button(
                    size,
                    on_click=lambda: ShopState.select_size(size),
                    class_name=rx.cond(
                        ShopState.selected_size == size,
                        "border-gray-900 bg-gray-900 text-white py-3 px-4 border rounded-md text-sm font-medium hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900",
                        "border-gray-200 bg-white text-gray-900 py-3 px-4 border rounded-md text-sm font-medium hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900",
                    ),
                ),
            ),
            class_name="grid grid-cols-4 gap-4 sm:grid-cols-8 lg:grid-cols-4",
        ),
    )


def color_selector() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Color", class_name="text-sm font-medium text-gray-900 mb-4"),
        rx.el.div(
            rx.foreach(
                ShopState.current_product["colors"],
                lambda color: rx.el.button(
                    rx.el.span(color, class_name="sr-only"),
                    rx.el.span(
                        class_name="h-8 w-8 rounded-full border border-black border-opacity-10",
                        style={
                            "backgroundColor": rx.cond(
                                color == "White",
                                "#ffffff",
                                rx.cond(color == "Black", "#000000", "gray"),
                            )
                        },
                    ),
                    title=color,
                    on_click=lambda: ShopState.select_color(color),
                    class_name=rx.cond(
                        ShopState.selected_color == color,
                        "relative -m-0.5 flex cursor-pointer items-center justify-center rounded-full p-0.5 ring-gray-900 ring-2",
                        "relative -m-0.5 flex cursor-pointer items-center justify-center rounded-full p-0.5 ring-transparent hover:ring-gray-300",
                    ),
                ),
            ),
            class_name="flex items-center space-x-3",
        ),
    )


def product_detail() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.cond(
                    ShopState.current_product,
                    rx.el.div(
                        rx.el.nav(
                            rx.el.ol(
                                rx.el.li(
                                    rx.el.div(
                                        rx.el.a(
                                            "Home",
                                            href="/",
                                            class_name="mr-2 text-sm font-medium text-gray-900 hover:text-gray-700",
                                        ),
                                        rx.icon(
                                            "chevron-right",
                                            class_name="h-4 w-4 text-gray-400",
                                        ),
                                    ),
                                    class_name="flex items-center",
                                ),
                                rx.el.li(
                                    rx.el.div(
                                        rx.el.a(
                                            ShopState.current_product["category"],
                                            href=rx.cond(
                                                ShopState.current_product["category"]
                                                == "Men",
                                                "/men",
                                                "/women",
                                            ),
                                            class_name="mr-2 text-sm font-medium text-gray-900 hover:text-gray-700 ml-2",
                                        ),
                                        rx.icon(
                                            "chevron-right",
                                            class_name="h-4 w-4 text-gray-400",
                                        ),
                                    ),
                                    class_name="flex items-center",
                                ),
                                rx.el.li(
                                    rx.el.span(
                                        ShopState.current_product["name"],
                                        class_name="ml-2 text-sm font-medium text-gray-500",
                                    ),
                                    class_name="flex items-center",
                                ),
                                class_name="flex items-center space-x-2",
                            ),
                            class_name="py-4 mb-8",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.div(
                                    rx.image(
                                        src=ShopState.current_product["images"][
                                            ShopState.selected_image_index
                                        ],
                                        class_name="w-full h-full object-cover object-center rounded-lg",
                                    ),
                                    class_name="aspect-square w-full overflow-hidden rounded-lg bg-gray-100 mb-4",
                                ),
                                rx.el.div(
                                    rx.foreach(
                                        ShopState.current_product["images"],
                                        lambda url, i: thumbnail_image(url, i),
                                    ),
                                    class_name="grid grid-cols-4 gap-4",
                                ),
                                class_name="flex flex-col",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.h1(
                                        ShopState.current_product["name"],
                                        class_name="text-3xl font-bold tracking-tight text-gray-900 mb-3",
                                    ),
                                    rx.el.div(
                                        rx.el.p(
                                            f"${ShopState.current_product['price']:.2f}",
                                            class_name="text-2xl tracking-tight text-gray-900",
                                        ),
                                        rx.el.div(
                                            rx.el.div(
                                                rx.foreach(
                                                    rx.Var.range(5),
                                                    lambda i: rx.icon(
                                                        "star",
                                                        class_name=rx.cond(
                                                            i
                                                            < ShopState.current_product[
                                                                "rating"
                                                            ],
                                                            "text-yellow-400 fill-yellow-400 h-5 w-5",
                                                            "text-gray-200 fill-gray-200 h-5 w-5",
                                                        ),
                                                    ),
                                                ),
                                                class_name="flex items-center",
                                            ),
                                            rx.el.span(
                                                f"{ShopState.current_product['reviews']} reviews",
                                                class_name="ml-3 text-sm font-medium text-blue-600 hover:text-blue-500",
                                            ),
                                            class_name="flex items-center ml-4 border-l border-gray-300 pl-4",
                                        ),
                                        class_name="flex items-center mt-2 mb-6",
                                    ),
                                    rx.el.div(
                                        rx.el.h3("Description", class_name="sr-only"),
                                        rx.el.p(
                                            ShopState.current_product["description"],
                                            class_name="text-base text-gray-700 leading-relaxed",
                                        ),
                                        class_name="mb-8",
                                    ),
                                ),
                                rx.el.div(color_selector(), class_name="mb-8"),
                                rx.el.div(size_selector(), class_name="mb-10"),
                                rx.el.button(
                                    "Add to Cart",
                                    on_click=lambda: CartState.add_to_cart(
                                        ShopState.current_product
                                    ),
                                    class_name="flex w-full items-center justify-center rounded-md border border-transparent bg-blue-600 px-8 py-4 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 mb-4",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.icon(
                                            "truck",
                                            class_name="h-5 w-5 text-gray-400 mr-2",
                                        ),
                                        rx.el.span(
                                            "Free shipping on orders over $100",
                                            class_name="text-sm text-gray-500",
                                        ),
                                        class_name="flex items-center",
                                    ),
                                    rx.el.div(
                                        rx.icon(
                                            "shield-check",
                                            class_name="h-5 w-5 text-gray-400 mr-2",
                                        ),
                                        rx.el.span(
                                            "2-year warranty included",
                                            class_name="text-sm text-gray-500",
                                        ),
                                        class_name="flex items-center",
                                    ),
                                    class_name="flex flex-col gap-2 mt-6 pt-6 border-t border-gray-200",
                                ),
                                class_name="mt-10 lg:mt-0 lg:col-start-2",
                            ),
                            class_name="grid grid-cols-1 gap-x-8 gap-y-10 lg:grid-cols-2",
                        ),
                    ),
                    rx.el.div(
                        rx.spinner(),
                        rx.el.p(
                            "Loading product details...",
                            class_name="mt-4 text-gray-500",
                        ),
                        class_name="flex flex-col items-center justify-center min-h-[50vh]",
                    ),
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8",
            ),
            class_name="pt-20 min-h-screen bg-white",
        ),
        footer(),
        on_mount=ShopState.reset_product_state,
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col",
    )