def verify_card_number(card_number):
    # Initialize an accumulator for digits in odd positions (from the right).
    # After reversing the string, these are at indices 0, 2, 4, ...
    sum_of_odd_digits = 0

    # Reverse the card number so the rightmost digit becomes index 0.
    # This makes it easy to apply Luhn's "every second digit from the right" rule.
    card_number_reversed = card_number[::-1]

    # Slice to get every other character starting at index 0 (positions 0, 2, 4, ...).
    # In the original (non-reversed) number, these correspond to the odd positions from the right.
    odd_digits = card_number_reversed[::2]

    # Sum the odd-position digits directly (no transformation per Luhn).
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Initialize an accumulator for the even-position digits (from the right).
    sum_of_even_digits = 0

    # Slice to get every other character starting at index 1 (positions 1, 3, 5, ...).
    # In the original number, these are the even positions from the right.
    even_digits = card_number_reversed[1::2]

    # For each even-position digit (from the right), double it.
    # If doubling yields a two-digit number (>= 10), sum those two digits.
    # Note: summing the digits of a doubled value (e.g., 12 -> 1 + 2) is equivalent to subtracting 9.
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)  # equivalent to: number -= 9
        sum_of_even_digits += number

    # Combine the two sums to get the Luhn checksum total.
    total = sum_of_odd_digits + sum_of_even_digits

    # If the total ends in 0 (i.e., divisible by 10), the number passes the Luhn check.
    return total % 10 == 0


def main():
    # Example input containing separators (dashes). Spaces are also supported below.
    card_number = '4111-1111-4555-1142'

    # Build a translation table that maps '-' and ' ' to '' (i.e., removes them).
    # This allows users to input card numbers with common separators safely.
    card_translation = str.maketrans({'-': '', ' ': ''})

    # Apply the translation table to strip separators from the input.
    # NOTE: If
