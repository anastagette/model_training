# def power(a, n):
#     m = 1
#     if n >= 0:
#         for i in range(n):
#             m *= a
#     else:
#         for i in range(n, 0):
#             m *= 1/a
#     return print(m)
# power(int(input()), int(input()))
heights = []
for i in range(5):
    heights.append(int(input()))
print(heights)
for i in range(5):
    print(heights.index(max(heights)))
    heights.insert(heights.index(max(heights)), 0)
    heights.remove(max(heights))
    print(heights)