from greeter import greet


def test_greet_returns_correct_greeting():
    assert greet("World") == "Hello, World!"
    assert greet("Alice") == "Hello, Alice!"
    assert greet("") == "Hello, !"
