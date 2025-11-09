# Dataset and data transformation
Import dataset from kagglehub, it contains a register of inbound crossings at the US-Canada and US-Mexico border.

```python
import kagglehub
path = kagglehub.dataset_download("sahirmaharajj/border-crossing-dataset")
```
Import CSV file and sort by date.

```python
import pandas as pd
file_path = path+"/Border_Crossing_Entry_Data.csv"
df=pd.read_csv(file_path)
```

```python
df['Date'] = pd.to_datetime(df['Date'], format="%Y/%m/%d")
sorted_df = df.sort_values(by='Date')
```

Then export data.

```python
sorted_df.to_csv('sorted_df.csv')
```

In the pyhton app, group by port code and get the group corresponding to port 2402.

```python
sorted_df=pd.read_csv('sorted_df.csv')
by_port_code = sorted_df.groupby("Port Code")
el_paso_2402 = by_port_code.get_group(2402)
```
Finally the code in the app.py file renders the interactive graph.
