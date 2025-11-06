# Utilities to compute bbox overlap (used by tests)
from PIL import Image
import numpy as np

def bbox_overlap(b1, b2):
    # b1, b2 = (x0,y0,x1,y1)
    x0 = max(b1[0], b2[0])
    y0 = max(b1[1], b2[1])
    x1 = min(b1[2], b2[2])
    y1 = min(b1[3], b2[3])
    if x1 < x0 or y1 < y0:
        return 0
    return (x1-x0) * (y1-y0)
