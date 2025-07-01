from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Moose'}
    return '''
<html>
    <head>
        <title>Home Page - Moose</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''