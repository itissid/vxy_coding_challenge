from flask import Flask, flash
from flask import render_template
from config import Config
from flask_bower import Bower

from voxy.app.forms import WordCountForm
from voxy.wordcount.wordcount import count_words

wordcount = Flask(__name__, static_url_path='')
Bower(wordcount)
wordcount.debug = True
wordcount.config.from_object(Config)


@wordcount.route('/', methods=["GET", "POST"])
def index():
    form = WordCountForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        word_count = count_words(form.text.data)
        flash("You submitted text data with {} words".format(word_count))
        print(wordcount)
        return render_template("index.html", title="Word Count", form=form, word_count=word_count)
    return render_template("index.html", title="Word Count", form=form)


if __name__ == '__main__':
    print("Running from main")
    wordcount.run()
