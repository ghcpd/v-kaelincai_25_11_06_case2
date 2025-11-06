from PIL import Image
import numpy as np

def bbox_overlap_pixels(img, threshold=50):
    w,h = img.size
    top_region = img.crop((0,0,w,int(h*0.4))).convert('L')
    dark = 0
    for x in range(top_region.size[0]):
        for y in range(top_region.size[1]):
            if top_region.getpixel((x,y))<threshold:
                dark += 1
    return dark
