from flask import render_template
import random
from .models import Quotes
from .forms import QuoteForm
from helloapp import app, db

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/hello/<string:username>/')
def hello_user(username):

    quotes = Quotes.query.all()
    quotes = [ quote.quotestring for quote in quotes]

    random_quote = random.choice(quotes)

    return render_template('hello_user.html', username=username, quote=random_quote)

@app.route('/quotes/')
def display_quotes():

    quotes = Quotes.query.all()
    quotes = [ quote.quotestring for quote in quotes]

    return render_template('quotes.html', quotes=quotes)

## Define below a view function 'add_quote', which renders 'addquote.html' template that displays the form , QuoteForm
## The form takes a quote and it's author information and submit's it to server.
## The server process the input data and if found valid, the data is inserted into quotes table.
## and finally renders 'addquote_confirmation.html' template.
## In case if any error is found in input, it renders 'addquote.html' template highlighting errors.
## that displays all the quotes present in 'quotes' list in a unordered list.

@app.route('/addquote/', methods=['GET', 'POST'])
def add_quote():
  form = QuoteForm()
  render_template('addquote.html', form=form)
  if form.validate_on_submit():
      Quote = Quotes(quoteauthor=form.qauthor.data, quotestring=form.qstring.data)
      try:
           db.session.add(Quote)
           db.session.commit()
           return render_template('addquote_confirmation.html', form = form)
      except Exception:
           db.session.rollback()
  else:
      return render_template('addquote.html', form=form)




