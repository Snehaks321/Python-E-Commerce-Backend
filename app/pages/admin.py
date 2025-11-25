import reflex as rx
from app.states.auth_state import AuthState
from app.states.shop_state import ShopState, Product


def admin_header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Admin Dashboard", class_name="text-xl font-bold text-gray-900"
                ),
                rx.el.div(
                    rx.el.span(
                        f"Welcome, {AuthState.user['name']}",
                        class_name="text-sm text-gray-500 mr-4",
                    ),
                    rx.el.button(
                        "Logout",
                        on_click=AuthState.logout,
                        class_name="text-sm font-medium text-red-600 hover:text-red-800",
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex justify-between items-center h-16 px-4 sm:px-6 lg:px-8",
            ),
            class_name="bg-white border-b border-gray-200 shadow-sm",
        )
    )


def product_form_field(
    label: str, type_: str, value: str | float, on_change: rx.event.EventType
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1"),
        rx.el.input(
            type=type_,
            on_change=on_change,
            class_name="block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm px-3 py-2 border",
            default_value=value,
        ),
        class_name="mb-4",
    )


def product_modal() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        rx.cond(
                            ShopState.editing_product_id,
                            "Edit Product",
                            "Add New Product",
                        ),
                        class_name="text-lg font-medium leading-6 text-gray-900",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="h-5 w-5 text-gray-400"),
                        on_click=ShopState.close_admin_modal,
                        class_name="bg-white rounded-md hover:text-gray-500 focus:outline-none",
                    ),
                    class_name="flex justify-between items-center mb-5",
                ),
                rx.el.div(
                    product_form_field(
                        "Product Name",
                        "text",
                        ShopState.form_name,
                        ShopState.set_form_name,
                    ),
                    rx.el.div(
                        product_form_field(
                            "Price ($)",
                            "number",
                            ShopState.form_price,
                            ShopState.set_form_price,
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Category",
                                class_name="block text-sm font-medium text-gray-700 mb-1",
                            ),
                            rx.el.select(
                                rx.el.option("Men", value="Men"),
                                rx.el.option("Women", value="Women"),
                                value=ShopState.form_category,
                                on_change=ShopState.set_form_category,
                                class_name="block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm px-3 py-2 border",
                            ),
                            class_name="mb-4",
                        ),
                        class_name="grid grid-cols-2 gap-4",
                    ),
                    product_form_field(
                        "Image URL",
                        "text",
                        ShopState.form_image_url,
                        ShopState.set_form_image_url,
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Description",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.textarea(
                            on_change=ShopState.set_form_description,
                            rows=3,
                            class_name="block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm px-3 py-2 border",
                            default_value=ShopState.form_description,
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            rx.el.input(
                                type="checkbox",
                                checked=ShopState.form_is_new,
                                on_change=ShopState.toggle_form_is_new,
                                class_name="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded",
                            ),
                            rx.el.span(
                                "New Arrival", class_name="ml-2 text-sm text-gray-900"
                            ),
                            class_name="flex items-center",
                        ),
                        rx.el.label(
                            rx.el.input(
                                type="checkbox",
                                checked=ShopState.form_is_sale,
                                on_change=ShopState.toggle_form_is_sale,
                                class_name="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded",
                            ),
                            rx.el.span(
                                "On Sale", class_name="ml-2 text-sm text-gray-900"
                            ),
                            class_name="flex items-center",
                        ),
                        class_name="flex gap-6 mb-6",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Cancel",
                            on_click=ShopState.close_admin_modal,
                            class_name="mt-3 inline-flex w-full justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-base font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm",
                        ),
                        rx.el.button(
                            "Save Product",
                            on_click=ShopState.save_product,
                            class_name="inline-flex w-full justify-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none sm:ml-3 sm:w-auto sm:text-sm",
                        ),
                        class_name="sm:flex sm:flex-row-reverse",
                    ),
                ),
                class_name="inline-block w-full max-w-lg transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left align-bottom shadow-xl transition-all sm:my-8 sm:align-middle sm:p-6",
            ),
            class_name="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0",
        ),
        class_name="fixed inset-0 z-50 overflow-y-auto bg-gray-500 bg-opacity-75 transition-opacity backdrop-blur-sm",
    )


def product_row(product: Product) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.image(
                src=product["image_url"],
                class_name="h-10 w-10 rounded-full object-cover",
            ),
            class_name="whitespace-nowrap py-4 pl-4 pr-3 text-sm sm:pl-6",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.div(product["name"], class_name="font-medium text-gray-900"),
                class_name="text-sm",
            ),
            class_name="whitespace-nowrap px-3 py-4 text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.span(
                product["category"],
                class_name="inline-flex rounded-full bg-gray-100 px-2 text-xs font-semibold leading-5 text-gray-800",
            ),
            class_name="whitespace-nowrap px-3 py-4 text-sm text-gray-500",
        ),
        rx.el.td(
            f"${product['price']:.2f}",
            class_name="whitespace-nowrap px-3 py-4 text-sm text-gray-500",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    "Edit",
                    on_click=lambda: ShopState.open_edit_product_modal(product),
                    class_name="text-blue-600 hover:text-blue-900 mr-4 font-medium",
                ),
                rx.el.button(
                    "Delete",
                    on_click=lambda: ShopState.delete_product(product["id"]),
                    class_name="text-red-600 hover:text-red-900 font-medium",
                ),
                class_name="flex",
            ),
            class_name="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6",
        ),
    )


def admin_dashboard() -> rx.Component:
    return rx.el.div(
        admin_header(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Products", class_name="text-lg font-medium text-gray-900"
                        ),
                        rx.el.button(
                            "Add Product",
                            on_click=ShopState.open_add_product_modal,
                            class_name="inline-flex items-center justify-center rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 sm:w-auto",
                        ),
                        class_name="flex justify-between items-center mb-6",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.table(
                                rx.el.thead(
                                    rx.el.tr(
                                        rx.el.th(
                                            "Image",
                                            class_name="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6",
                                        ),
                                        rx.el.th(
                                            "Name",
                                            class_name="px-3 py-3.5 text-left text-sm font-semibold text-gray-900",
                                        ),
                                        rx.el.th(
                                            "Category",
                                            class_name="px-3 py-3.5 text-left text-sm font-semibold text-gray-900",
                                        ),
                                        rx.el.th(
                                            "Price",
                                            class_name="px-3 py-3.5 text-left text-sm font-semibold text-gray-900",
                                        ),
                                        rx.el.th(
                                            "Actions",
                                            class_name="relative py-3.5 pl-3 pr-4 sm:pr-6",
                                        ),
                                    ),
                                    class_name="bg-gray-50",
                                ),
                                rx.el.tbody(
                                    rx.foreach(ShopState.products, product_row),
                                    class_name="divide-y divide-gray-200 bg-white",
                                ),
                                class_name="min-w-full divide-y divide-gray-300",
                            ),
                            class_name="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg",
                        ),
                        class_name="mt-8 flex flex-col",
                    ),
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8",
            )
        ),
        rx.cond(ShopState.is_admin_modal_open, product_modal(), rx.fragment()),
        class_name="min-h-screen bg-gray-50 font-['Inter']",
    )