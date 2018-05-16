from flask import Flask, flash, make_response, request, redirect, url_for
from flask import render_template
from config import Config
from flask_bower import Bower

from voxy.app.forms import WordCountForm
from voxy.wordcount.wordcount import count_words

wordcount = Flask(__name__, static_url_path='')
Bower(wordcount)
wordcount.debug = True
wordcount.config.from_object(Config)


@wordcount.route('/', methods=["GET"])
def index():
    form = WordCountForm()
    return render_template("index.html", title="Word Count", form=form, is_init=True)

_err_message_tempate = "You must submit some words to count!"
_success_message_tempate = "You submitted text data with {} words"
# TODO: Would like to have some kind of a word/data limit on what can be submitted.
@wordcount.route('/submit', methods=["GET","POST"])
def submit():
    if request.method == "GET":
        return redirect(("/"))

    form = WordCountForm()
    print(form.validate_on_submit())

    if form.validate_on_submit():
        word_count = count_words(form.text.data)
        flash(_success_message_tempate.format(word_count))
        print(wordcount)
        return render_template("index.html", title="Word Count", form=form, word_count=word_count)
    flash(_err_message_tempate)
    return render_template("index.html", title="Word Count", form=form)

if __name__ == '__main__':
    print("Running from main")
    wordcount.run()
