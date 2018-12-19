from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "What's up Comp Prog Class?????!"

# use decorators to link the function to a url
@app.route('/')
def main():
    return render_template('index.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)