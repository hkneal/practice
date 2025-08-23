""" Practicing divmod"""
if __name__ == "__main__":

    a = 17
    b = 10

    print(a//b)
    print(a%b)
    print(divmod(a, b))

def digital_root_modulo(n):
  if n == 0:
    return 0
  else:
    return (n - 1) % 9 + 1


print(digital_root_modulo(13))