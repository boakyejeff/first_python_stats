# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# For Modeling
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.neural_network import MLPRegressor, MLPClassifier

# Model Metrics
from sklearn.metrics import (mean_squared_error, r2_score,
                             classification_report, confusion_matrix)

# %%
College = pd.read_csv("/home/john/TodaysScripts/College.csv")
# List comprehension to remove special chars from column names
College.columns = [re.sub("[ ,\$]", "_", re.sub("[.]", "", c))
                      for c in College.columns]

# %%
X = College.drop(["RoomBoard",'Unnamed:_0', 'Private'], axis = 1)
y = College["RoomBoard"]

# %%
# Define train/test split
XTrain, XTest, YTrain, YTest = train_test_split(X, y,
                                                test_size = 0.1,
                                                random_state = 8100)

# %%
scaler = StandardScaler()

# %%
TrainScalingDetails = scaler.fit(XTrain)
print(TrainScalingDetails.mean_[0:4])
print(TrainScalingDetails.scale_[0:4])

# %%
XTrain.to_numpy()[0,0:4]
XTest.to_numpy()[0,0:4]

# %%
((XTrain.to_numpy()[0,0] - TrainScalingDetails.mean_[0])/
          TrainScalingDetails.scale_[0])

# %%
((XTest.to_numpy()[0,0] - TrainScalingDetails.mean_[0])/
          TrainScalingDetails.scale_[0])

# %%
XTrain = TrainScalingDetails.transform(XTrain)
XTest = TrainScalingDetails.transform(XTest)
XTrain[0,0:4]
XTest[0,0:4]

# %%
def NeatResults(true, pred):
  RMSE = mean_squared_error(true, pred, squared = False)
  Rsq = r2_score(true, pred)
  print(f"RMSE = {np.round(RMSE,3)}, R^2 = {np.round(Rsq,3)}")

# %%
LinMod = LinearRegression().fit(XTrain, YTrain)
# dir(LinMod)

# %%
yHatTrainLM = LinMod.predict(XTrain)
NeatResults(YTrain, yHatTrainLM)
yHatTestLM = LinMod.predict(XTest)
NeatResults(YTest, yHatTestLM)

# %%
RFMod = RandomForestRegressor().fit(XTrain, YTrain)
# dir(RFMod)

# %%
yHatTrainRF = RFMod.predict(XTrain)
NeatResults(YTrain, yHatTrainRF)
yHatTestRF = RFMod.predict(XTest)
NeatResults(YTest, yHatTestRF)

# %%
NNMod = (MLPRegressor(hidden_layer_sizes=(50),
                      max_iter=50_000)
          .fit(XTrain, YTrain))

# %%
yHatTrainNN = NNMod.predict(XTrain)
NeatResults(YTrain, yHatTrainNN)
yHatTestNN = NNMod.predict(XTest)
NeatResults(YTest, yHatTestNN)

# %%
GridMin, GridMax = np.min(YTest), np.max(YTest)
fig = plt.figure(figsize=(5,2))
plt.plot(YTest, yHatTestLM, linestyle = "None", marker = ".", color = "y", label = "Linear Regression")
plt.plot(YTest, yHatTestRF, linestyle = "None", marker = ".", color = "b", label = "Random Forest")
plt.plot(YTest, yHatTestNN, linestyle = "None", marker = ".", color = "r", label = "Neural Network")
plt.plot([GridMin, GridMax], [GridMin, GridMax], color='k', linestyle='-', linewidth=2)
plt.title("Comparison of Models")
plt.xlabel("True Value")
plt.ylabel("Predicted Value")
plt.legend()
plt.show()

# %%
College["HighRmBrd"] = 0
College.loc[College["RoomBoard"] > np.median(College["RoomBoard"]),
             "HighRmBrd"] = 1

College["Private"] = LabelEncoder().fit_transform(College["Private"])
X = College.drop(["Unnamed:_0", "RoomBoard", "HighRmBrd"], axis = 1)
y = LabelEncoder().fit_transform(College["HighRmBrd"])

# Define train/test split
XTrain, XTest, YTrain, YTest = train_test_split(X, y,
                                                test_size = 0.1,
                                                random_state = 8100)

# %%
# Scale X
TrainScalingDetails = scaler.fit(XTrain)
XTrain = TrainScalingDetails.transform(XTrain)
XTest = TrainScalingDetails.transform(XTest)

# %%
LogisticMod = LogisticRegression().fit(XTrain, YTrain)

# %%
RFMod = RandomForestClassifier().fit(XTrain, YTrain)

# %%
NNMod = (MLPClassifier(hidden_layer_sizes=(50),
                       max_iter=50_000)
                .fit(XTrain, YTrain))

# %%
# And obtain predictions
yPredLogistic = LogisticMod.predict(XTest)
yPredRF = RFMod.predict(XTest)
yPredNN = NNMod.predict(XTest)

# %%
print(classification_report(YTest,yPredLogistic))
print(confusion_matrix(YTest,yPredLogistic))

# %%
print(classification_report(YTest,yPredRF))
print(confusion_matrix(YTest,yPredRF))

# %%
print(classification_report(YTest,yPredNN))
print(confusion_matrix(YTest,yPredNN))