from flask import Flask, render_template
app = Flask(__name__)


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("list.html", random_numbers=[3, 1, 5], students=student_info)


@app.route('/')
def hello_world():
    return render_template('index.html', phrase='hello', times=5)

# import statements, maybe some other routes


# @app.route('/success')
# def success():

    # return "<b>success</b>"


# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# @app.route('/hello/<name>')
# def hello(name):
    # print(name)
    # return "Hello, " + name


# for a route '/users/____/____', two parameters in the url get passed as username and id
# @app.route('/users/<username>/<id>')
# def show_user_profile(username, id):
   #  print(id)
    # return "username: " + username + ", id: " + id


if __name__ == "__main__":
    app.run(debug=True)
