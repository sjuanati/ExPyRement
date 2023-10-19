"""
Reco: always use @functools.wraps when using own decorators in case of using
some libs or frameworks that look at the __name__ of the function instead of
the variable name
Reco: use generic decorators accepting *args, **kwargs to be able to use them
in multiple functions
"""

import functools

user = {"username": "Sergi", "access_level": "admin"}


def without_decorator():
    """function without decorator"""

    def my_function():
        """docstring in my function"""
        return "Password for admin is 1234"

    def user_has_permission(func):
        if user.get("access_level") == "admin":
            return func
        raise RuntimeError

    my_secure_function = user_has_permission(my_function)
    print(my_secure_function())  # Output: Password for admin is 1234
    print(my_function.__name__)  # Output: my_function
    print(my_function.__doc__)  # Output: docstring in my function


def with_decorator():
    """without decorator"""

    def user_has_permission(func):
        def secure_func():
            if user.get("access_level") == "admin":
                return func()

        return secure_func

    @user_has_permission  # `my_function()` is replaced by `user_has_permission()`
    def my_function():
        """docstring in my function"""
        return "Password for admin is 1234"

    print(my_function())  # Output: Password for admin is 1234
    print(my_function.__name__)  # Output: secure_func
    print(my_function.__doc__)  # Output: None


def with_decorator_wrap():
    """decorator without wrapping"""

    def user_has_permission(func):
        @functools.wraps(func)
        def secure_func():
            if user.get("access_level") == "admin":
                return func()

        return secure_func

    @user_has_permission  # `my_function()` is replaced by `user_has_permission()`
    def my_function():
        """doctring in my function"""
        return "Password for admin is 1234"

    print(my_function())  # Output: Password for admin is 1234
    print(my_function.__name__)  # Output: my_function
    print(my_function.__doc__)  # Output: doctring in my function


def with_decorator_func_param():
    """decorator with param in function"""

    def user_has_permission(func):
        @functools.wraps(func)
        def secure_func(panel):
            if user.get("access_level") == "admin":
                return func(panel)

        return secure_func

    @user_has_permission
    def my_function(panel):
        return f"Password for {panel} panel is 1234"

    print(my_function("movies"))  # Output: Password for movies panel is 1234


def with_decorator_deco_param():
    """decorator with param in function and in decorator"""

    def user_has_permission(access_level):
        def my_decorator(func):
            @functools.wraps(func)
            def secure_func(panel):
                if user.get("access_level") == access_level:
                    return func(panel)

            return secure_func

        return my_decorator

    @user_has_permission("admin")
    def my_function(panel):
        return f"Password for {panel} panel is 1234"

    print(my_function("movies"))  # Output: Password for movies panel is 1234


def with_decorator_any_params():
    """decorator with any number of params in function"""

    def user_has_permission(func):
        @functools.wraps(func)
        def secure_func(*args, **kwargs):  # receives either a tuple or dictionary
            if user.get("access_level") == "admin":
                return func(*args, **kwargs)

        return secure_func

    @user_has_permission
    def my_function(panel):
        return f"Password for {panel} panel is 1234"

    @user_has_permission
    def another_func():
        return "Other function"

    print(my_function("movies"))  # Output: Password for movies panel is 1234
    print(another_func())  # Output: Other function


def test():
    LINE = "-----------------\n"
    print(LINE, "1) without decorator:")
    without_decorator()
    print(LINE, "2) decorator without wrapping:")
    with_decorator()
    print(LINE, "3) decorator wrapping:")
    with_decorator_wrap()
    print(LINE, "4) decorator with param in function:")
    with_decorator_func_param()
    print(LINE, "5) decorator with param in function and in decorator:")
    with_decorator_deco_param()
    print(LINE, "6) decorator with any number of params in function:")
    with_decorator_any_params()
