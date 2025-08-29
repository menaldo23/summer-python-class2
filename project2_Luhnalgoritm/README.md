# Credit Card Validator (Luhn Algorithm)

This is a simple Python program to validate credit card numbers using
the **Luhn algorithm**.

## 📖 How it Works

1.  The program removes spaces and dashes from the input card number.
2.  It reverses the digits of the card number.
3.  Odd-position digits (from the right) are summed directly.
4.  Even-position digits are doubled, and if the result is greater than
    9, the digits of the result are summed (or equivalently, 9 is
    subtracted).
5.  If the total sum is divisible by 10, the card number is considered
    **VALID**.

## 🚀 Usage

Run the program with:

``` bash
python card_validator.py
```

Example:

    Card number: 4111-1111-4555-1142
    Output: INVALID!

## 🛠 Example Code

``` python
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number > 9:
            number -= 9
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
```

## ✅ Example Results

-   `4111-1111-1111-1111` → VALID
-   `4111-1111-4555-1142` → INVALID

------------------------------------------------------------------------

📌 This project is for **educational purposes only**. Do not use it with
real credit card numbers.
git