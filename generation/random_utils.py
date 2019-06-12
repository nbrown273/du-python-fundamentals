from urllib.request import urlopen
from unidecode import unidecode
import random
from datetime import datetime, timedelta
from faker import Faker

common_words_url = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt"
genres_url = "https://gist.githubusercontent.com/sampsyo/1241307/raw/208ab2e4b5b576ebc51d801b039f93ee2bbc33ea/genres.txt"

def load(url):
    with urlopen(url) as data:
        return {unidecode(x.decode("utf-8").strip().lower()) for x in data.readlines()}

def get_title(words, word_count=None):
    if word_count==None:
        word_count = random.randint(1, 4)
    return " ".join(random.sample(words, word_count))

get_name = Faker().name

def get_date(before = None, after = None):
    if before == None:
        before = datetime.now()
    if after == None:
        after = datetime(1980, 1, 1)
    return datetime.fromtimestamp(random.randint(int(after.timestamp()), int(before.timestamp())))

def get_duration():
    return timedelta(seconds = random.randint(60, 10*60))

def get_song(words):
    return {
        "name": get_title(words),
        "duration": get_duration(),
        "release_date": get_date()
    }