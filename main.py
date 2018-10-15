from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://build-a-blog:password@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(600))


    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route("/", methods=['POST', 'GET'])
def index():
    return redirect('/blog')

@app.route("/blog")
def blog():
    
    return render_template('blog.html') #Maybe include blogs=blogs if relevant error occurs

@app.route("/newpost", methods=['GET', 'POST'])
def newpost():
    if request.method == "POST": 
        blog_title = request.form['blog-title']
        blog_body = request.form['blog-body']
        new_post = Blog(blog_title, blog_body)
        db.session.add(new_post)
        db.session.commit()

        blogs = Blog.query.all()
        return render_template("blog.html",title="Blogs in Space", blogs=blogs) #Maybe include blogs=blogs if relevant error occurs
    return render_template('newpost.html')

if __name__ == ('__main__'):
    app.run()