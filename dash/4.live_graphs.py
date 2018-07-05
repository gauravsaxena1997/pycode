import dash 
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque


# Deque make a list of specified number and if maxlen is 20 , when the 21th element is inserted it remove the 1st one and insert new 21st element
X = deque (maxlen=20)
Y = deque (maxlen=20)

X.append(1)
Y.append(1)

app = dash.Dash(__name__)
app.layout = html.Div([
	dcc.Graph (id='live-graph', animate=True),
	dcc.Interval (
		id='graph-update',
		interval=1000
		)
	])

@app.callback(
	Output ('live-graph','figure'),
	events = [Event('graph-update','interval')]
	)
def update_graph():
	global X
	global Y
	X.append(X[-1]+1)
	Y.append(Y[-1]+  Y[-1]*random.uniform(-0.1,0.1))

	data = go.Scatter(
		x = list(X),
		y = list(Y),
		name = 'Scatter',
		mode = 'lines+markers'
		)
	return {'data':[data], 'layout': go.Layout( xaxis = dict(range=[min(X),max(X)]  ),
												yaxis = dict(range=[min(Y),max(Y)]  ))  }

if ( __name__ == '__main__') :
    app.run_server( host='192.168.43.89', port=8020, debug=True) 



















