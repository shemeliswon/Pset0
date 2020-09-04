def print_pyramid(n_rows) -> object:
    for i in range(n_rows):
        print(' ' * (n_rows - i - 1) + (2 * i + 1) * '=')


print_pyramid(2)
print_pyramid(3)

