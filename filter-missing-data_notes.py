# https://www.science-emergence.com/Articles/How-to-filter-missing-data-NAN-or-NULL-values-in-a-pandas-DataFrame-/

# Find columns with missing data
df.isnull().any()

# Get a list of columns with missing data
df.columns[df.isnull().any()]

# Get the number of missing data per column
df.isnull().sum()

# Get the column with the maximum number of missing data
df.isnull().sum().nlargest(1)

# Another example: with the first 3 columns with the largest number of missing data:
df.isnull().sum().nlargest(3)

# Get the number total of missing data in the DataFrame
df.isnull().sum().sum()

# Remove columns that contains more than 50% of missing data
column_with_nan = df.columns[df.isnull().any()]
df.shape()
for column in column_with_nan:
	print(column, df[column].isnull().sum())

# Remove from the DataFrame the columns with more than 50% of missing data using drop():
for column in column_with_nan:
	if df[column].isnull().sum()*100.0/df_shape[0] > 50:
		df.drop(column,1, inplace=True)

# Find rows with missing data
df.isnull().any(axis=1)

# Get a list of rows with missing data
df.index[df.isnull().any(axis=1)]

# Get the number of missing data per row

# Get the number of missing data for a given row
df.iloc[1453,:].isnull().sum()

# Get the row with the largest number of missing data
df.isnull().sum(axis=1).nlargest(1)

df.isnull().sum(axis=1).nlargest(3)

# Remove rows with missing data
index_with_nan = df.index[df.isnull().any(axis=1)]
index_with_nan.shape
df.drop(index_with_nan,0, inplace=True)
df.shape