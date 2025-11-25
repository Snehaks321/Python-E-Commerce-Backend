import reflex as rx


def hero() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.image(
                    src="https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=2000&q=80",
                    class_name="w-full h-full object-cover object-top opacity-90",
                ),
                class_name="absolute inset-0 z-0",
            ),
            rx.el.div(
                class_name="absolute inset-0 bg-gradient-to-r from-gray-900/60 to-transparent z-10"
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "Autumn / Winter",
                        class_name="text-white/90 font-medium tracking-widest text-sm sm:text-base uppercase mb-4 block animate-fade-in",
                    ),
                    rx.el.h1(
                        "The New Standard",
                        class_name="text-4xl sm:text-5xl md:text-7xl font-bold text-white mb-6 leading-tight",
                    ),
                    rx.el.p(
                        "Discover our latest collection defined by modern silhouettes and premium sustainable fabrics.",
                        class_name="text-white/80 text-lg sm:text-xl max-w-lg mb-8 font-light",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Shop Women",
                            href="/women",
                            class_name="bg-white text-gray-900 px-8 py-3 font-semibold hover:bg-gray-100 transition-colors duration-200",
                        ),
                        rx.el.a(
                            "Shop Men",
                            href="/men",
                            class_name="border border-white text-white px-8 py-3 font-semibold hover:bg-white hover:text-gray-900 transition-all duration-200",
                        ),
                        class_name="flex flex-col sm:flex-row gap-4",
                    ),
                    class_name="max-w-3xl",
                ),
                class_name="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex items-center",
            ),
            class_name="relative h-[600px] sm:h-[700px] w-full bg-gray-900 overflow-hidden",
        )
    )