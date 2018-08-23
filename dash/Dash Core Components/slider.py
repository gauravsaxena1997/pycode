import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
print (dcc.__version__)

app = dash.Dash()

app.layout = html.Div ([
	html.H2 ('Basic Slider'),
	dcc.Slider ( 
		id = "slider-1",
		min = 0,
		max = 10,
		step = 0.5,
		value = 2 ),
	html.Div ( id="output-slider" ),
	html.H2 ('Marks and Steps'),
	dcc.Slider ( 
		min = 0,
		max = 10,
		step = None,
		marks = {
			0: '0 °F',
			2: '2 °F',
			5: '5 °F',
			7.5: '7.5 °F' },
		value = 5),
	html.H2 ('Styling Marks'),
	dcc.Slider ( 
		min = 0,
		max = 10,
		step = None,
		marks = {
			0: { 'label': '0 °F' , 'style': { 'color': ' #0e6fb6 ' } },
			2: { 'label': '2 °F' , 'style': { 'color': ' #54aae8 ' } },
			5: { 'label': '5 °F' , 'style': { 'color': ' #ffaf2c ' } },
			7.5: { 'label': '7.5 °F' , 'style': { 'color': ' #fa5801 ' } } },
		value = 5),
	html.H2 ('included false'),
	dcc.Slider ( 
		min = 0,
		max = 10,
		marks = {
			0: { 'label': '0 °F' , 'style': { 'color': ' #0e6fb6 ' } },
			2: { 'label': '2 °F' , 'style': { 'color': ' #54aae8 ' } },
			5: { 'label': '5 °F' , 'style': { 'color': ' #ffaf2c ' } },
			7.5: { 'label': '7.5 °F' , 'style': { 'color': ' #fa5801 ' } } },
		value = 5,
		included  = False )
], style = {"padding": 40} )

@app.callback (
	Output ( 'output-slider', 'children' ),
	[Input ( 'slider-1', 'value' ) ]
)
def update_data(value):
	return 'You selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)