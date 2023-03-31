import time

from flask import Flask, render_template, request
from wtforms import FileField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from imageprocessing import ProcessImage
import os

app = Flask(__name__)
app.secret_key = "asdklfjoooiwjedlkjxcvmkjlfs"
process_image = ProcessImage()


class GetPhoto(FlaskForm):
    photo = FileField(validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=['POST', 'GET'])
def home():
    form = GetPhoto()
    colors = []
    if request.method == "POST" and form.validate_on_submit:
        image = request.files['photo']
        image_name = secure_filename(image.filename)
        image.save(image_name)
        top10 = process_image.get_top_10(image_name)
        colors = top10
        if os.path.isfile(f"./{image_name}"):
            os.remove(f"./{image_name}")

    return render_template('home.html', form=form, colors=colors)


if __name__ == "__main__":
    app.run(debug=True)
