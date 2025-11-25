import reflex as rx
from app.states.cart_state import CartState
from app.components.navbar import navbar
from app.components.footer import footer


def form_input(
    label: str, placeholder: str, on_change: rx.event.EventType, value: str = ""
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1"),
        rx.el.input(
            placeholder=placeholder,
            on_change=on_change,
            class_name="w-full rounded-md border border-gray-300 px-3 py-2 text-sm shadow-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500",
        ),
        class_name="mb-4",
    )


def order_summary_item(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=item["image_url"],
                class_name="h-16 w-16 rounded-md object-cover border border-gray-200",
            ),
            rx.el.div(
                rx.el.p(item["name"], class_name="text-sm font-medium text-gray-900"),
                rx.el.p(f"Qty: {item['quantity']}", class_name="text-xs text-gray-500"),
                class_name="ml-4",
            ),
            class_name="flex items-center",
        ),
        rx.el.p(
            f"${item['price'] * item['quantity']:.2f}",
            class_name="text-sm font-medium text-gray-900",
        ),
        class_name="flex items-center justify-between py-4",
    )


def checkout_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Shipping Information",
                class_name="text-lg font-semibold text-gray-900 mb-6",
            ),
            rx.el.form(
                form_input("Full Name", "John Doe", CartState.set_shipping_name),
                form_input("Address", "123 Main St", CartState.set_shipping_address),
                rx.el.div(
                    form_input("City", "New York", CartState.set_shipping_city),
                    form_input(
                        "ZIP / Postal Code", "10001", CartState.set_shipping_zip
                    ),
                    class_name="grid grid-cols-2 gap-4",
                ),
                form_input("Country", "United States", CartState.set_shipping_country),
            ),
            class_name="bg-white p-6 rounded-lg shadow-sm border border-gray-100",
        ),
        rx.el.div(
            rx.el.h2(
                "Payment Method", class_name="text-lg font-semibold text-gray-900 mb-6"
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.input(
                        type="radio",
                        name="payment",
                        id="card",
                        default_checked=True,
                        class_name="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500",
                    ),
                    rx.el.label(
                        "Credit Card",
                        html_for="card",
                        class_name="ml-3 block text-sm font-medium text-gray-700",
                    ),
                    class_name="flex items-center mb-4",
                ),
                rx.el.div(
                    rx.el.input(
                        type="radio",
                        name="payment",
                        id="paypal",
                        class_name="h-4 w-4 text-blue-600 border-gray-300 focus:ring-blue-500",
                    ),
                    rx.el.label(
                        "PayPal",
                        html_for="paypal",
                        class_name="ml-3 block text-sm font-medium text-gray-700",
                    ),
                    class_name="flex items-center",
                ),
                class_name="bg-white p-6 rounded-lg shadow-sm border border-gray-100",
            ),
            class_name="mt-8",
        ),
    )


def order_confirmation() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("check_check", class_name="h-16 w-16 text-green-500 mx-auto mb-4"),
            rx.el.h1(
                "Order Confirmed!", class_name="text-3xl font-bold text-gray-900 mb-2"
            ),
            rx.el.p(
                f"Order #{CartState.order_number}",
                class_name="text-xl text-gray-600 mb-6",
            ),
            rx.el.p(
                "Thank you for your purchase. We have received your order and will send you a confirmation email shortly.",
                class_name="text-gray-500 mb-8 max-w-md mx-auto",
            ),
            rx.el.a(
                "Continue Shopping",
                href="/",
                class_name="inline-block bg-blue-600 text-white px-8 py-3 rounded-md font-medium hover:bg-blue-700 transition-colors",
            ),
            class_name="text-center py-16",
        ),
        class_name="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8",
    )


def checkout_content() -> rx.Component:
    return rx.cond(
        CartState.order_placed,
        order_confirmation(),
        rx.el.div(
            rx.el.h1("Checkout", class_name="text-3xl font-bold text-gray-900 mb-8"),
            rx.el.div(
                rx.el.div(checkout_form(), class_name="lg:col-span-7"),
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Order Summary",
                            class_name="text-lg font-medium text-gray-900 mb-4",
                        ),
                        rx.el.div(
                            rx.foreach(CartState.items, order_summary_item),
                            class_name="divide-y divide-gray-200 border-t border-b border-gray-200 mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.span("Subtotal", class_name="text-gray-600"),
                                rx.el.span(
                                    f"${CartState.subtotal:.2f}",
                                    class_name="font-medium text-gray-900",
                                ),
                                class_name="flex justify-between py-2",
                            ),
                            rx.el.div(
                                rx.el.span("Shipping", class_name="text-gray-600"),
                                rx.el.span(
                                    "$5.00", class_name="font-medium text-gray-900"
                                ),
                                class_name="flex justify-between py-2",
                            ),
                            rx.el.div(
                                rx.el.span("Tax", class_name="text-gray-600"),
                                rx.el.span(
                                    f"${CartState.tax:.2f}",
                                    class_name="font-medium text-gray-900",
                                ),
                                class_name="flex justify-between py-2",
                            ),
                            rx.el.div(
                                rx.el.span(
                                    "Total",
                                    class_name="text-lg font-bold text-gray-900",
                                ),
                                rx.el.span(
                                    f"${CartState.total_price + 5.0:.2f}",
                                    class_name="text-lg font-bold text-gray-900",
                                ),
                                class_name="flex justify-between py-4 border-t border-gray-200 mt-2",
                            ),
                            class_name="text-sm",
                        ),
                        rx.el.button(
                            "Place Order",
                            on_click=CartState.place_order,
                            class_name="w-full mt-6 bg-blue-600 text-white py-4 rounded-md font-bold text-lg hover:bg-blue-700 transition-colors shadow-md hover:shadow-lg",
                        ),
                        class_name="bg-gray-50 p-6 rounded-lg h-fit sticky top-24",
                    ),
                    class_name="lg:col-span-5",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8",
        ),
    )


def checkout_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(checkout_content(), class_name="pt-20 min-h-screen bg-white"),
        footer(),
        class_name="font-['Inter'] bg-white min-h-screen flex flex-col",
    )