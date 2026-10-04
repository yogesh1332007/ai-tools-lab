def is_palindrome(s):
    """Check whether a string reads the same forwards and backwards."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def count_words(text):
    """Count and return the number of words in the given text."""
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32


# Example usage
print("Palindrome:", is_palindrome("madam"))
print("Word count:", count_words("Hello world from Python"))
print("Temperature:", celsius_to_fahrenheit(25))
