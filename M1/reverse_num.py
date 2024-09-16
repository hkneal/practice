def reverse_number(my_num):
  # Reverse the number 
  my_num = [int(x) for x in str(my_num)]
  reverse_num = my_num[::-1]
  # Return the number
  return reverse_num

## Example usage:
print(reverse_number([1223])) # Output: 3221
print(reverse_number(987654321)) # Output: 123456789