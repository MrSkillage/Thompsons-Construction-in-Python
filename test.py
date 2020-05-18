# Conor Rabbitte
# Testing for Thompsons Construction

import regex

# If statement checks that we are in the main method
if __name__ == "__main__":
  # Dictionary tests holds test information
  tests = [
    ["a.b|b*", "bbbb", True],
    ["a.b|b*", "abbb", False],
    ["a?.b.c", "abc", True],
    ["a?.b.c", "aaaaabc", False],
    ["a+.b.c", "aaaaaabc", True],
    ["a+.b.c", "abbbc", False],
    ["b*", "b", True],
    ["b*", "", True],
    ["b*", "abbbb", False]
  ]

# Checks each test in tests and asserts them against the regex match function
for test in tests:
  assert regex.match(test[0], test[1]) == test[2], test[0] + \
  (" should match " if test[2] else " should not mtach ") + test[1]

