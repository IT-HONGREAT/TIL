import numpy as np
from PIL import Image

img = np.asarray(Image.open('lena.png'))

img = img.copy()

img[img >=150] = 255

img = Image.fromarray(img, 'RGB')
img.save('out_condition_2.png')

