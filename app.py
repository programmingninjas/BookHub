from flask import Flask,render_template,redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from downloader import download
from urllib.parse import urlparse

app = Flask(__name__)
app.config['SECRET_KEY'] = "@programmingninjas"

class book_form(FlaskForm):
    
    book_link = StringField("book link", validators=[DataRequired()])
    submit = SubmitField("Submit")

book_link = None

@app.route('/',methods=['GET','POST'])
def song():

    form = book_form()    

    if form.validate_on_submit():

        book_link = form.book_link.data   #book_link or book_name

        try:
            
            download_link = download(book_link)

            return redirect(download_link)

        except:
            
            return render_template("notfound.html")

        
    return render_template("home.html",form=form)

if __name__ == '__main__':

    app.run()