from voxy.wordcount.wordcount import count_words


def test_word_count():
    test_text = """This is a text with some punctuations. And some new lines
                    and plenty of spaces."""
    expected_count = 15
    actual_count = count_words(test_text)
    assert actual_count == expected_count

