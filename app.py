import pandas as pd
from dash import Dash, html, dash_table, dcc, Input, Output
import plotly.express as px
from dash_bootstrap_templates import load_figure_template

sorted_df=pd.read_csv('sorted_df.csv')
by_port_code = sorted_df.groupby("Port Code")
el_paso_2402 = by_port_code.get_group(2402)

load_figure_template('LUX')

# Initialize the app
app = Dash()

# App layout
app.layout = html.Div(
        children=[
    html.Div(
        children=[
        html.H1('Inbound Crossings El Paso 1996-2023',
        style={'textAlign': 'center'}),
        ]
    ),

    html.Div([
        html.H2('Data table: Port 2402', style={'padding-left': '2em'}),
        html.Div(
        children=[
        html.Figure(dash_table.DataTable(data=el_paso_2402.to_dict('records'), page_size=10,
            style_as_list_view=True,
            style_cell={'padding': '5px'},
            style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold',
    },
                                        )) ]
        ),
        html.Div([ 
        html.H2('Visualization', style={'padding-left': '2em'}),
        dcc.Graph(id="graph",style={'padding': '0em 2em'}),
        dcc.Checklist(
        id="checklist",
        options=["Bus Passengers", "Personal Vehicles","Personal Vehicle Passengers",
                 "Pedestrians","Trucks"],
        value=["Personal Vehicle Passengers","Personal Vehicles","Pedestrians", "Bus Passengers","Trucks"],
        inline=True,
        style={'text-align':'center', 'padding-bottom':'2em'}
        ),
        
                 ]),
    ])
        ])

@app.callback(
    Output("graph", "figure"),
    Input("checklist", "value"))
def update_line_chart(measures):
    mask = el_paso_2402.Measure.isin(measures)
    fig = px.line(el_paso_2402[mask],
        x="Date", y="Value", 
        color='Measure',
        color_discrete_map={'Personal Vehicles': 'blue', 'Personal Vehicle Passengers': 'red', 
                            'Pedestrians': 'green', 'Bus Passengers': '#ae4deb', 'Trucks': '#ed3ed6', 
                                }
                 )
    fig.update_layout(
    legend=dict(
        orientation="v", 
        yanchor="top", 
        y=1.02,          
        xanchor="right",  
        x=1              
    )
)
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)