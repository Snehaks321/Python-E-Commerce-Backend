import reflex as rx
from typing import TypedDict
from app.states.shop_state import Product, ShopState


class CartItem(TypedDict):
    id: str
    name: str
    price: float
    image_url: str
    quantity: int
    size: str
    color: str
    category: str


class CartState(rx.State):
    items: list[CartItem] = []
    is_open: bool = False
    shipping_name: str = ""
    shipping_address: str = ""
    shipping_city: str = ""
    shipping_zip: str = ""
    shipping_country: str = ""
    order_placed: bool = False
    order_number: str = ""

    @rx.var
    def total_items(self) -> int:
        return sum((item["quantity"] for item in self.items))

    @rx.var
    def subtotal(self) -> float:
        return sum((item["price"] * item["quantity"] for item in self.items))

    @rx.var
    def tax(self) -> float:
        return self.subtotal * 0.08

    @rx.var
    def total_price(self) -> float:
        return self.subtotal + self.tax

    @rx.event
    async def add_to_cart(self, product: Product):
        shop_state = await self.get_state(ShopState)
        size = (
            shop_state.selected_size
            if shop_state.selected_size
            else product["sizes"][0]
        )
        color = (
            shop_state.selected_color
            if shop_state.selected_color
            else product["colors"][0]
        )
        for i, item in enumerate(self.items):
            if (
                item["id"] == product["id"]
                and item["size"] == size
                and (item["color"] == color)
            ):
                self.items[i]["quantity"] += 1
                self.items = self.items
                yield rx.toast("Cart updated")
                return
        new_item: CartItem = {
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "image_url": product["image_url"],
            "quantity": 1,
            "size": size,
            "color": color,
            "category": product["category"],
        }
        self.items.append(new_item)
        yield rx.toast("Added to cart")

    @rx.event
    def remove_item(self, index: int):
        if 0 <= index < len(self.items):
            self.items.pop(index)

    @rx.event
    def increment_quantity(self, index: int):
        if 0 <= index < len(self.items):
            self.items[index]["quantity"] += 1
            self.items = self.items

    @rx.event
    def decrement_quantity(self, index: int):
        if 0 <= index < len(self.items):
            if self.items[index]["quantity"] > 1:
                self.items[index]["quantity"] -= 1
                self.items = self.items
            else:
                self.items.pop(index)

    @rx.event
    def set_shipping_name(self, val: str):
        self.shipping_name = val

    @rx.event
    def set_shipping_address(self, val: str):
        self.shipping_address = val

    @rx.event
    def set_shipping_city(self, val: str):
        self.shipping_city = val

    @rx.event
    def set_shipping_zip(self, val: str):
        self.shipping_zip = val

    @rx.event
    def set_shipping_country(self, val: str):
        self.shipping_country = val

    @rx.event
    def place_order(self):
        if not self.items:
            yield rx.toast("Cart is empty")
            return
        if (
            not self.shipping_name
            or not self.shipping_address
            or (not self.shipping_city)
        ):
            yield rx.toast("Please fill in all shipping details")
            return
        import random

        self.order_number = f"ORD-{random.randint(10000, 99999)}"
        self.order_placed = True
        self.items = []
        yield rx.window_alert("Order placed successfully!")