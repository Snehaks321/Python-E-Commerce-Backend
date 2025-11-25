import reflex as rx


def footer_column(title: str, links: list[tuple[str, str]]) -> rx.Component:
    return rx.el.div(
        rx.el.h4(
            title,
            class_name="font-semibold text-gray-900 mb-4 text-sm uppercase tracking-wider",
        ),
        rx.el.ul(
            rx.foreach(
                links,
                lambda link: rx.el.li(
                    rx.el.a(
                        link[0],
                        href=link[1],
                        class_name="text-gray-500 hover:text-gray-900 transition-colors duration-200 text-sm",
                    ),
                    class_name="mb-3",
                ),
            ),
            class_name="space-y-2",
        ),
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "LUXE",
                        class_name="text-gray-900 font-bold tracking-tighter text-2xl",
                    ),
                    rx.el.span(
                        "WEAR",
                        class_name="text-gray-500 font-light tracking-widest text-2xl",
                    ),
                    rx.el.p(
                        "Elevating your everyday style with premium sustainable essentials.",
                        class_name="mt-4 text-gray-500 text-sm leading-relaxed max-w-xs",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon(
                                "instagram",
                                class_name="w-5 h-5 stroke-gray-600 hover:stroke-gray-900",
                            ),
                            href="#",
                            class_name="p-2",
                        ),
                        rx.el.a(
                            rx.icon(
                                "twitter",
                                class_name="w-5 h-5 stroke-gray-600 hover:stroke-gray-900",
                            ),
                            href="#",
                            class_name="p-2",
                        ),
                        rx.el.a(
                            rx.icon(
                                "facebook",
                                class_name="w-5 h-5 stroke-gray-600 hover:stroke-gray-900",
                            ),
                            href="#",
                            class_name="p-2",
                        ),
                        class_name="flex gap-2 mt-6",
                    ),
                    class_name="col-span-1 md:col-span-2",
                ),
                footer_column(
                    "Shop",
                    [
                        ("New Arrivals", "#"),
                        ("Men", "/men"),
                        ("Women", "/women"),
                        ("Accessories", "#"),
                        ("Sale", "#"),
                    ],
                ),
                footer_column(
                    "Support",
                    [
                        ("Contact Us", "#"),
                        ("Shipping & Returns", "#"),
                        ("Size Guide", "#"),
                        ("FAQ", "#"),
                    ],
                ),
                footer_column(
                    "Company",
                    [
                        ("About Us", "#"),
                        ("Sustainability", "#"),
                        ("Careers", "#"),
                        ("Privacy Policy", "#"),
                    ],
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-12",
            ),
            rx.el.div(
                rx.el.p(
                    "© LuxeWear Inc. All rights reserved.",
                    class_name="text-gray-400 text-sm",
                ),
                rx.el.div(
                    rx.icon("credit-card", class_name="w-8 h-8 text-gray-300"),
                    class_name="flex gap-4",
                ),
                class_name="border-t border-gray-100 mt-16 pt-8 flex flex-col sm:flex-row justify-between items-center gap-4",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
        ),
        class_name="bg-white border-t border-gray-100",
    )