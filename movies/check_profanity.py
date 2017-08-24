import urllib.request

def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

def check_profanity():
    connection = urllib.request.urlopen("http://qawww.shiant.com")
    print(connection.read())


check_profanity()