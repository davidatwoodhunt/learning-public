#!/usr/bin/env python
# coding: utf-8

# # Monte Carlo Example 
# - Runs Monte Carlo with brownian motion 

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
def simulate_stock_price(S0, mu, sigma, T, dt):
    N = int(T/dt)
    t = np.linspace(0, T, N)
    W = np.random.standard_normal(size=N)
    W = np.cumsum(W)*np.sqrt(dt) # standard Brownian motion
    X = (mu-0.5*sigma**2)*t + sigma*W
    S = S0*np.exp(X)
    return t, S

# Parameters
S0 = 100    # Initial stock price
mu = 0.02   # Expected return
sigma = 0.4 # Volatility
T = 10.0     # Time horizon
dt = 0.01   # Time step

# Simulation for 50 diff scenarios 
for _ in range(50):
    t, S = simulate_stock_price(S0, mu, sigma, T, dt)
    plt.plot(t, S)
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.title('Stock Price Simulation')
plt.show()



# # Explanation on Brownian Motion 
# 

# In[ ]:




