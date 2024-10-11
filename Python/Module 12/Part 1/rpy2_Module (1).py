# %%
import rpy2.robjects as robjects

# %%
pi = robjects.r['pi']
print(pi[0])

# %%
RMonths = robjects.r['month.name']
RMonths
type(RMonths)
RMonths[0:4]

# %%
Months = list(RMonths)
type(Months)
Months[0:4]


# %%
robjects.r("x <- 2") # returns the value to Python
# %%
robjects.r("y <- x^3")
# %%
robjects.r("c(y, x)")

# %%
robjects.r('pi') + 2

# %%
import numpy as np
from rpy2.robjects import FloatVector

# %%
NumPyRange = np.arange(1, 5, 1)

# %%
robjects.r("NumPyRange^2")


# %%
# Will not work because R does not understand NumPy arrays
robjects.globalenv['NumPyRange'] = NumPyRange


# %%
# Must use robjects.FloatVector() to convert.
robjects.globalenv['NumPyRange'] = FloatVector(NumPyRange)

# %%
robjects.r("NumPyRange")
# %%
robjects.r("NumPyRange^2")


# %%
RangeSquared = robjects.r("NumPyRange^2")
type(RangeSquared)
np.array(RangeSquared)


# %%
import rpy2.robjects.packages as rpackages
base = rpackages.importr('base')
utils = rpackages.importr('utils')
# %%
type(utils)


# select the first mirror in the list
#utils.chooseCRANmirror(ind=1)
#utils.install_packages("<package name>")


# library(mcmc)
# p <- function(x) exp(-x^2/2)
# p(c(-2, -1, 0, 1, 2))

# MH = metrop(p, 0, 1000)
# str(MH)
# head(MH[[2]][,1])

# plot(MH[[2]][,1],type = "l")


# %%
import numpy as np
import matplotlib.pyplot as plt
import rpy2.robjects.packages as rpackages
import rpy2.robjects as robjects


# %%
base = rpackages.importr('base')
utils = rpackages.importr('utils')


# %%
#utils.chooseCRANmirror(ind=1) # select the first mirror in the list
#utils.install_packages("mcmc")
mcmc = rpackages.importr('mcmc')
#dir(mcmc)


# %%
p = robjects.r("p <- function(x) exp(-x^2/2)")

# %%
robjects.r("p(c(-2, -1, 0, 1, 2))")


# %%
MH = mcmc.metrop(p, 0, 1000)
dir(MH)
vals = MH[1]
npvals = np.array(vals)

# %%
plt.plot(npvals)
plt.show()
