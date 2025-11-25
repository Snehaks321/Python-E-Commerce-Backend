import reflex as rx
from app.states.shop_state import ShopState
from app.states.cart_state import CartState
from app.states.auth_state import AuthState


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.el.a(
        text,
        href=url,
        class_name="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors duration-200",
    )


def search_result_item(product: dict) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.image(
                src=product["image_url"], class_name="h-12 w-12 rounded object-cover"
            ),
            rx.el.div(
                rx.el.p(
                    product["name"], class_name="text-sm font-medium text-gray-900"
                ),
                rx.el.p(f"${product['price']:.2f}", class_name="text-sm text-gray-500"),
                class_name="ml-3",
            ),
            class_name="flex items-center",
        ),
        href=f"/product/{product['id']}",
        on_click=ShopState.toggle_search,
        class_name="block py-2 hover:bg-gray-50 rounded-md transition-colors",
    )


def search_modal() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "search",
                        class_name="pointer-events-none absolute inset-y-0 left-0 h-full w-5 text-gray-400 ml-3",
                    ),
                    rx.el.input(
                        placeholder="Search products...",
                        on_change=ShopState.set_search_query,
                        auto_focus=True,
                        class_name="block w-full rounded-md border-0 py-4 pl-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6",
                        default_value=ShopState.search_query,
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="h-5 w-5 text-gray-500"),
                        on_click=ShopState.toggle_search,
                        class_name="absolute inset-y-0 right-0 flex items-center pr-3 cursor-pointer",
                    ),
                    class_name="relative",
                ),
                rx.cond(
                    ShopState.search_query != "",
                    rx.el.div(
                        rx.cond(
                            ShopState.search_results.length() > 0,
                            rx.el.div(
                                rx.el.p(
                                    "Products",
                                    class_name="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2",
                                ),
                                rx.el.div(
                                    rx.foreach(
                                        ShopState.search_results, search_result_item
                                    ),
                                    class_name="space-y-1",
                                ),
                                class_name="max-h-96 overflow-y-auto py-4",
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "No products found.",
                                    class_name="text-sm text-gray-500 text-center py-8",
                                )
                            ),
                        ),
                        class_name="mt-2",
                    ),
                    rx.fragment(),
                ),
                class_name="mx-auto max-w-2xl transform rounded-xl bg-white p-2 shadow-2xl ring-1 ring-black ring-opacity-5 transition-all",
            ),
            class_name="fixed inset-0 z-50 overflow-y-auto p-4 sm:p-6 md:p-20",
        ),
        rx.el.div(
            class_name="fixed inset-0 bg-gray-500 bg-opacity-25 transition-opacity z-40",
            on_click=ShopState.toggle_search,
        ),
        class_name="relative z-50",
    )


def mobile_nav_link(text: str, url: str) -> rx.Component:
    return rx.el.a(
        text,
        href=url,
        class_name="text-lg font-medium text-gray-800 py-3 border-b border-gray-100 w-full block hover:text-indigo-600 transition-colors",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.span(
                        "LUXE",
                        class_name="text-gray-900 font-bold tracking-tighter text-2xl",
                    ),
                    rx.el.span(
                        "WEAR",
                        class_name="text-gray-500 font-light tracking-widest text-2xl",
                    ),
                    href="/",
                    class_name="flex items-center gap-1",
                ),
                rx.el.div(
                    navbar_link("Men", "/men"),
                    navbar_link("Women", "/women"),
                    navbar_link("New Arrivals", "/new-arrivals"),
                    navbar_link("Sale", "/sale"),
                    class_name="hidden md:flex items-center gap-8",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon(
                            "search",
                            class_name="w-5 h-5 stroke-gray-600 hover:stroke-gray-900 transition-colors",
                        ),
                        on_click=ShopState.toggle_search,
                        class_name="p-2",
                    ),
                    rx.el.a(
                        rx.icon(
                            "user",
                            class_name="w-5 h-5 stroke-gray-600 hover:stroke-gray-900 transition-colors",
                        ),
                        href=rx.cond(AuthState.is_authenticated, "/profile", "/login"),
                        class_name="p-2",
                    ),
                    rx.el.a(
                        rx.el.div(
                            rx.icon(
                                "shopping-bag",
                                class_name="w-5 h-5 stroke-gray-600 hover:stroke-gray-900 transition-colors",
                            ),
                            rx.cond(
                                CartState.total_items > 0,
                                rx.el.span(
                                    CartState.total_items,
                                    class_name="absolute -top-1 -right-1 bg-black text-white text-[10px] font-bold h-4 w-4 rounded-full flex items-center justify-center",
                                ),
                                rx.fragment(),
                            ),
                            class_name="relative",
                        ),
                        href="/cart",
                        class_name="p-2",
                    ),
                    rx.el.button(
                        rx.icon("menu", class_name="w-6 h-6 stroke-gray-900"),
                        on_click=ShopState.toggle_mobile_menu,
                        class_name="md:hidden p-2 ml-2",
                    ),
                    class_name="flex items-center gap-2",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between",
            ),
            class_name="border-b border-gray-100 bg-white/90 backdrop-blur-md fixed top-0 left-0 right-0 z-50",
        ),
        rx.cond(
            ShopState.is_mobile_menu_open,
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.button(
                            rx.icon("x", class_name="w-6 h-6 stroke-gray-500"),
                            on_click=ShopState.toggle_mobile_menu,
                            class_name="absolute top-6 right-6 p-2",
                        ),
                        rx.el.div(
                            mobile_nav_link("Men", "/men"),
                            mobile_nav_link("Women", "/women"),
                            mobile_nav_link("New Arrivals", "/new-arrivals"),
                            mobile_nav_link("Sale", "/sale"),
                            mobile_nav_link(
                                "Account",
                                rx.cond(
                                    AuthState.is_authenticated, "/profile", "/login"
                                ),
                            ),
                            class_name="flex flex-col mt-16 px-6",
                        ),
                        class_name="bg-white h-full w-full sm:w-80 shadow-2xl transform transition-transform duration-300 ease-in-out",
                    ),
                    class_name="fixed inset-y-0 right-0 z-50 flex",
                ),
                rx.el.div(
                    on_click=ShopState.close_mobile_menu,
                    class_name="fixed inset-0 bg-black/30 backdrop-blur-sm z-40",
                ),
                class_name="relative z-50",
            ),
            rx.fragment(),
        ),
        rx.cond(ShopState.is_search_open, search_modal(), rx.fragment()),
    )