import reflex as rx
from app.states.auth_state import AuthState
from app.components.navbar import navbar
from app.components.footer import footer


def input_field(
    label: str,
    type_: str,
    placeholder: str,
    on_change: rx.event.EventType,
    value: str = "",
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700"),
        rx.el.div(
            rx.el.input(
                type=type_,
                placeholder=placeholder,
                on_change=on_change,
                class_name="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm",
            ),
            class_name="mt-1",
        ),
    )


def login_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Sign in to your account",
                class_name="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900",
            ),
            rx.el.p(
                rx.el.a(
                    "Or start your 14-day free trial",
                    href="#",
                    class_name="font-medium text-blue-600 hover:text-blue-500",
                ),
                class_name="mt-2 text-center text-sm text-gray-600",
            ),
            class_name="sm:mx-auto sm:w-full sm:max-w-md",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.form(
                    rx.el.div(
                        input_field(
                            "Email address",
                            "email",
                            "you@example.com",
                            AuthState.set_login_email,
                        ),
                        class_name="space-y-6",
                    ),
                    rx.el.div(
                        input_field(
                            "Password",
                            "password",
                            "********",
                            AuthState.set_login_password,
                        ),
                        class_name="space-y-6 mt-6",
                    ),
                    rx.cond(
                        AuthState.error_message != "",
                        rx.el.div(
                            AuthState.error_message,
                            class_name="mt-4 text-sm text-red-600 text-center",
                        ),
                        rx.fragment(),
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Sign in",
                            type="button",
                            on_click=AuthState.login,
                            class_name="flex w-full justify-center rounded-md border border-transparent bg-blue-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2",
                        ),
                        class_name="mt-6",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.a(
                                "Don't have an account? Sign up",
                                href="/signup",
                                class_name="font-medium text-blue-600 hover:text-blue-500",
                            ),
                            class_name="text-sm",
                        ),
                        class_name="flex items-center justify-center mt-6",
                    ),
                ),
                class_name="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10",
            ),
            class_name="mt-8 sm:mx-auto sm:w-full sm:max-w-md",
        ),
        class_name="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8",
    )


def signup_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Create your account",
                class_name="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900",
            ),
            class_name="sm:mx-auto sm:w-full sm:max-w-md",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.form(
                    rx.el.div(
                        input_field(
                            "Full Name", "text", "John Doe", AuthState.set_signup_name
                        ),
                        class_name="space-y-6",
                    ),
                    rx.el.div(
                        input_field(
                            "Email address",
                            "email",
                            "you@example.com",
                            AuthState.set_signup_email,
                        ),
                        class_name="space-y-6 mt-6",
                    ),
                    rx.el.div(
                        input_field(
                            "Password",
                            "password",
                            "********",
                            AuthState.set_signup_password,
                        ),
                        class_name="space-y-6 mt-6",
                    ),
                    rx.el.div(
                        input_field(
                            "Confirm Password",
                            "password",
                            "********",
                            AuthState.set_signup_confirm_password,
                        ),
                        class_name="space-y-6 mt-6",
                    ),
                    rx.cond(
                        AuthState.error_message != "",
                        rx.el.div(
                            AuthState.error_message,
                            class_name="mt-4 text-sm text-red-600 text-center",
                        ),
                        rx.fragment(),
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Sign up",
                            type="button",
                            on_click=AuthState.signup,
                            class_name="flex w-full justify-center rounded-md border border-transparent bg-blue-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2",
                        ),
                        class_name="mt-6",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.a(
                                "Already have an account? Sign in",
                                href="/login",
                                class_name="font-medium text-blue-600 hover:text-blue-500",
                            ),
                            class_name="text-sm",
                        ),
                        class_name="flex items-center justify-center mt-6",
                    ),
                ),
                class_name="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10",
            ),
            class_name="mt-8 sm:mx-auto sm:w-full sm:max-w-md",
        ),
        class_name="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8",
    )


def login_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(login_form(), class_name="pt-20 min-h-screen bg-gray-50"),
        footer(),
        class_name="font-['Inter'] bg-gray-50 min-h-screen flex flex-col",
    )


def signup_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(signup_form(), class_name="pt-20 min-h-screen bg-gray-50"),
        footer(),
        class_name="font-['Inter'] bg-gray-50 min-h-screen flex flex-col",
    )