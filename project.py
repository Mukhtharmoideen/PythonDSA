# Prime checking if not prime it will print factors of the number.
def prime_check(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


num = int(input('Enter the number: '))
factors = []
if prime_check(num):
    print(True)
else:
    for i in range(2, num + 1):
        if num % i == 0:
            factors.append(i)
    print(factors)

# Program to rotate elements of an array to left or right by a given number of steps
def rotate_arr(arr, steps, direction):
    length = len(arr)

    # Adjust steps if it's greater than array length
    steps %= length

    if direction == 'left':
        rotated_arr = arr[steps:] + arr[:steps]
    elif direction == 'right':
        rotated_arr = arr[-steps:] + arr[:-steps]
    else:
        raise ValueError('Invalid direction. Use "left" or "right."')
    return rotated_arr


arr = [1, 2, 3, 4, 5, 6, 7]
steps = int(input('Enter the steps to rotate:'))
direction = input('Enter the direction (left, or right): ')
print(arr)
rotated_Arr = rotate_arr(arr, steps, direction)
print(rotated_Arr)


