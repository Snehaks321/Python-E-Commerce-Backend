import reflex as rx
from app.states.shop_state import Product, ShopState
from app.states.cart_state import CartState


def product_card(product: Product) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.image(
                        src=product["image_url"],
                        alt=product["name"],
                        class_name="w-full h-full object-cover object-center transform group-hover:scale-105 transition-transform duration-700 ease-out",
                    ),
                    href=f"/product/{product['id']}",
                    class_name="block w-full h-full",
                ),
                rx.el.div(
                    rx.cond(
                        product["is_new"],
                        rx.el.span(
                            "NEW",
                            class_name="bg-black text-white text-[10px] font-bold px-2 py-1 uppercase tracking-wider",
                        ),
                        rx.fragment(),
                    ),
                    rx.cond(
                        product["is_sale"],
                        rx.el.span(
                            "SALE",
                            class_name="bg-red-600 text-white text-[10px] font-bold px-2 py-1 uppercase tracking-wider ml-2",
                        ),
                        rx.fragment(),
                    ),
                    class_name="absolute top-3 left-3 flex gap-1 pointer-events-none",
                ),
                rx.el.div(
                    rx.el.button(
                        "Quick Add",
                        on_click=lambda: CartState.add_to_cart(product),
                        class_name="w-full bg-white/90 backdrop-blur text-gray-900 py-3 font-semibold text-sm hover:bg-gray-900 hover:text-white transition-colors duration-200",
                    ),
                    class_name="absolute bottom-0 left-0 right-0 translate-y-full group-hover:translate-y-0 transition-transform duration-300 ease-in-out",
                ),
                class_name="relative aspect-[3/4] bg-gray-100 overflow-hidden mb-4",
            ),
            rx.el.div(
                rx.el.p(product["category"], class_name="text-gray-500 text-xs mb-1"),
                rx.el.a(
                    rx.el.h3(
                        product["name"],
                        class_name="text-gray-900 font-medium text-sm mb-1 group-hover:underline decoration-gray-400 underline-offset-4",
                    ),
                    href=f"/product/{product['id']}",
                ),
                rx.el.div(
                    rx.el.span(
                        f"${product['price']:.2f}",
                        class_name="text-gray-900 font-semibold text-sm",
                    ),
                    class_name="flex items-center gap-2",
                ),
                class_name="flex flex-col",
            ),
            class_name="group",
        )
    )