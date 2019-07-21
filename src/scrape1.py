import requests
import six
import lxml.html as lh
from itertools import cycle, islice
from matplotlib import colors
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.nfl.com/standings/division/2018/REG"

page = requests.get(url)

page = requests.get(url)

doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//tr')

[len(T) for T in tr_elements[:12]]


for j in range(1, len(tr_elements)):
    T = tr_elements[j]

    if len(T) != 10:
        break

    i = 0

    for t in T.iterchildren():
        data = t.text_content()

        if i > 0:
            try:
                data = int(data)
            except:
                pass

        col[i][1].append(data)
        i += 1

print(j)
