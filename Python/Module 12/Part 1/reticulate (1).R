library(reticulate)
conda_list()

np <- import("numpy")
NumPyArray <- np$arange(1, 10, 1)


smf <- import("statsmodels.formula.api")
sm <- import("statsmodels.api")

# in R
x <- runif(1e5, 0, 10)
y <- 1 + 2*x + rnorm(1e5,0,.1)
My_Data <- data.frame(Y = y, X = x)

# To Python!
#Model <- smf$ols("Y ~ X", data = My_Data) # Doesn't work!
Model <- sm$OLS(endog = My_Data$Y, exog = My_Data$X)
FittedModel <- Model$fit()
FittedModel$summary2()


pd <- import("pandas")
College <- pd$read_csv("~/TodaysScripts/College.csv")
class(College)

repl_python()
# Python Code
exit
