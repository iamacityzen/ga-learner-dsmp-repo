# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)
data.hist('Rating',bins = 5)
data= data[data['Rating'] <=5]
data.hist('Rating',bins = 5)
#Code ends here


# --------------
# code starts here



total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())
missing_data = pd.concat([total_null,percent_null],keys=['Total','Percent'],axis = 1)
data.dropna(inplace = True)
total_null_1 = data.isnull().sum()
percent_null_1 = (total_null/data.isnull().count())
missing_data_1 = pd.concat([total_null_1,percent_null_1],keys=['Total','Percent'],axis = 1)
# code ends here


# --------------

#Code starts here
import seaborn as sns
import matplotlib.pyplot as pyplot
sns.set(style = 'ticks')
sns.catplot(x="Category",y="Rating",data=data, kind="box" , height = 10)

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
data['Installs'].value_counts()
data['Installs'] = data['Installs'].str.replace('+' , " ")
data['Installs'] = data['Installs'].str.replace(',' , "")
data['Installs'] = data['Installs'].astype(int)
le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])

#Code ends here



# --------------


#Code starts here

#Removing `,` from the column
data['Price']=data['Price'].str.replace('$','')



#Converting the column to `int` datatype
data['Price'] = data['Price'].astype(float)




#Code ends here#Code starts here



#Code ends here


# --------------

#Code starts here
data['Genres'].unique()
new = data['Genres'].str.split(pat = ';', expand = True)
data['Genres'] = new[0]
gr_mean = data.groupby('Genres',as_index = False)[['Rating']].mean()
gr_mean.describe()
gr_mean = gr_mean.sort_values(by = 'Rating',ascending = True)


#Code ends here


# --------------

#Code starts here
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = data['Last Updated'].max()
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days



#Code ends here


