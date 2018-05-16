import app


class TestIntegration():
    """
    Here is a good post I read on flask later to understand how to test things properly
    http://kronosapiens.github.io/blog/2014/08/14/understanding-contexts-in-flask.html
    """
    def test_form_word_count(self):
        response = self.client.get("/")
        assert "<title>The Voxy Word Count App</title>" in response.data.decode()

    # Lets try posting some data to the form and call the submit thingy
    def test_form_submit(self):
        # What about creating a request context or application context?
        # Those are created and destroyed as the post request is made. See the blog post for
        # understanding this concept better.
        expected_number_words = 3
        response = self.client.post("/submit", data=dict(text="foo bar bam"))
        assert app._success_message_tempate.format(expected_number_words) in response.data.decode()

    def test_form_no_words(self):
        response = self.client.post("/submit")
        assert app._err_message_tempate in response.data.decode()

    def setup_method(self, _):
        app.wordcount.config['WTF_CSRF_ENABLED'] = False
        app.wordcount.config['TESTING'] = True
        self.client = app.wordcount.test_client()

    def teardown_method(self, _):
        print("Nothing to teardown..")