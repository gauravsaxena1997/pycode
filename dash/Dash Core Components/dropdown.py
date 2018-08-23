import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
print (dcc.__version__)

app = dash.Dash()
app.config['suppress_callback_exceptions']=True

app.layout = html.Div ([
	html.H1 ('Dash Core Components'),
	html.Hr (),
	html.H4 ('Dropdown Single Select'),
	dcc.Dropdown (
		id = 'dropdown',
		options= [
			{ 'label': 'Bootstrap', 'value': "bt" },
			{ 'label': 'Django', 'value': "dj" },
			{ 'label': 'Docker', 'value': "doc" },
			{ 'label': 'Ansible', 'value': "ansi" }
		],
		value = "doc"           #Default
	) ,
	html.H5 ( id = 'output-div1' ),
	html.H4 ('Dropdown Multi Select'),
	dcc.Dropdown (
		id = 'multi-dropdown',
		options= [
			{ 'label': 'Hadoop' , 'value':'had' },
			{ 'label': 'Spark' , 'value':'spa' },
			{ 'label': 'Hive' , 'value':'hi' },
			{ 'label': 'Hbase' , 'value':'h' } ] ,
		value = 'spa',
		multi = True
		),
	html.H5 ( id = 'output-div2' ),
	html.H4 ('Dropdown: Disable search'),
	dcc.Dropdown (
	options= [
		{ 'label': 'Hadoop' , 'value':'had' },
		{ 'label': 'Spark' , 'value':'spa' },
		{ 'label': 'Hive' , 'value':'hi' },
		{ 'label': 'Hbase' , 'value':'h' } ] ,
	searchable = False
	),
	html.H4 ('Dropdown Clear'),
	dcc.Dropdown (
	options= [
		{ 'label': 'Hadoop' , 'value':'had' },
		{ 'label': 'Spark' , 'value':'spa' },
		{ 'label': 'Hive' , 'value':'hi' },
		{ 'label': 'Hbase' , 'value':'h' } ] ,
	clearable = False
	),
	html.H4 ('Disable Dropdown'),
	dcc.Dropdown (
	options= [
		{ 'label': 'Hadoop' , 'value':'had' },
		{ 'label': 'Spark' , 'value':'spa' },
		{ 'label': 'Hive' , 'value':'hi' },
		{ 'label': 'Hbase' , 'value':'h' } ] ,
	disabled= True
	),
	html.H4 ('Disable Options'),
	dcc.Dropdown (
	options= [
		{ 'label': 'Hadoop' , 'value':'had' },
		{ 'label': 'Spark' , 'value':'spa', 'disabled': 'True' },
		{ 'label': 'Hive' , 'value':'hi' },
		{ 'label': 'Hbase' , 'value':'h' } ] ,
	),
	html.H4 ('Placeholder Test'),
	dcc.Dropdown (
	options= [
		{ 'label': 'Hadoop' , 'value':'had' },
		{ 'label': 'Spark' , 'value':'spa' },
		{ 'label': 'Hive' , 'value':'hi' },
		{ 'label': 'Hbase' , 'value':'h' } ] ,
	placeholder = "Select a technology"
	),
] , style={'marginBottom': 80, 'marginTop': 25} )

@app.callback (
	Output ( 'output-div1', 'children' ),
	[ Input ('dropdown', 'value') ]
)
def update_data_single (value):
	return 'You have selected "{}"'.format(value)

@app.callback (
	Output ( 'output-div2', 'children'),
	[Input ( 'multi-dropdown', 'value' )]
)
def update_data_multi (value):
	return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)