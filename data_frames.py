import pandas as pd 

data = {"id":[1001,1002,1003,1004,1005,1006], "name":["Ganpath Patel","Anuj Avasthi","Anil Kumar","Gaurav Gupta","Anant Nag","Ganesh Rao"], "sal":[10000,23000.50,18000.33,16500.50,12000.75,9999.99],"doj":["10-10-2000","3-20-2002","3-3-2002","9-10-2000","10-8-2000","9-9-1999"] }
df = pd.DataFrame(data)
#print(df.shape)

#r, c = df.shape

#print(r)

#print(df.head(3))  #prints the first n number of rows
 
#print(df.tail(2))  #prints last n number of rows
 
#print(df[2:5])     #excludes the 5th row

#print(df[::2])     #or df[0::2] used for displaying alternate rows
 
#print(df[5:0:-1])  #displays rows in reverse order

#print(df.columns)  #displays column data
#print(df.sal)      #displays column data can also use df['sal']
#print(df[['name', 'doj']])   #displays multiple column data
#print(df['sal'].max())  #displays maximum
#print(df['sal'].min())  #displays minimum
#print(df['sal'].describe())  #method to retrieve statistical information
#print(df[df.sal == df.sal.min()])
#print(df[['id', 'name']][df.sal>10000])
#print(df.index)  #knowing the index range
df1 = df.set_index('id') # setting a column as index
#print(df1)

#print(df1.loc[1003])  #location by id number
#df1.reset_index(inplace = True)
#print(df1)
#print(df.sort_values('sal')) #sorting the data in ascending order
#print(df.sort_values('id', ascending=False))  #sorting the values in descending order
