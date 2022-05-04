#Python 3.7.10
'''pip3 install flask'''
from flask import Flask,render_template,request
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

app = Flask('__name__')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
    
@app.route('/')
def home():
    return render_template('Jenkins-page.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
