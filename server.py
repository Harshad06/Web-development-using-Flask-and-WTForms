from flask import Flask, render_template, request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

@app.route('/')
def home():
    return '<h2>Hello Pythoneer!</h2>'

@app.route('/about')
def about():
    return 'The About Page...'

@app.route('/blog')
def blog():
    posts = [{'title':'Science and Technology', 'Author':'Joy'},
              {'title':'Fiction', 'Author':'Jim'}]
    return render_template("blog.html", author="Joy", sunny=True, post=posts)

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is my Blog post ' + blog_id


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)


if __name__=="__main__":
    app.run(debug=True)