from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

stories = {"silly story": silly_story,
           "excited story": excited_story
        }

@app.get("/")
def home():
    """Returns home page with dropdown to select story"""

    return render_template("stories.html", stories=stories.keys())

@app.get("/questions")
def questions():
    """Returns questions page with story form"""

    story_key = request.args.get("story")
    story = stories.get(story_key)

    return render_template("questions.html", prompts=story.prompts, story=story_key)

@app.get("/<story>/results")
def results(story):
    """Returns results page with filled story"""

    return render_template("results.html",
                           story=stories[story].get_result_text(request.args))