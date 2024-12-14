def count_digits(s):
    return sum(char.isdigit() for char in s)
  
s = input()
print(count_digits(s))
