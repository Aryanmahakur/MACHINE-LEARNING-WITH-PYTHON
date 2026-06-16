import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023]
income = [40, 55, 70, 60]

plt.plot(
    years,
    income,
    color='red',          # line color
    linestyle='--',       # -, --, :, -.
    linewidth=3,          # thickness
    marker='o',           # marker shape
    markersize=10,        # marker size
    label='Income'        # legend name
)

plt.title("Income Trend")
plt.xlabel("Year")
plt.ylabel("Income")
plt.grid(True)
plt.legend()

plt.show()

import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
marks = [30, 45, 55, 70, 85]

plt.scatter(
    hours,
    marks,
    c='green',      # color
    s=200,          # point size
    alpha=0.6,      # transparency
    marker='*'      # shape
)

plt.title("Study Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")

plt.show()

import matplotlib.pyplot as plt

lang = ["Python", "Java", "C++", "C"]
users = [90, 60, 45, 20]

plt.bar(
    lang,
    users,
    color='orange',        # bar color
    width=0.5,             # width
    edgecolor='black',     # border color
    linewidth=2,           # border thickness
    align='center'         # alignment
)

plt.title("Language Popularity")
plt.xlabel("Language")
plt.ylabel("Users")

plt.show()

import numpy as np
import matplotlib.pyplot as plt

marks = np.random.normal(70, 10, 100)

plt.hist(
    marks,
    bins=8,                # groups
    color='skyblue',       # fill color
    edgecolor='black',     # border
    alpha=0.8,             # transparency
    density=False          # frequency count
)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")

plt.show()

import matplotlib.pyplot as plt

lang = ["Python", "Java", "C++", "C"]
users = [90, 60, 45, 20]

explode = [0, 0.1, 0, 0]

plt.pie(
    users,
    labels=lang,          # labels
    autopct='%1.1f%%',    # percentages
    explode=explode,      # pull slice
    shadow=True,          # shadow
    startangle=90         # rotate
)

plt.title("Language Share")

plt.show()

import numpy as np
import matplotlib.pyplot as plt

marks = np.random.normal(70, 10, 100)

plt.boxplot(
    marks,
    showmeans=True,      # mean value
    notch=True,          # notch
    vert=True,           # vertical
    widths=0.5           # width
)

plt.title("Marks Boxplot")
plt.ylabel("Marks")

plt.show()

import matplotlib.pyplot as plt

lang = ["Python", "Java", "C++", "C"]
users = [90, 60, 45, 20]

plt.barh(
    lang,
    users,
    color='cyan',
    edgecolor='black',
    linewidth=2,
    height=0.5
)

plt.title("Language Popularity")
plt.xlabel("Users")
plt.ylabel("Language")

plt.show()