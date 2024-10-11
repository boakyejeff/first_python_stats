# %%
import numpy as np
import matplotlib.pyplot as plt
import random
from time import time, sleep

# %%
from numba import jit, njit

# %%
# First define a basic function
def hypot(a, b):
  return np.sqrt(a**2 + b**2)

# %%
hypot(3.0, 4.0)

# %%
N = 5_000_000
StartTime = time()
for _ in range(N): c = hypot(3.0, 4.0)
print(f"{N} evaluations took {round(time() - StartTime,2)} seconds.")

# %%
@njit
def hypot_jit(a, b):
  return np.sqrt(a**2 + b**2)

# %%
hypot_jit(3.0, 4.0)

# %%
StartTime = time()
for _ in range(N): c = hypot_jit(3.0, 4.0)
print(f"{N} evaluations took {round(time() - StartTime,2)} seconds.")

# %% Brute force estimation of pi
# A = pi*r^2, so for a unit circle A = pi
@njit
def compute_pi(N):
  NumAccept = 0
  for i in range(N):
    # Simulate an (x,y) in a unit square
    x = random.random()
    y = random.random()
    # Note that x and y are in [0,1], so we are only considering the
    # upper right quadrant when we simulate
    #
    # Is the point in the unit circle?
    if (x**2 + y**2 < 1.0):
      NumAccept += 1
    # Proportion of samples in the unit circle x4
    # because we only sampled from one quadrant
  return 4.0 * NumAccept / N

# %% Calling the first time takes longer
N = 10_000_000
StartTime = time()
compute_pi(N)  # First time calling, needs to compile
print(f"Took {round(time() - StartTime,2)} seconds")

# %%
StartTime = time()
compute_pi(N)  # Faster
print(f"Took {round(time() - StartTime,2)} seconds")

# %% Numba stores the original Python function in .py_func()
StartTime = time()
# Original Python implementation, slow
compute_pi.py_func(N)
print(f"Took {round(time() - StartTime,2)} seconds")

# %% Function with Gamma-Normal Mixture
@njit
def MixtureGamNorm(x):
  p = np.exp(-((x - 15)**2)/2)
  if x > 0:
    p += x*np.exp(-x/2)
  return p

# %%
print(MixtureGamNorm(-5))
print(MixtureGamNorm(1))
print(MixtureGamNorm(15))

# %%
@njit
def MetropolisHastings(N, p):
  # Initialize empty array
  PSamples = np.empty((N))
  PSamples[:] = np.NaN # Not strictly needed but good practice
  PSamples[0] = 1 # "arbitrary" but should be in the ballpark
  # core MH loop
  for i in range(N-1):
    CurrentSample = PSamples[i]
    # Step 1: Propose move
    # Switch between the two below lines to note the error
    #ProposedSample = random.normalvariate(mu = CurrentSample, sigma = 1.0)
    ProposedSample = np.random.normal(loc = CurrentSample)
    #
    # Step 2: Compute acceptance ratio
    alpha = p(ProposedSample)/p(CurrentSample)
    u = random.random()
    if u < alpha:
      PSamples[i+1] = ProposedSample
    else:
      PSamples[i+1] = CurrentSample
  return PSamples

# %%
Sims435 = MetropolisHastings(N = 1, p = MixtureGamNorm) # One to compile

# %%
N = 1_000_000
# %%
StartTime = time()
Sims1 = MetropolisHastings(N, p = MixtureGamNorm)
print(f"Took {round(time() - StartTime,2)} seconds")

# %%
StartTime = time()
Sims2 = MetropolisHastings.py_func(N, p = MixtureGamNorm.py_func)
print(f"Took {round(time() - StartTime,2)} seconds")

# %%
Sims = MetropolisHastings(10_000_000, p = MixtureGamNorm)
fig = plt.figure(figsize=(7,3))
# empty assignment to avoid output
_ = plt.hist(Sims1, bins = 1000, range = (-1, 20))
plt.show()

##################################################################
# Parallel Processing with Pool()
##################################################################
# %%
def SuperComplexFun(SleepTime):
  sleep(SleepTime) # math calculation simulator

# %%
Start = time()
SuperComplexFun(1)
print(f"Took {round(time() - Start,3)}s")

# %%
Start = time()
for _ in range(3): SuperComplexFun(1)
print(f"Took {round(time() - Start,3)}s")

# %%
import multiprocessing as mp
print(mp.cpu_count())

# %%
#Can specify how many processors we wish to use
# defaults to all (mp.cpu_count()) available
pool = mp.Pool()
# %%
Start = time()
# Note no parenthesis in function call
_ = pool.map(SuperComplexFun,[2]*8)
print(f"Took {round(time() - Start,3)}s") # takes 1s for 8 evaluations!
pool.close()  # Closes the child processes
pool.join()   # Aggregates results

# %% Calling our MH function with multiple arguments
# Pass a list of tuples which correspond to the arguments
# Each list element will be eveluated in parallel
pool = mp.Pool(2)
Args = [(10, MixtureGamNorm), (10, MixtureGamNorm)]
# %%
Result = pool.starmap(MetropolisHastings, Args)
pool.close()
pool.join()

# %%
type(Result)

# %%
len(Result)

# %%
print(Result)

# %% 
# Original
StartTime = time()
Sims1 = MetropolisHastings(100_000_000, p = MixtureGamNorm)
print(f"Took {round(time() - StartTime,2)} seconds")

# %%
# Parallel
Start = time()
pool = mp.Pool(5)
Args = [(20_000_000, MixtureGamNorm) for _ in range(5)]
Result = pool.starmap(MetropolisHastings, Args)
pool.close()
pool.join()
Result = np.concatenate( Result, axis=0 )
print(f"Took {round(time() - Start,3)}s")

# %%
_ = plt.hist(Result, bins = 1000, range = (-1, 20))
plt.show()
# %%
1+1
# %%