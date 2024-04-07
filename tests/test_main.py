from App import MainApp

def test_message():
    app = MainApp()
    assert app.get_greeting() == "Message for testing from github actions"