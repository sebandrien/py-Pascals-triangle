def pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)

    return triangle

n = 5  # You can change this value to generate more rows
triangle = pascal_triangle(n)

for row in triangle:
    print(row)
