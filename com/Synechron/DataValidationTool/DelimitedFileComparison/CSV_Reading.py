import pandas as pd

# Reading data from both source and destination data container
df_source = pd.read_csv("F:\\Git_Projects\\DVT_Pyhon\\Files\\csv\\Source.csv")
df_target = pd.read_csv("F:\\Git_Projects\\DVT_Pyhon\\Files\\csv\\Target.csv")

df_failures = pd.DataFrame(columns=df_source.columns)

print("Source: Total no of rows are = " + str(df_source.shape[0]))
print("Source: Total no of columns are = " + str(df_source.shape[1]))

print("Target: Total no of rows are = " + str(df_target.shape[0]))
print("Target: Total no of columns are = " + str(df_target.shape[1]))

for iRowCounter in range(df_source.shape[0]): # Running from first row to last row in source dataframe
    if df_source.iloc[iRowCounter][0] == df_target.iloc[iRowCounter][0]: # if primary keys are matching
        for iColumnCounter in range(df_source.shape[1]):
            # print(df_source.iloc[iRowCounter][iColumnCounter])
            if df_source.iloc[iRowCounter][iColumnCounter] == df_target.iloc[iRowCounter][iColumnCounter]:
                # print(str(df_source.iloc[iRowCounter][iColumnCounter]) + " matches with " + str(df_target.iloc[iRowCounter][iColumnCounter]))
                pass
            else:
                # print(str(df_source.iloc[iRowCounter][iColumnCounter]) + " do not match with " + str(df_target.iloc[iRowCounter][iColumnCounter]))
                # print(df_source.iloc[iRowCounter])
                # print(df_target.iloc[iRowCounter])
                df_failures = df_failures.append(df_source.iloc[iRowCounter])
                df_failures = df_failures.append(df_target.iloc[iRowCounter])
                break
    elif df_source.iloc[iRowCounter][0] in (df_target[list(df_target)[0]]).tolist(): # check if respective row is present in destination dataframe
        iNewRowCounter = int(df_target[df_target[list(df_target)[0]]== df_source.iloc[iRowCounter][0]].index[0])
        for iColumnCounter in range(df_source.shape[1]):
            if df_source.iloc[iRowCounter][iColumnCounter] == df_target.iloc[iNewRowCounter][iColumnCounter]:
                # print(str(df_source.iloc[iRowCounter][iColumnCounter]) + " matches with " + str(df_target.iloc[iRowCounter][iColumnCounter]))
                pass
            else:
                # print(str(df_source.iloc[iRowCounter][iColumnCounter]) + " do not match with " + str(df_target.iloc[iRowCounter][iColumnCounter]))
                # print(df_source.iloc[iRowCounter])
                # print(df_target.iloc[iRowCounter])
                df_failures = df_failures.append(df_source.iloc[iRowCounter])
                df_failures = df_failures.append(df_target.iloc[iNewRowCounter])
                break
    else:   # if respective record is not present in destimation dataframe
        print(str(df_source.iloc[iRowCounter][0]) + " do not present in " + str(df_target.iloc[iRowCounter][0]))




print(df_source.iloc[1][3])




#print(df_source.count())
#print(df_source.count())
#print(df_source.iloc(0))
#print(df_source.iloc[0])

#test = df_source.iloc[0]
#print(type(test))





#df = 2
#print(df_source)
#print(df_source.columns.size)
#print(df_source.dtypes)
#print(df_source.values)
#print(df_source.head(2))
#print(df_source.at[2,'id'])
#print(type(df_source.at[2,'id']))


print("This is the end of the program")