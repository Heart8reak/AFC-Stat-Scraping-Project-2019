# AFC Stat Scraping Project 2019

1. We need to setup an environment to do our scraping, start off on the Desktop

```bash
mkdir scraping00
cd scraping00
```

2. Create a virtual Environment within the directory and then activate

```bash
virtualenv - p python3 .
soucre bin/activate
```

3. create an src directory to store the project

```bash
mkdir src
cd src
```

4. Download/pip install the dependacies for our projects

```bash
pip install requests
pip install BeautifulSoup
pip install jupyter
pip install pandas
```

5. lets open up Jupyter Notebook, a window with Jupyter notebooks

```bash
jupyter notebook
```

6. click on New, Python 3, will give us a brand new notebook for our scraping project

7. lets start off with our imports

```python
import sys
import collection as co
from requests import *
from bs4 import BeautifulSoup
import pandas as pd
```

8. lets get the url, response status code

```python
url = "https://www.pro-football-reference.com/years/2018/index.htm"

response = get(url)

print(response.status_code)
```

9. We will create a BeautifulSoup object and pass it through a variable

```python
nfl = BeautifulSoup(response.content, 'html.parser)
```

10. Now we search for the element that we are looking

```python
afc_table = nfl.find('div',{'class':'overthrow table_container'})
```

11. We are going to grab headers

```python
table_head = afc_table.find('thead')
header = []
for th in table_head.findAll('th):
    key = th.get_text()
    header.append(key)
print(header)
```

12. We are going to count the rows

```python
endrows = 0
for tr in afc_table.findAll('tbody'):
    if tr.findAll('th')[0].get_text() in (''):
        endrows += 1

rows = len(afc_table.findAll('tr'))
rows -= endrows + 1

print(rows)
```

13. We are going to add it to a Pnadas DataFrame

```python
list_of_dicts = []
for row in range(rows):
    the_row = []
    try:
        table_row = afc_table.findAll('tr')[row]
        for tr in table_row:
            value = tr.get_text()
            the_row.append(value)
        od = co.OrderedDict(zip(header,the_row))
        list_of_dicts.append(od)
    except AttributeError:
        continue

df = pd.DataFrame(list_of_dicts)
df
```

14. Clean the data, remove the NaN

```python
df = df[:].fillna(")
```

15. Let's save it to a csv file

```python
df.to_csv("afc_2018_stat.csv")
```
