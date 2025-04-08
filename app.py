# Install Dash if not already installed: pip install dash
from dash import Dash, dcc, html, Input, Output
import pandas as pd

# Initialize Dash app
app = Dash(__name__)

# Define categories and criteria
categories = {
    "Demographics Management": [
        "Promote workforce diversity",
        "Ensure knowledge transfer",
        "Address aging workforce"
    ],
    "Technology Integration": [
        "Adopt AI and automation",
        "Implement modular construction",
        "Upskill workforce for emerging tech"
    ],
    "Core Competencies": [
        "Develop leadership capabilities",
        "Integrate sustainability practices",
        "Enhance collaboration"
    ],
    "Training Programs": [
        "Build continuous learning frameworks",
        "Scenario-specific training (AI, green tech)"
    ],
    "Challenges": [
        "Improve retention practices",
        "Manage workforce mobility"
    ]
}

# Generate layout dynamically
app.layout = html.Div([
    html.H1("Future State Selection Tool", style={'text-align': 'center'}),
    dcc.Tabs(id="category-tabs", value="Demographics Management", children=[
        dcc.Tab(label=category, value=category) for category in categories.keys()
    ]),
    html.Div(id="category-content"),
    html.Hr(),
    html.Div(id="summary")
])

# Callbacks for rendering each category's content
@app.callback(
    Output("category-content", "children"),
    Input("category-tabs", "value")
)
def render_category(category):
    criteria = categories[category]
    return html.Div([
        html.H3(f"{category}"),
        html.Table([
            html.Tr([
                html.Th("Criterion"),
                html.Th("Priority (1-5)"),
                html.Th("Readiness (1-5)"),
                html.Th("Gap"),
                html.Th("Comments")
            ])
        ] + [
            html.Tr([
                html.Td(criterion),
                html.Td(dcc.Input(id=f"priority-{category}-{i}", type="number", min=1, max=5, value=1)),
                html.Td(dcc.Input(id=f"readiness-{category}-{i}", type="number", min=1, max=5, value=1)),
                html.Td(id=f"gap-{category}-{i}"),
                html.Td(dcc.Input(id=f"comments-{category}-{i}", type="text"))
            ]) for i, criterion in enumerate(criteria)
        ])
    ])

# Callback to calculate gaps dynamically
@app.callback(
    Output("gap-Demographics Management-0", "children"),
    Input("priority-Demographics Management-0", "value"),
    Input("readiness-Demographics Management-0", "value")
)
def calculate_gap(priority, readiness):
    if priority and readiness:
        return str(priority - readiness)
    return "--"

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
