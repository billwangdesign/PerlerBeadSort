# l = [[1, 2], [2, 3], [4, 5]]

# out = open('out.csv', 'w')
# for row in l:
#     for column in row:
#         out.write('%d;' % column)
#     out.write('\n')
# out.close()


import csv
from random import random
import random
import numpy as np

def main():
    # persons=[('Lata',22,45),('Anil',21,56),('John',20,60)]
    # csvfile = open('beadsRGB.txt','a', newline='')
    # obj = csv.writer(csvfile)
    # for person in persons:
    #     obj.writerow(person)
    # csvfile.close()
    randnums = np.random.randint(1,100, size=(3,50))
    #print(randnums)
    f = open("bead.csv", "a", newline="")
    
    for i in range(0,50):
        colors = ["red-" + str(random.randrange(999)), randnums[0][i], randnums[1][i], randnums[2][i]]
        writer = csv.writer(f)
        writer.writerow(colors)        
    
    f.close()
    # 
    # colors = ("red", 255, 19, 28)
    # writer = csv.writer(f)
    # writer.writerow(colors)
    # f.close()

if __name__ == '__main__': main()
