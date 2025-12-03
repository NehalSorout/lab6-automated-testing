import calculator

def run_test(test_name, func, expected):
    try:
        result = func()
        if result == expected:
            print(f"[PASS] {test_name}")
        else:
            print(f"[FAIL] {test_name} → Expected {expected}, got {result}")
    except Exception as e:
        if isinstance(expected, type) and isinstance(e, expected):
            print(f"[PASS] {test_name} (caught expected exception: {e})")
        else:
            print(f"[FAIL] {test_name} → Unexpected exception: {e}")


def test_add():
    return calculator.add(2, 3)

def test_subtract():
    return calculator.subtract(10, 4)

def test_multiply():
    return calculator.multiply(6, 7)

def test_divide():
    return calculator.divide(20, 5)

def test_divide_by_zero():
    return calculator.divide(10, 0) 


if __name__ == "__main__":
    print("Running tests one by one...\n")

    run_test("Addition test", test_add, 5)
    run_test("Subtraction test", test_subtract, 6)
    run_test("Multiplication test", test_multiply, 42)
    run_test("Division test", test_divide, 4)
    run_test("Division by zero test", test_divide_by_zero, ValueError)

    print("\nAll tests completed.")
