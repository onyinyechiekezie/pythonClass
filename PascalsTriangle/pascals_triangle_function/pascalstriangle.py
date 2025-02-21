def get_pascals_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'({i},{j})', end=' ')

n = int(input("Enter a number: "))
get_pascals_triangle(n)
