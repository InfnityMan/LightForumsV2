import database_manager as dm

from flask import Flask, render_template, request, jsonify, redirect, url_for, session

import os
from flask import send_from_directory

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'your_secret_key_here'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def begin():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        print(session['username'])
        return render_template("index.html")


@app.route('/add_account', methods=['GET'])
def add_account():
    # Fetch User Details
    username = request.args.get('username')
    password = request.args.get('password')

    # Adds Account and Proceeds to Login Check

    dm.add_account(username, password)

    return redirect(url_for('login_check', username=username, password=password))


@app.route('/signup_page')
def signup_page():
    return render_template('signup_page.html')


@app.route('/login')
def login():
    return render_template('login_page.html')


@app.route("/logging_in", methods=['GET'])
def login_check():
    # Fetch Login Information from User
    username = request.args.get('username')
    password = request.args.get('password')

    login_info = dm.login(username, password)  # Checks if Login Info is Valid

    if login_info is not None:
        session['username'] = login_info[1]
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})


@app.route("/thread/<int:thread_id>")
def open_thread(thread_id):
    return render_template('thread.html', thread_id=thread_id)


@app.route("/show_thread/<int:thread_id>")
def show_thread(thread_id):
    # Call Function to Retrieve Thread
    thread = dm.show_thread(thread_id)
    return jsonify(thread)


@app.route("/get_threads", methods=['GET'])
def show_threads():
    # Call Function to Retrieve All Threads
    threads = dm.show_all_threads()
    return jsonify(threads)


@app.route("/new_thread", methods=['GET'])
def new_thread():
    return render_template('new_thread.html')


@app.route("/add_thread", methods=['POST'])
def add_thread():
    # Fetch Thread Details from Website
    author = session['username']
    title = request.form.get('title')
    content = request.form.get('content')

    # Add Thread
    dm.add_thread(author, title, content)
    return redirect('/')


@app.route('/add_comment/<int:thread_id>', methods=['POST'])
def add_comment(thread_id):
    # Fetch Comment Information Form User
    author = session['username']
    content = request.form.get('content')

    # Add Comment and Return Updated Comments
    return jsonify(dm.add_comment(thread_id, author, content))


@app.route("/log_out")
def log_out():
    # Reset Login Information
    session['username'] = None
    session['password'] = None
    return redirect(url_for('begin'))


@app.route("/get_name", methods=['GET'])
def get_name():
    return session['username']


if __name__ == '__main__':
    app.run()
