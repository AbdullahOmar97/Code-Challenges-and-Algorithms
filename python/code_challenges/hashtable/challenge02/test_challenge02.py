# Write your test here

from challenge02 import find_first_repeated_word

def test_find_first_repeated_word():
    results = {
        "Python is a great language. Python is easy to learn.": find_first_repeated_word("Python is a great language. Python is easy to learn."),
        "Java JavaScript Java": find_first_repeated_word("Java JavaScript Java"),
        "Every day is a new opportunity.": find_first_repeated_word("Every day is a new opportunity."),
        "Just testing for repeated words.": find_first_repeated_word("Just testing for repeated words."),
        "Hello world. Hello!": find_first_repeated_word("Hello world. Hello!"),
        "Repeat, repeat, repeat!": find_first_repeated_word("Repeat, repeat, repeat!")
    }

    expected_results = {
        "Python is a great language. Python is easy to learn.": "PYTHON",
        "Java JavaScript Java": "JAVA",
        "Every day is a new opportunity.": "No Repetition",
        "Just testing for repeated words.": "No Repetition",
        "Hello world. Hello!": "HELLO",
        "Repeat, repeat, repeat!": "REPEAT"
    }

    for input_str, actual in results.items():
        expected = expected_results[input_str]
        if actual == expected:
            print(f"PASSED: {input_str} -> {actual}")
        else:
            print(f"FAILED: {input_str} -> Expected: {expected}, Actual: {actual}")

# Run the tests
if __name__ == "__main__":
    test_find_first_repeated_word()
