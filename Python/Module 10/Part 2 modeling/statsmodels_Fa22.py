# %%
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import re # for string substitution

# %%
College = pd.read_csv("/home/john/TodaysScripts/College.csv")

# List comprehension to remove special chars from column names
College.columns = [re.sub("[ ,\$]", "_", re.sub("[.]", "", c))
                      for c in College.columns]

# %%
# DEFINE model
lin_reg_model = smf.ols('RoomBoard ~ Private + Personal + PhD + Outstate',
                          data = College)
# %%
# dir(lin_reg_model) # uncomment to see everything inside
lin_reg_model.endog_names # Y is called "endogenous" by some
lin_reg_model.endog[0:8] # Y data is stored here

# %%
lin_reg_model.exog_names # X variables are called "exogenous"
lin_reg_model.exog[0:4,:] # X data is stored here

# %%
# FIT model
lin_reg_result = lin_reg_model.fit()
# dir(lin_reg_result)

# %%
# EXPLORE model
lin_reg_result.summary()

# %%
lin_reg_result.params
lin_reg_result.pvalues

# %%
lin_reg_result.rsquared
lin_reg_result.rsquared_adj

# %%
y_hat = lin_reg_result.predict(College)
#print(y_hat[0:5])

# %%
fig = plt.figure(figsize=(4,1.75))
# yhat vs y
plt.plot(College['RoomBoard'], y_hat, linestyle = "None", marker = ".")

# %%
print(lin_reg_model.exog_names)

# %%
ExogPred = dict(Private="Yes", Personal=1000, PhD=75, Outstate=10_000)
lin_reg_result.predict(exog = ExogPred)

# %%
# Multiple predictions just use lists in the dict elements
ExogPred = dict(Private=["Yes", "No"],
                Personal=[1000, 1000],
                PhD=[75, 75],
                Outstate=[10_000, 10_000])

lin_reg_result.predict(exog = ExogPred)

# %%
my_figure = plt.figure(figsize=(3,2))
pl = my_figure.add_subplot(1, 1, 1)
sm.graphics.qqplot(lin_reg_result.resid, line='s', ax = pl)

# %%
LogModel = smf.ols('np.log(RoomBoard) ~ Private + Personal + PhD + Outstate',
                     data = College).fit()

# %%
my_figure = plt.figure(figsize=(3,2))
pl = my_figure.add_subplot(1, 1, 1)
sm.graphics.qqplot(LogModel.resid, line='s', ax = pl)

# %%
lin_reg_model.exog[771:774,:] # X data is stored here
College["Private"][771:774]

# %%
College["PrivateNum"] = 0
College.loc[College["Private"] == "Yes", "PrivateNum"] = 1
LogModel2 = smf.ols('np.log(RoomBoard) ~ C(PrivateNum)+Personal+PhD+Outstate',
                     data = College).fit()

# %%
# Create a new variable that indicates if a college has a lot of PhDs
College["MorePhD"] = 0
College.loc[College["PhD"] > np.median(College["PhD"]), "MorePhD"] = 1

# %%
CollegeANOVA = smf.ols('np.log(RoomBoard) ~ C(Private)*C(MorePhD)',
                        data=College).fit()

ANOVAtable = sm.stats.anova_lm(CollegeANOVA, typ=2) # Type II SS
print(np.round(ANOVAtable,5))
# %%
