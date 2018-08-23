import dash
import dash_core_components as dcc
import dash_html_components as html
print (dcc.__version__)

app = dash.Dash()


app.layout = html.Div ([
	html.H1 ('Dash Core Components'),
	html.H4 ('Dropdown Single Select'),
	dcc.Dropdown (
		options= [
			{ 'label': 'Bootstrap', 'value': "bt" },
			{ 'label': 'Django', 'value': "dj" },
			{ 'label': 'Docker', 'value': "doc" },
			{ 'label': 'Ansible', 'value': "ansi" }
		],
		value = "doc"           #Default
	) ,
	html.H4 ('Dropdown Multi Select'),
	dcc.Dropdown (
		options= [
			{ 'label': 'Hadoop' , 'value':'had' },
			{ 'label': 'Spark' , 'value':'spa' },
			{ 'label': 'Hive' , 'value':'hi' },
			{ 'label': 'Hbase' , 'value':'h' } ] ,
		value = 'spa',
		multi = True
		)
	html.H4 ('Slider'),


])


if __name__ == '__main__':
    app.run_server(debug=True)