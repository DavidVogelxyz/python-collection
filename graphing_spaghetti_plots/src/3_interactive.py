import pandas as pd
import plotly.express as px

df_wide = pd.read_csv('../test-data.csv')
df_long = pd.melt(
        df_wide,
        id_vars=['x'],
        value_vars=[
            'hello',
            'there',
            'this',
            'is',
            'a',
            'test',
            'using',
            'some',
            'python'
            ]
        )

fig = px.line(df_long, x='x', y='value', color='variable')

fig.show()
