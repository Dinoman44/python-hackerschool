def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return (dx**2 + dy**2) ** 0.5

d = distance(1, 5, -4, 10)
print(d)