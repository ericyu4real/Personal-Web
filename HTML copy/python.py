import sys

from PIL import Image
import numpy as np
import math
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon



image = Image.open("track_7_one_branch_15deg_w7 copy 2.png")
numpyData = np.asarray(image)

deg = int(sys.argv[1])
width = int(sys.argv[2])
length = int(sys.argv[3])

deg = math.radians(deg)
if (length + width / math.tan(deg))*math.sin(deg) > 90:
    exit("the branch exceeds the image, try a different parameter")

A = (508, 14)
B = (int(A[0] + width / math.sin(deg)), A[1])
C = (int(B[0] - (length + width / math.tan(deg)) * math.cos(deg)), int(B[1] + (length + width / math.tan(deg)) * math.sin(deg)))
D = (int(A[0] - length * math.cos(deg)), int(A[1] + length * math.sin(deg)))
polygon = Polygon([A, B, C, D])

minx, miny, maxx, maxy = polygon.bounds
minx, miny, maxx, maxy = int(minx), int(miny), int(maxx), int(maxy)

minx, miny, maxx, maxy = int(minx), int(miny), int(maxx), int(maxy)
box_patch = [[x, y] for x in range(minx, maxx + 1) for y in range(miny, maxy + 1)]
for pb in box_patch:
  point = Point(pb[0],pb[1])
  if(polygon.contains(point)):
      numpyData[pb[1]][pb[0]] = 1


im = Image.fromarray(numpyData)
im.putpalette(image.getpalette())
# im.save('photoshop.png')
im.save("track_7_one_branch_15deg_w7.png")




# data_to_pass_back = 'Send this to node process'

# input = sys.argv[1]
# output = data_to_pass_back
# print(output)

# sys.stdout.flush()