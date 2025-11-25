import reflex as rx
import logging
from typing import TypedDict


class Product(TypedDict):
    id: str
    name: str
    price: float
    category: str
    image_url: str
    images: list[str]
    is_new: bool
    is_sale: bool
    description: str
    sizes: list[str]
    colors: list[str]
    rating: float
    reviews: int


class ShopState(rx.State):
    is_mobile_menu_open: bool = False
    is_search_open: bool = False
    search_query: str = ""
    show_only_new: bool = False
    show_only_sale: bool = False
    cart_count: int = 2
    current_category_filter: str = "All"
    price_min: float = 0.0
    price_max: float = 500.0
    filter_sizes: list[str] = []
    sort_option: str = "featured"
    selected_size: str = ""
    selected_color: str = ""
    selected_image_index: int = 0
    is_admin_modal_open: bool = False
    admin_search_query: str = ""
    editing_product_id: str = ""
    form_name: str = ""
    form_price: str = ""
    form_category: str = ""
    form_image_url: str = ""
    form_description: str = ""
    form_is_new: bool = False
    form_is_sale: bool = False
    products: list[Product] = [
        {
            "id": "1",
            "name": "Essential Cotton Tee",
            "price": 29.0,
            "category": "Men",
            "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?auto=format&fit=crop&w=800&q=80",
            ],
            "is_new": True,
            "is_sale": False,
            "description": "A wardrobe staple, our Essential Cotton Tee is crafted from 100% organic cotton for breathability and comfort. Features a classic crew neck and a relaxed fit.",
            "sizes": ["S", "M", "L", "XL"],
            "colors": ["White", "Black", "Navy"],
            "rating": 4.8,
            "reviews": 124,
        },
        {
            "id": "3",
            "name": "Minimalist Linen Shirt",
            "price": 45.0,
            "category": "Men",
            "image_url": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?auto=format&fit=crop&w=800&q=80",
            ],
            "is_new": False,
            "is_sale": True,
            "description": "Stay cool in our Minimalist Linen Shirt. Perfect for summer days or tropical getaways. Breathable, lightweight, and effortlessly stylish.",
            "sizes": ["M", "L", "XL"],
            "colors": ["Beige", "White", "Olive"],
            "rating": 4.5,
            "reviews": 89,
        },
        {
            "id": "5",
            "name": "Everyday Chino Pants",
            "price": 55.0,
            "category": "Men",
            "image_url": "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?auto=format&fit=crop&w=800&q=80",
            ],
            "is_new": False,
            "is_sale": False,
            "description": "Versatile chinos that work for the office or the weekend. Made with a hint of stretch for all-day comfort.",
            "sizes": ["30", "32", "34", "36"],
            "colors": ["Khaki", "Navy", "Grey"],
            "rating": 4.6,
            "reviews": 210,
        },
        {
            "id": "9",
            "name": "Oxford Button-Down",
            "price": 59.0,
            "category": "Men",
            "image_url": "https://images.unsplash.com/photo-1598033129183-c4f50c736f10?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1598033129183-c4f50c736f10?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": False,
            "is_sale": False,
            "description": "The classic Oxford shirt, reimagined. Durable fabric that softens with every wash.",
            "sizes": ["S", "M", "L", "XL"],
            "colors": ["Blue", "White", "Pink"],
            "rating": 4.7,
            "reviews": 156,
        },
        {
            "id": "10",
            "name": "Slim Fit Jeans",
            "price": 79.0,
            "category": "Men",
            "image_url": "https://images.unsplash.com/photo-1542272617-08f08375810c?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1542272617-08f08375810c?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": True,
            "is_sale": False,
            "description": "Modern slim fit jeans with premium denim fabric. Includes classic 5-pocket styling.",
            "sizes": ["30", "32", "34", "36"],
            "colors": ["Indigo", "Black"],
            "rating": 4.9,
            "reviews": 54,
        },
        {
            "id": "11",
            "name": "Tech Fleece Hoodie",
            "price": 85.0,
            "category": "Men",
            "image_url": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1556821840-3a63f95609a7?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": False,
            "is_sale": False,
            "description": "Engineered for warmth without the weight. Features a sleek design and zippered pockets.",
            "sizes": ["S", "M", "L", "XL"],
            "colors": ["Grey", "Black"],
            "rating": 4.8,
            "reviews": 320,
        },
        {
            "id": "12",
            "name": "Heavyweight Flannel",
            "price": 65.0,
            "category": "Men",
            "image_url": "https://images.unsplash.com/photo-1622445275463-afa2ab738c34?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1622445275463-afa2ab738c34?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": False,
            "is_sale": True,
            "description": "Rugged and warm, this flannel is perfect for layering in colder months.",
            "sizes": ["M", "L", "XL", "XXL"],
            "colors": ["Red Plaid", "Green Plaid"],
            "rating": 4.6,
            "reviews": 98,
        },
        {
            "id": "13",
            "name": "Merino Wool Sweater",
            "price": 95.0,
            "category": "Men",
            "image_url": "https://images.unsplash.com/photo-1620799140408-ed5341cd2431?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1620799140408-ed5341cd2431?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": True,
            "is_sale": False,
            "description": "Fine gauge merino wool sweater that regulates temperature and resists odors.",
            "sizes": ["S", "M", "L", "XL"],
            "colors": ["Navy", "Charcoal", "Burgundy"],
            "rating": 4.9,
            "reviews": 45,
        },
        {
            "id": "14",
            "name": "Utility Jacket",
            "price": 120.0,
            "category": "Men",
            "image_url": "https://images.unsplash.com/photo-1487222477894-8943e31ef7b2?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1487222477894-8943e31ef7b2?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": False,
            "is_sale": False,
            "description": "Inspired by workwear, this utility jacket features multiple pockets and durable canvas construction.",
            "sizes": ["M", "L", "XL"],
            "colors": ["Olive", "Tan"],
            "rating": 4.7,
            "reviews": 112,
        },
        {
            "id": "15",
            "name": "Performance Shorts",
            "price": 45.0,
            "category": "Men",
            "image_url": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": False,
            "is_sale": False,
            "description": "Quick-drying shorts designed for movement. Great for the gym or a casual day out.",
            "sizes": ["S", "M", "L", "XL"],
            "colors": ["Black", "Grey", "Blue"],
            "rating": 4.5,
            "reviews": 180,
        },
        {
            "id": "2",
            "name": "Urban Denim Jacket",
            "price": 89.5,
            "category": "Women",
            "image_url": "https://images.unsplash.com/photo-1543076447-215ad9ba6923?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1543076447-215ad9ba6923?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1516257984-b1b4d8c9230c?auto=format&fit=crop&w=800&q=80",
            ],
            "is_new": False,
            "is_sale": False,
            "description": "A slightly oversized denim jacket with a vintage wash. The perfect layering piece for any season.",
            "sizes": ["XS", "S", "M", "L"],
            "colors": ["Light Wash", "Medium Wash"],
            "rating": 4.7,
            "reviews": 340,
        },
        {
            "id": "4",
            "name": "Structured Wool Coat",
            "price": 159.0,
            "category": "Women",
            "image_url": "https://images.unsplash.com/photo-1539533018447-63fcce2678e3?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1539533018447-63fcce2678e3?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1541363111435-5c1b7d867904?auto=format&fit=crop&w=800&q=80",
            ],
            "is_new": True,
            "is_sale": False,
            "description": "Elegant wool coat with a tailored fit. Features a notched lapel and deep pockets.",
            "sizes": ["S", "M", "L"],
            "colors": ["Camel", "Black", "Grey"],
            "rating": 4.9,
            "reviews": 85,
        },
        {
            "id": "6",
            "name": "Flowy Summer Dress",
            "price": 65.0,
            "category": "Women",
            "image_url": "https://images.unsplash.com/photo-1495385794356-15371f348c31?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1495385794356-15371f348c31?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1496747611176-843222e1e57c?auto=format&fit=crop&w=800&q=80",
            ],
            "is_new": False,
            "is_sale": True,
            "description": "Lightweight and feminine, this dress features a floral print and a flattering wrap silhouette.",
            "sizes": ["XS", "S", "M", "L"],
            "colors": ["Blue Floral", "Pink Floral"],
            "rating": 4.6,
            "reviews": 215,
        },
        {
            "id": "8",
            "name": "Ribbed Knit Sweater",
            "price": 75.0,
            "category": "Women",
            "image_url": "https://images.unsplash.com/photo-1576566588028-4147f3842f27?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1576566588028-4147f3842f27?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": True,
            "is_sale": False,
            "description": "Cozy ribbed knit sweater with a mock neck. Soft against the skin and keeps you warm.",
            "sizes": ["XS", "S", "M", "L"],
            "colors": ["Cream", "Rust", "Black"],
            "rating": 4.8,
            "reviews": 145,
        },
        {
            "id": "16",
            "name": "High-Waist Leggings",
            "price": 48.0,
            "category": "Women",
            "image_url": "https://images.unsplash.com/photo-1506619216599-9d16d0903dfd?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1506619216599-9d16d0903dfd?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": False,
            "is_sale": False,
            "description": "Buttery soft leggings with high compression. Squat-proof and perfect for yoga.",
            "sizes": ["XS", "S", "M", "L", "XL"],
            "colors": ["Black", "Olive", "Purple"],
            "rating": 4.9,
            "reviews": 560,
        },
        {
            "id": "17",
            "name": "Silk Camisole",
            "price": 60.0,
            "category": "Women",
            "image_url": "https://images.unsplash.com/photo-1609357912348-17930c0110c7?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1609357912348-17930c0110c7?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": False,
            "is_sale": False,
            "description": "Luxurious silk camisole that drapes beautifully. Wear it alone or under a blazer.",
            "sizes": ["XS", "S", "M", "L"],
            "colors": ["Champagne", "Black", "Emerald"],
            "rating": 4.7,
            "reviews": 78,
        },
        {
            "id": "18",
            "name": "Oversized Blazer",
            "price": 135.0,
            "category": "Women",
            "image_url": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": True,
            "is_sale": False,
            "description": "On-trend oversized blazer. Adds immediate polish to any outfit.",
            "sizes": ["S", "M", "L"],
            "colors": ["Beige", "Check", "Black"],
            "rating": 4.8,
            "reviews": 92,
        },
        {
            "id": "19",
            "name": "Pleated Midi Skirt",
            "price": 78.0,
            "category": "Women",
            "image_url": "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": False,
            "is_sale": False,
            "description": "Metallic pleated skirt that moves with you. Great for evening wear.",
            "sizes": ["XS", "S", "M", "L"],
            "colors": ["Silver", "Gold", "Black"],
            "rating": 4.6,
            "reviews": 134,
        },
        {
            "id": "20",
            "name": "Crop Top Hoodie",
            "price": 42.0,
            "category": "Women",
            "image_url": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": False,
            "is_sale": True,
            "description": "Cute and casual crop hoodie. Soft fleece interior.",
            "sizes": ["XS", "S", "M", "L"],
            "colors": ["Pink", "White", "Grey"],
            "rating": 4.5,
            "reviews": 201,
        },
        {
            "id": "21",
            "name": "Boyfriend Jeans",
            "price": 88.0,
            "category": "Women",
            "image_url": "https://images.unsplash.com/photo-1584370848010-d7cc637703e6?auto=format&fit=crop&w=800&q=80",
            "images": [
                "https://images.unsplash.com/photo-1584370848010-d7cc637703e6?auto=format&fit=crop&w=800&q=80"
            ],
            "is_new": True,
            "is_sale": False,
            "description": "Relaxed fit jeans with distressed details. Maximum comfort without sacrificing style.",
            "sizes": ["25", "26", "27", "28", "29", "30"],
            "colors": ["Light Blue", "Vintage Blue"],
            "rating": 4.7,
            "reviews": 115,
        },
    ]

    @rx.var
    def featured_products(self) -> list[Product]:
        return self.products[:4]

    @rx.var
    def search_results(self) -> list[Product]:
        if not self.search_query:
            return []
        return [
            p for p in self.products if self.search_query.lower() in p["name"].lower()
        ]

    @rx.var
    def filtered_products(self) -> list[Product]:
        products = self.products
        if self.show_only_new:
            products = [p for p in products if p["is_new"]]
        if self.show_only_sale:
            products = [p for p in products if p["is_sale"]]
        if self.current_category_filter != "All":
            products = [
                p for p in products if p["category"] == self.current_category_filter
            ]
        products = [
            p for p in products if self.price_min <= p["price"] <= self.price_max
        ]
        if self.filter_sizes:
            products = [
                p for p in products if any((s in p["sizes"] for s in self.filter_sizes))
            ]
        if self.sort_option == "price_asc":
            products = sorted(products, key=lambda p: p["price"])
        elif self.sort_option == "price_desc":
            products = sorted(products, key=lambda p: p["price"], reverse=True)
        elif self.sort_option == "newest":
            products = sorted(products, key=lambda p: p["is_new"], reverse=True)
        elif self.sort_option == "popular":
            products = sorted(products, key=lambda p: p["reviews"], reverse=True)
        return products

    @rx.var
    def current_product(self) -> Product | None:
        args = self.router.page.params
        p_id = args.get("id", "")
        for p in self.products:
            if p["id"] == p_id:
                return p
        return None

    @rx.event
    def set_category_filter(self, category: str):
        self.current_category_filter = category
        self.show_only_new = False
        self.show_only_sale = False
        self.price_min = 0.0
        self.price_max = 500.0
        self.filter_sizes = []
        self.sort_option = "featured"

    @rx.event
    def set_new_arrivals_filter(self):
        self.current_category_filter = "All"
        self.show_only_new = True
        self.show_only_sale = False
        self.price_min = 0.0
        self.price_max = 500.0
        self.filter_sizes = []
        self.sort_option = "newest"

    @rx.event
    def set_sale_filter(self):
        self.current_category_filter = "All"
        self.show_only_new = False
        self.show_only_sale = True
        self.price_min = 0.0
        self.price_max = 500.0
        self.filter_sizes = []
        self.sort_option = "price_asc"

    @rx.event
    def toggle_search(self):
        self.is_search_open = not self.is_search_open
        if not self.is_search_open:
            self.search_query = ""

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def set_price_min(self, val: str):
        try:
            self.price_min = float(val)
        except ValueError as e:
            logging.exception(f"Error: {e}")

    @rx.event
    def set_price_max(self, val: str):
        try:
            self.price_max = float(val)
        except ValueError as e:
            logging.exception(f"Error: {e}")

    @rx.event
    def toggle_size_filter(self, size: str, checked: bool):
        if checked:
            if size not in self.filter_sizes:
                self.filter_sizes.append(size)
        elif size in self.filter_sizes:
            self.filter_sizes.remove(size)

    @rx.event
    def set_sort_option(self, option: str):
        self.sort_option = option

    @rx.event
    def select_size(self, size: str):
        self.selected_size = size

    @rx.event
    def select_color(self, color: str):
        self.selected_color = color

    @rx.event
    def select_image(self, index: int):
        self.selected_image_index = index

    @rx.event
    def reset_product_state(self):
        self.selected_size = ""
        self.selected_color = ""
        self.selected_image_index = 0

    @rx.event
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    @rx.event
    def close_mobile_menu(self):
        self.is_mobile_menu_open = False

    @rx.event
    def add_to_cart(self, product_id: str):
        self.cart_count += 1
        yield rx.toast("Item added to cart")

    @rx.event
    def set_admin_search_query(self, query: str):
        self.admin_search_query = query

    @rx.event
    def set_form_name(self, val: str):
        self.form_name = val

    @rx.event
    def set_form_price(self, val: str):
        self.form_price = val

    @rx.event
    def set_form_category(self, val: str):
        self.form_category = val

    @rx.event
    def set_form_image_url(self, val: str):
        self.form_image_url = val

    @rx.event
    def set_form_description(self, val: str):
        self.form_description = val

    @rx.event
    def toggle_form_is_new(self, val: bool):
        self.form_is_new = val

    @rx.event
    def toggle_form_is_sale(self, val: bool):
        self.form_is_sale = val

    @rx.event
    def open_add_product_modal(self):
        self.editing_product_id = ""
        self.form_name = ""
        self.form_price = ""
        self.form_category = "Men"
        self.form_image_url = ""
        self.form_description = ""
        self.form_is_new = False
        self.form_is_sale = False
        self.is_admin_modal_open = True

    @rx.event
    def open_edit_product_modal(self, product: Product):
        self.editing_product_id = product["id"]
        self.form_name = product["name"]
        self.form_price = str(product["price"])
        self.form_category = product["category"]
        self.form_image_url = product["image_url"]
        self.form_description = product["description"]
        self.form_is_new = product["is_new"]
        self.form_is_sale = product["is_sale"]
        self.is_admin_modal_open = True

    @rx.event
    def close_admin_modal(self):
        self.is_admin_modal_open = False

    @rx.event
    def save_product(self):
        try:
            price = float(self.form_price) if self.form_price else 0.0
        except ValueError as e:
            logging.exception(f"Error: {e}")
            price = 0.0
            yield rx.toast("Invalid price format")
            return
        if self.editing_product_id:
            for i, p in enumerate(self.products):
                if p["id"] == self.editing_product_id:
                    self.products[i]["name"] = self.form_name
                    self.products[i]["price"] = price
                    self.products[i]["category"] = self.form_category
                    self.products[i]["image_url"] = self.form_image_url
                    self.products[i]["images"] = [self.form_image_url]
                    self.products[i]["description"] = self.form_description
                    self.products[i]["is_new"] = self.form_is_new
                    self.products[i]["is_sale"] = self.form_is_sale
                    break
            yield rx.toast("Product updated successfully")
        else:
            import random

            new_id = str(random.randint(1000, 9999))
            new_product: Product = {
                "id": new_id,
                "name": self.form_name,
                "price": price,
                "category": self.form_category,
                "image_url": self.form_image_url,
                "images": [self.form_image_url],
                "description": self.form_description,
                "is_new": self.form_is_new,
                "is_sale": self.form_is_sale,
                "sizes": ["S", "M", "L", "XL"],
                "colors": ["Black", "White"],
                "rating": 0.0,
                "reviews": 0,
            }
            self.products.insert(0, new_product)
            yield rx.toast("Product created successfully")
        self.products = self.products
        self.is_admin_modal_open = False

    @rx.event
    def delete_product(self, product_id: str):
        self.products = [p for p in self.products if p["id"] != product_id]
        yield rx.toast("Product deleted")