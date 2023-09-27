from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def home():
    """Returns home page with story form"""

    return render_template("questions.html", prompts=silly_story.prompts)

@app.get("/results")
def results():
    """Returns results page with filled story"""

    return render_template("results.html",
                           story=silly_story.get_result_text(request.args))