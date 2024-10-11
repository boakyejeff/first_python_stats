# %%
import numpy as np
import matplotlib.pyplot as plt

# These are suggested for IDEs
# To prepare IPython for plotting
# %matplotlib          
# %matplotlib notebook # For when plotting in a notebook!
# %%
x, y = np.arange(0,10), np.arange(0,10) # Step 1
fig = plt.figure                        # Step 2

plt.plot(x, y)                          # Step 3
plt.title("Awesome Plot!")              # Step 4
#plt.show()                              # Step 5

# %%
from scipy import pi
from scipy.interpolate import interp1d

xSeq = np.linspace(0, pi, 20)
ySeq = np.sin(2 * pi * xSeq)

plt.plot(xSeq, ySeq)
plt.title("Low Resolution sin(x)")

# %%
x2 = np.linspace(0, pi, 100)
y2 = np.sin(2 * pi * x2)

# %%
plt.plot(xSeq, ySeq)
plt.plot(x2, y2)
plt.title("Low Resolution sin(x)")

# %% Customizing with axis ranges and legend
fig = plt.figure(figsize=(5,2))
plt.plot(xSeq, ySeq, label = "Generated Values")
plt.plot(x2, y2, label = "True Relationship")

# argument to axis
#[xmin, xmax, ylim, ymax]
plt.axis([-1,pi,-2,1])
plt.legend(loc = "lower left", fontsize = "small")

# %% Scatterplot
m, b = 2, 1
x = np.random.uniform(size = 100)
y = m*x + b + np.random.normal(size = 100)
fig = plt.figure(figsize=(5,2))
plt.scatter(x, y)
# or
#plt.plot(x, y,"*")

# %% Styles
plt.style.use('classic')
# %%
print(plt.style.available)

# %%
# with: To make it temporary
with plt.xkcd():
    fig1 = plt.figure()
    # ...

# %%
W = np.random.normal(size = 100)
fig = plt.figure(figsize=(5,2))
plt.hist(W)

# %% Reading data
import pandas as pd
College = pd.read_csv("/home/john/TodaysScripts/College.csv")
College.head()

# %% Plotting data
fig = plt.figure(figsize=(5,2))
plt.scatter(College['Apps'], College['Grad.Rate'])
# change axis scale
#plt.yscale("log")
#plt.xscale("log")

# %% Generating a random walk
import numpy as np
random_data = np.random.randn(50)
rand_walk = random_data.cumsum()  # simulate a random walk
print(random_data[0:4])
print(rand_walk[0:4])

# %% Plotting random walk
fig = plt.figure(figsize=(5,2))
plt.plot(rand_walk)

# %% subplots
fig = plt.figure(figsize=(5,1.5))
pl = fig.add_subplot(1, 2, 1)
pl.plot(rand_walk, "--")
pl = fig.add_subplot(1, 2, 2)
pl.plot(rand_walk, ".")
plt.show()

# %% Customizing with labels
fig = plt.figure(figsize=(3,2))

plt.plot(rand_walk)
plt.title('A Random Walk')
plt.ylabel('Cumulative Sum')
plt.xlabel('Random Sample')

# %% Generate two different random walks
rand_walk_1 = np.random.randn(50).cumsum()
rand_walk_2 = np.random.randn(50).cumsum()

# %%
fig = plt.figure(figsize=(3,1))
plt.plot(rand_walk_1, '-',label = 'RW1')
plt.plot(rand_walk_2, '--', label = 'RW2')
plt.legend()

# %%
fig = plt.figure(figsize=(5,2))
plt.plot(rand_walk,
          color = "k",
          linestyle = "-",
          marker = "*")
#plt.plot(rand_walk, "k--*")
# Documentation: 
# https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html
# %%
fig = plt.figure(figsize=(5,2))
plt.plot(rand_walk, "k--*")
plt.grid(True)
plt.tight_layout()

# %%
