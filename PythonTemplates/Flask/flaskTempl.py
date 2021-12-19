from flask import Flask, render_template

# set up app
app = Flask(__name__)


@app.get("/")
def home():
    """
    A method that enables GET for endpoint '/'
    :return: Content for the page
    """
    return "Hello World!"


@app.get("/welcome")
def welcome():
    # /welcome endpoint using template HTML
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run(debug=True)
