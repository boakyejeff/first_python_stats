import pandas as pd
from pandas import Series, DataFrame

# %%
a_Series_object = Series([23, 21, 13, 42])
a_Series_object

# %%
a_Series_object[2]
a_Series_object = Series([23, 21, 13, 42],
                         index = ['John','Fred','Bill','Joe'])
# %%
a_Series_object
# %%
a_Series_object[0]
# %%
a_Series_object['John']

# %%
a_dict = {'Joe':12, 'Fred':10, 'Bill':9, 'John':4}
another_Series = Series(a_dict)
another_Series

# %%
a_Series_object
# %%
another_Series
# %%
a_Series_object + another_Series

# %%
nested_dict = {'Var_1': a_dict,
               'Var_2': {'John':23,'Fred':21, 'Bill':13, 'Joe':42}}

# %%
a_DataFrame = DataFrame(nested_dict)
# %%
aThirdDict = {'Joe':122, 'Bill':150, 'Fred':19, 'John':43}
# %%
a_DataFrame["another_col"] = Series(aThirdDict)
# %%
a_DataFrame

# %%
a_DataFrame.head(2) #tail() for the last few

# %%
a_DataFrame.drop('John')
# %%
a_DataFrame.drop('Var_1',axis=1)

# %%
a_DataFrame['Joe':'John']
# %%
a_DataFrame['Var_1']
# %%
a_DataFrame.index
# %%
a_DataFrame.columns
# %%
a_DataFrame.shape
# %%
a_DataFrame.values

# %%
a_DataFrame
# %%
a_DataFrame.describe()

# %%
# Sorting columns/rows
a_DataFrame.sort_index(axis = 1, ascending = False)
# %%
# sorting DF by column values
a_DataFrame.sort_values(by = "Var_2")
# %%
a_DataFrame['Fred':'John']
# %%
a_DataFrame['Var_1']
# Select a row by index label

# %%
a_DataFrame.loc["John"]

# %%
# Select by columns
a_DataFrame.loc[:,["Var_1","Var_1"]]
# %%
HairColors = {'Bill':"Black", 'John':"Black", 'Fred':"Red", 'Joe':"Blonde"}
# %%
a_DataFrame["HairColors"] = Series(HairColors)
# %%
a_DataFrame[a_DataFrame["HairColors"] == "Black"]
# %%
a_DataFrame[a_DataFrame["Var_1"] > 5]
# %%
a_DataFrame.mean()
# %%
a_DataFrame.median()
# %%
a_DataFrame.std()

# %%
another_DataFrame = DataFrame({'HairColors': ["Black","Red"],
                               'RBG_HEX': ["#000000","#FF0000"]})
                               # %%
a_DataFrame.merge(another_DataFrame, how = "left", on = "HairColors")

# %%
# DF.groupby().<FUN>()
a_DataFrame.groupby("HairColors").mean()


