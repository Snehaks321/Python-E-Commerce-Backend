import reflex as rx
from typing import TypedDict
import asyncio


class Order(TypedDict):
    id: str
    date: str
    total: float
    status: str
    items: int


class User(TypedDict):
    name: str
    email: str
    password: str
    orders: list[Order]


class AuthState(rx.State):
    user: User | None = None
    is_authenticated: bool = False
    login_email: str = ""
    login_password: str = ""
    signup_name: str = ""
    signup_email: str = ""
    signup_password: str = ""
    signup_confirm_password: str = ""
    error_message: str = ""
    _users: list[User] = [
        {
            "name": "Demo User",
            "email": "demo@example.com",
            "password": "password",
            "orders": [
                {
                    "id": "ORD-2024-001",
                    "date": "Oct 15, 2024",
                    "total": 125.5,
                    "status": "Delivered",
                    "items": 3,
                }
            ],
        }
    ]

    @rx.event
    def set_login_email(self, value: str):
        self.login_email = value
        self.error_message = ""

    @rx.event
    def set_login_password(self, value: str):
        self.login_password = value
        self.error_message = ""

    @rx.event
    def set_signup_name(self, value: str):
        self.signup_name = value
        self.error_message = ""

    @rx.event
    def set_signup_email(self, value: str):
        self.signup_email = value
        self.error_message = ""

    @rx.event
    def set_signup_password(self, value: str):
        self.signup_password = value
        self.error_message = ""

    @rx.event
    def set_signup_confirm_password(self, value: str):
        self.signup_confirm_password = value
        self.error_message = ""

    @rx.event
    def login(self):
        for u in self._users:
            if u["email"] == self.login_email and u["password"] == self.login_password:
                self.user = u
                self.is_authenticated = True
                self.error_message = ""
                return rx.redirect("/profile")
        self.error_message = "Invalid email or password"

    @rx.event
    def signup(self):
        if not self.signup_name or not self.signup_email or (not self.signup_password):
            self.error_message = "All fields are required"
            return
        if self.signup_password != self.signup_confirm_password:
            self.error_message = "Passwords do not match"
            return
        for u in self._users:
            if u["email"] == self.signup_email:
                self.error_message = "User already exists"
                return
        new_user: User = {
            "name": self.signup_name,
            "email": self.signup_email,
            "password": self.signup_password,
            "orders": [],
        }
        self._users.append(new_user)
        self.user = new_user
        self.is_authenticated = True
        self.error_message = ""
        return rx.redirect("/profile")

    @rx.event
    def logout(self):
        self.user = None
        self.is_authenticated = False
        return rx.redirect("/")