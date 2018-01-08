from libtiff import TIFF
import numpy as np

filename='\home\\nauge\TSTORM\Data\\tifffile.tif'
data=np.zeros((2048,2048),dtype=np.uint16)
tiff = TIFF.open(filename, mode='w8')
for i in range(600):
    tiff.write_image(data)
    print(i)
tiff.close()