import pandas as pd 

data = {'Task': ['Finish project', 'Read book', 'Go shopping'],
'Status': ['Completed', 'Pending', 'Pending']}
df = pd.DataFrame(data)
print(df)