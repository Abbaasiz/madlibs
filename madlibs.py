from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_word(word_type):
    """ Function to get a random word basedon the type. """
    words = {
        'noun': ['dog', 'car', 'banana', 'mountain', 'cookie', 'cat', 'chair'],
        'verb': ['run', 'jump', 'bite', 'drink', 'drive'],
        'adjective': ['big', 'yellow', 'quick', 'lazy', 'funny'],
        'adverb': ['quickly', 'lazily', 'happily', 'sadly', 'slowly'],
        'place': ['park', 'restaurant', 'school', 'zoo', 'museum'],
        'exclamation': ['Wow', 'OH NO', 'HOORAY', 'YIKES', 'OOPS'],
    }
    return random.choice(words[word_type])

def create_story():
    """ Function to create a random story based on a template """
    story_template = (
        "{exclamation}! Today I went to the {place} and I saw  a very {adjective} {noun}. "
        "It was {verb}ing around {adverb}! I couldn't beleive my eyes soi decided to "
        "{verb} along with it. What a day!"
    )

    # Replace placeholders with random words
    story = story_template.format(
        exclamation=get_word('exclamation'),
        place=get_word('place'),
        adjective=get_word('adjective'),
        noun=get_word('noun'),
        adverb=get_word('adverb'),
        verb=get_word('verb')
    )

    return story

@app.route('/')
def home():
    return create_story()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)