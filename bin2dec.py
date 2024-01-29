from math import log2

def is_valid_binary(string):
  """
  Checks if a string contains only 0s and 1s.
  """
  invalid_chars = set(string) - {'0', '1'}
  if invalid_chars:
    print(f"Invalid input! Please enter only 0s and 1s (found: {', '.join(invalid_chars)})")
    return False
  return True

def binary_to_decimal(string):
  """
  Converts a binary string to its decimal equivalent using log2.
  """
  if not is_valid_binary(string):
    return None
  decimal_value = 0
  for i, digit in enumerate(string[::-1]):
    decimal_value += int(digit) * 2**i
  return decimal_value

# Main program
while True:
  binary_string = input("Enter a binary number (up to 8 digits): ")
  if binary_string.lower() == "q":
    break
  decimal_value = binary_to_decimal(binary_string)
  if decimal_value is not None:
    print(f"Decimal equivalent: {decimal_value}")
  else:
    print("Please try again!")

# Bonus feature: variable number of digits
# Instead of hardcoding 8 digits in the input prompt, you can use a loop to read digits dynamically:
#
# binary_string = ""
# while len(binary_string) < 1 or len(binary_string) > 8:
#   digit = input("Enter a binary digit (0 or 1): ")
#   if digit in {'0', '1'}:
#     binary_string += digit
#   else:
#     print("Invalid input! Please enter only 0 or 1.")
#
# ... continue with conversion and processing
