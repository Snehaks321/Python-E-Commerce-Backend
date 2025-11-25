import reflex as rx
from app.states.auth_state import AuthState
from app.components.navbar import navbar
from app.components.footer import footer


def order_row(order: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            order["id"],
            class_name="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6",
        ),
        rx.el.td(
            order["date"],
            class_name="whitespace-nowrap px-3 py-4 text-sm text-gray-500",
        ),
        rx.el.td(
            f"${order['total']:.2f}",
            class_name="whitespace-nowrap px-3 py-4 text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.span(
                order["status"],
                class_name=rx.cond(
                    order["status"] == "Delivered",
                    "inline-flex rounded-full bg-green-100 px-2 text-xs font-semibold leading-5 text-green-800",
                    "inline-flex rounded-full bg-yellow-100 px-2 text-xs font-semibold leading-5 text-yellow-800",
                ),
            ),
            class_name="whitespace-nowrap px-3 py-4 text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.a("View", href="#", class_name="text-blue-600 hover:text-blue-900"),
            class_name="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6",
        ),
    )


def profile_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.cond(
                AuthState.is_authenticated,
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.h1(
                                "My Account",
                                class_name="text-2xl font-bold text-gray-900",
                            ),
                            rx.el.button(
                                "Sign Out",
                                on_click=AuthState.logout,
                                class_name="text-sm font-medium text-red-600 hover:text-red-500",
                            ),
                            class_name="flex items-center justify-between mb-8",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.h2(
                                    "Profile Information",
                                    class_name="text-lg font-medium text-gray-900 mb-4",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.p(
                                            "Name",
                                            class_name="text-sm font-medium text-gray-500",
                                        ),
                                        rx.el.p(
                                            AuthState.user["name"],
                                            class_name="mt-1 text-sm text-gray-900",
                                        ),
                                        class_name="mb-4",
                                    ),
                                    rx.el.div(
                                        rx.el.p(
                                            "Email",
                                            class_name="text-sm font-medium text-gray-500",
                                        ),
                                        rx.el.p(
                                            AuthState.user["email"],
                                            class_name="mt-1 text-sm text-gray-900",
                                        ),
                                        class_name="mb-4",
                                    ),
                                    class_name="bg-white shadow rounded-lg p-6 mb-8",
                                ),
                            ),
                            rx.el.div(
                                rx.el.h2(
                                    "Order History",
                                    class_name="text-lg font-medium text-gray-900 mb-4",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.table(
                                            rx.el.thead(
                                                rx.el.tr(
                                                    rx.el.th(
                                                        "Order ID",
                                                        class_name="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6",
                                                    ),
                                                    rx.el.th(
                                                        "Date",
                                                        class_name="px-3 py-3.5 text-left text-sm font-semibold text-gray-900",
                                                    ),
                                                    rx.el.th(
                                                        "Total",
                                                        class_name="px-3 py-3.5 text-left text-sm font-semibold text-gray-900",
                                                    ),
                                                    rx.el.th(
                                                        "Status",
                                                        class_name="px-3 py-3.5 text-left text-sm font-semibold text-gray-900",
                                                    ),
                                                    rx.el.th(
                                                        "",
                                                        class_name="relative py-3.5 pl-3 pr-4 sm:pr-6",
                                                    ),
                                                ),
                                                class_name="bg-gray-50",
                                            ),
                                            rx.el.tbody(
                                                rx.foreach(
                                                    AuthState.user["orders"], order_row
                                                ),
                                                class_name="divide-y divide-gray-200 bg-white",
                                            ),
                                            class_name="min-w-full divide-y divide-gray-300",
                                        ),
                                        class_name="overflow-hidden shadow ring-1 ring-black ring-opacity-5 sm:rounded-lg",
                                    ),
                                    class_name="inline-block min-w-full align-middle",
                                ),
                            ),
                        ),
                    ),
                    class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
                ),
                rx.el.div(
                    rx.el.h2("Please log in to view your profile"),
                    rx.el.a(
                        "Log In",
                        href="/login",
                        class_name="text-blue-600 hover:text-blue-500 mt-4 inline-block",
                    ),
                    class_name="flex flex-col items-center justify-center h-96",
                ),
            ),
            class_name="pt-20 min-h-screen bg-white",
        ),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col",
    )