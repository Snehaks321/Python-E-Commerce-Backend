import reflex as rx
from app.states.cart_state import CartState
from app.components.navbar import navbar
from app.components.footer import footer


def cart_item(item: dict, index: int) -> rx.Component:
    return rx.el.li(
        rx.el.div(
            rx.image(
                src=item["image_url"],
                alt=item["name"],
                class_name="h-24 w-24 rounded-md object-cover object-center sm:h-32 sm:w-32",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            rx.el.a(
                                item["name"],
                                href=f"/product/{item['id']}",
                                class_name="font-medium text-gray-700 hover:text-gray-800",
                            ),
                            class_name="text-base font-medium text-gray-900",
                        ),
                        rx.el.p(
                            f"Size: {item['size']} | Color: {item['color']}",
                            class_name="mt-1 text-sm text-gray-500",
                        ),
                        rx.el.p(
                            f"${item['price']:.2f}",
                            class_name="mt-1 text-sm font-medium text-gray-900",
                        ),
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.button(
                                rx.icon("minus", class_name="h-3 w-3"),
                                on_click=lambda: CartState.decrement_quantity(index),
                                class_name="p-1 text-gray-400 hover:text-gray-500",
                            ),
                            rx.el.span(
                                item["quantity"],
                                class_name="mx-2 text-sm text-gray-900 font-medium",
                            ),
                            rx.el.button(
                                rx.icon("plus", class_name="h-3 w-3"),
                                on_click=lambda: CartState.increment_quantity(index),
                                class_name="p-1 text-gray-400 hover:text-gray-500",
                            ),
                            class_name="flex items-center border border-gray-200 rounded-md px-2 py-1",
                        ),
                        rx.el.button(
                            rx.icon("trash", class_name="h-4 w-4"),
                            on_click=lambda: CartState.remove_item(index),
                            class_name="ml-4 text-sm font-medium text-red-600 hover:text-red-500 flex items-center gap-1",
                        ),
                        class_name="flex items-center justify-between sm:justify-end mt-4 sm:mt-0 gap-4",
                    ),
                    class_name="flex flex-1 flex-col justify-between sm:flex-row sm:items-start",
                ),
                class_name="ml-4 flex flex-1 flex-col sm:ml-6",
            ),
            class_name="flex py-6",
        ),
        class_name="flex py-6",
    )


def cart_summary() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2("Order summary", class_name="text-lg font-medium text-gray-900"),
            rx.el.dl(
                rx.el.div(
                    rx.el.dt("Subtotal", class_name="text-sm text-gray-600"),
                    rx.el.dd(
                        f"${CartState.subtotal:.2f}",
                        class_name="text-sm font-medium text-gray-900",
                    ),
                    class_name="flex items-center justify-between",
                ),
                rx.el.div(
                    rx.el.dt("Shipping estimate", class_name="text-sm text-gray-600"),
                    rx.el.dd("$5.00", class_name="text-sm font-medium text-gray-900"),
                    class_name="flex items-center justify-between pt-4 border-t border-gray-200",
                ),
                rx.el.div(
                    rx.el.dt("Tax estimate", class_name="text-sm text-gray-600"),
                    rx.el.dd(
                        f"${CartState.tax:.2f}",
                        class_name="text-sm font-medium text-gray-900",
                    ),
                    class_name="flex items-center justify-between pt-4 border-t border-gray-200",
                ),
                rx.el.div(
                    rx.el.dt(
                        "Order total", class_name="text-base font-medium text-gray-900"
                    ),
                    rx.el.dd(
                        f"${CartState.total_price + 5.0:.2f}",
                        class_name="text-base font-medium text-gray-900",
                    ),
                    class_name="flex items-center justify-between pt-4 border-t border-gray-200",
                ),
                class_name="mt-6 space-y-4",
            ),
            rx.el.div(
                rx.el.button(
                    "Checkout",
                    on_click=rx.redirect("/checkout"),
                    class_name="w-full rounded-md border border-transparent bg-blue-600 px-4 py-3 text-base font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-gray-50",
                ),
                class_name="mt-6",
            ),
            class_name="rounded-lg bg-gray-50 px-4 py-6 sm:p-6 lg:p-8",
        ),
        class_name="mt-16 rounded-lg bg-gray-50 px-4 py-6 sm:p-6 lg:col-span-5 lg:mt-0 lg:p-8",
    )


def cart_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Shopping Cart",
                    class_name="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl",
                ),
                rx.el.div(
                    rx.cond(
                        CartState.items.length() > 0,
                        rx.el.form(
                            rx.el.section(
                                rx.el.ul(
                                    rx.foreach(
                                        CartState.items,
                                        lambda item, i: cart_item(item, i),
                                    ),
                                    class_name="divide-y divide-gray-200 border-t border-b border-gray-200",
                                ),
                                class_name="lg:col-span-7",
                            ),
                            cart_summary(),
                            class_name="mt-12 lg:grid lg:grid-cols-12 lg:gap-x-12 lg:items-start",
                        ),
                        rx.el.div(
                            rx.icon(
                                "shopping-cart",
                                class_name="mx-auto h-12 w-12 text-gray-400",
                            ),
                            rx.el.h3(
                                "Your cart is empty",
                                class_name="mt-2 text-sm font-medium text-gray-900",
                            ),
                            rx.el.p(
                                "Start shopping to add items to your cart.",
                                class_name="mt-1 text-sm text-gray-500",
                            ),
                            rx.el.div(
                                rx.el.a(
                                    "Continue Shopping",
                                    href="/",
                                    class_name="inline-flex items-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2",
                                ),
                                class_name="mt-6",
                            ),
                            class_name="text-center py-24",
                        ),
                    ),
                    class_name="mt-12",
                ),
                class_name="mx-auto max-w-2xl px-4 pb-24 pt-16 sm:px-6 lg:max-w-7xl lg:px-8",
            ),
            class_name="pt-20 min-h-screen bg-white",
        ),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col",
    )