n = 5 
# Lower Triangular
print("Lower Triangular Pattern:")
for i in range(1, n + 1):
    print("* " * i)
    
# Upper Triangular
print("\nUpper Triangular Pattern:")
for i in range(n, 0, -1):
    print("* " * i)
    
# Pyramid
print("\nPyramid Pattern:")
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '* ' * i
    print(spaces + stars)
