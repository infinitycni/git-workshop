# Custom python functions


def double_number(a):
    """Addition of the same number.
    param int a"""
    print(f"value before double_number(): {a}")
    result = a + a
    print(f"value after double_number(): {result}")
    return result


def square_number(a):
    """Squaring of the same number.
    param int a"""
    print(f"value before square_number(): {a}")
    result = a * a
    print(f"value after square_number(): {result}")
    return result