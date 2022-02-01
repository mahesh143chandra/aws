import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\sesa637792\Downloads\dirtydata.csv')
#print(df)
#print(df.to_string())
#print(pd.options.display.max_rows)
#print(df.tail(10))
#df.dropna(inplace=True)
#print(df.to_string())
#print(df.duplicated())
df.plot()
plt.show()