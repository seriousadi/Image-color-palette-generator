from PIL import Image
import numpy as np
from collections import Counter
from matplotlib.colors import rgb2hex


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


class ProcessImage():
    def __init__(self):
        pass

    def get_top_10(self, imageLocation):

        image = Image.open(f"{imageLocation}")

        list1 = []
        numpydata = np.asarray(image)

        for n in numpydata:
            for m in n:
                list1.append(f'[{m[0]}, {m[1]}, {m[2]}]')

        new_set = set(list1)
        words = {}
        c = Counter(list1)
        for n in new_set:
            words.__setitem__(n, c[n])

        top_10_colors = sorted(words.items(), key=lambda x: x[1], reverse=True)[0:10]
        new_list = []
        for n in top_10_colors:
            l = n[0].replace('[', '')
            l = l.replace(']', '').split(',')
            l = [int(x) for x in l]
            new_list.append(l)

        hex_codes = [rgb_to_hex(n[0], n[1], n[2]) for n in new_list]

        return hex_codes
