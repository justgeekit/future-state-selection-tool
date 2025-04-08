from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

criteria = [
    "Promote workforce diversity",
    "Ensure knowledge transfer",
    "Address aging workforce",
    "Adopt AI and automation",
    "Implement modular construction",
    "Upskill workforce for emerging tech",
    "Develop leadership capabilities",
    "Integrate sustainability practices",
    "Enhance collaboration",
    "Build continuous learning frameworks",
    "Scenario-specific training (AI, green tech)",
    "Improve retention practices",
    "Manage workforce mobility"
]

def generate_row(i, label):
    return dbc.Row([
        dbc.Col(html.Div(label), width=4),
        dbc.Col(dcc.Input(id=f'priority-{i}', type='number', min=1, max=5, placeholder='Priority (1-5)'), width=2),
        dbc.Col(dcc.Input(id=f'readiness-{i}', type='number', min=1, max=5, placeholder='Readiness (1-5)'), width=2),
        dbc.Col(html.Div(id=f'gap-{i}'), width=2),
    ], className='mb-2')

app.layout = html.Div([
    html.H2("Future State Selection Tool"),
    html.Hr(),
    html.Div([generate_row(i, label) for i, label in enumerate(criteria)]),
    html.Br(),
    dbc.Button("Calculate Gaps", id="calc-btn", color="primary"),
    html.Div(id="summary", className='mt-4')
])

@app.callback(
    Output("summary", "children"),
    Input("calc-btn", "n_clicks"),
    [State(f'priority-{i}', 'value') for i in range(len(criteria))] +
    [State(f'readiness-{i}', 'value') for i in range(len(criteria))]
)
def calculate_summary(n_clicks, *values):
    if not n_clicks:
        return ""
    n = len(criteria)
    priority = values[:n]
    readiness = values[n:]
    gaps = []
    total_gap = 0
    for i in range(n):
        if priority[i] is not None and readiness[i] is not None:
            gap = abs(priority[i] - readiness[i])
            gaps.append(gap)
            total_gap += gap
    return html.Div([
        html.H5("Assessment Summary"),
        html.P(f"Total Gap Score across all categories: {total_gap}")
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
