from math import sqrt

COLORS = (
    (181, 230, 99),
    (23, 186, 241),
    (99, 23, 153),
    (231, 99, 29),
)

def closest_color(r,g,b):
    color_diffs = []
    for color in COLORS:
        cr = color[0]
        cg = color[1]
        cb = color[2]
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

def main():
    k = closest_color(12, 34, 156)
    print(k)
    print("end")
# closest_color((12, 34, 156))
# # => (99, 23, 153)

# closest_color((23, 145, 234))
# # => (23, 186, 241)


# import numpy as np

# list_of_colors = [[255,0,0],[150,33,77],[75,99,23],[45,88,250],[250,0,255]]
# color = [155,155,155]

# def closest(colors,color):
#     colors = np.array(colors)
#     color = np.array(color)
#     distances = np.sqrt(np.sum((colors-color)**2,axis=1))
#     index_of_smallest = np.where(distances==np.amin(distances))
#     smallest_distance = colors[index_of_smallest]
#     return smallest_distance 

# closest_color = closest(list_of_colors,color)
# print(closest_color )



# l = [[1, 2], [2, 3], [4, 5]]

# out = open('out.csv', 'w')
# for row in l:
#     for column in row:
#         out.write('%d;' % column)
#     out.write('\n')
# out.close()


if __name__ == '__main__': main()