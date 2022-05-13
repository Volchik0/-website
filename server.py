from flask import Flask, render_template, url_for, request


app = Flask(__name__)


@app.route('/')
@app.route("/site")
def index():
    return render_template("index.html")


@app.route("/day-<num>")
def days(num):
    return render_template(f"day-{num}.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        print(request.form)

    return render_template('form.html')


@app.route('/profile/<username>')
def profile(username):
    for user in users:
        if user['username'] == username:
            if 'logged_in' in session:
                if session['logged_in'] == username:
                    return render_template('profile.html', username=username)
                else:
                    abort(403)
            flash('Вам туда нельзя. Зарегистрируйтесь!', category='error')
            return redirect(url_for('login'))
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
