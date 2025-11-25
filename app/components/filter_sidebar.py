import reflex as rx
from app.states.shop_state import ShopState


def filter_section(title: str, children: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-sm font-semibold text-gray-900 mb-4"),
        children,
        class_name="border-b border-gray-200 pb-6 mb-6 last:border-0",
    )


def filter_sidebar() -> rx.Component:
    return rx.el.div(
        filter_section(
            "Price Range",
            rx.el.div(
                rx.el.div(
                    rx.el.label("Min", class_name="text-xs text-gray-500 mb-1 block"),
                    rx.el.input(
                        type="number",
                        placeholder="0",
                        on_change=ShopState.set_price_min,
                        class_name="w-full border border-gray-300 rounded-md px-2 py-1 text-sm focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none",
                        default_value=ShopState.price_min,
                    ),
                ),
                rx.el.div(
                    rx.el.label("Max", class_name="text-xs text-gray-500 mb-1 block"),
                    rx.el.input(
                        type="number",
                        placeholder="500",
                        on_change=ShopState.set_price_max,
                        class_name="w-full border border-gray-300 rounded-md px-2 py-1 text-sm focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none",
                        default_value=ShopState.price_max,
                    ),
                ),
                class_name="grid grid-cols-2 gap-4",
            ),
        ),
        filter_section(
            "Size",
            rx.el.div(
                rx.foreach(
                    ["XS", "S", "M", "L", "XL", "XXL"],
                    lambda size: rx.el.label(
                        rx.el.input(
                            type="checkbox",
                            on_change=lambda val: ShopState.toggle_size_filter(
                                size, val
                            ),
                            checked=ShopState.filter_sizes.contains(size),
                            class_name="rounded border-gray-300 text-blue-600 focus:ring-blue-500 h-4 w-4 mr-2",
                        ),
                        size,
                        class_name="flex items-center text-sm text-gray-600 cursor-pointer hover:text-gray-900",
                    ),
                ),
                class_name="space-y-2",
            ),
        ),
        class_name="w-full md:w-64 flex-shrink-0",
    )