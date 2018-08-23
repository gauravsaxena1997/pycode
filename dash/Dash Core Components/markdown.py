import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
print (dcc.__version__)

app = dash.Dash()

app.layout = html.Div ([
dcc.Markdown('''

# This is an <h1> tag
## This is an <h2> tag
###### This is an <h6> tag
'''),

dcc.Markdown('''
*This text will be italic*

_This will also be italic_

**This text will be bold**

__This will also be bold__

_You **can** combine them_
'''),
dcc.Markdown('''
* Item 1
* Item 2
  * Item 2a
  * Item 2b
'''),
dcc.Markdown('''
>
> Block quotes are used to highlight text.
>
'''),
dcc.Markdown('''
[Dash User Guide](https://dash.plot.ly/)
'''),
dcc.Markdown('''
Inline code snippet: `True`

Block code snippet:
```
import dash
app = dash.Dash()
```
''')

])
if __name__ == '__main__':
    app.run_server(debug=True)