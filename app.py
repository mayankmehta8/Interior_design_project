from flask import Flask, render_template, request, send_from_directory, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileField,FileRequired
from wtforms import SubmitField
import replicate
import os


os.environ["REPLICATE_API_TOKEN"] = "r8_Q0ac6yTAIPXXdqNRbGzqCygMp7ZooYk2X9YP5"

app = Flask(__name__)
app.secret_key= 'sadasdfasdfsa'
app.config['UPLOADED_PHOTOS_DEST']='upload'
photos= UploadSet('photos',IMAGES)
configure_uploads(app,photos)
class UploadForm(FlaskForm):
    photo= FileField(
        validators=[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File field must not be empty')
        ]
    )
    submit= SubmitField('Upload')






# Sample data for the drop-down menu
dropdown_options = ["Professional", "Comfy", "Cute"]
dropdown_options2 = ["Living Room", "Bedroom", "Backyard"]
selected_option1 =''
selected_option2=''
@app.route('/upload/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    global fname,selected_option1,selected_option2
    form =UploadForm()
    if form.validate_on_submit():
        filename=photos.save(form.photo.data)
        file_url= url_for('get_file', filename=filename)
        fname= file_url
        fname = fname[1:]
    else:
        file_url=None 
    selected_option1 = request.form.get('dropdown')
    selected_option2 = request.form.get('dropdown2')    
    return render_template('index.html', form = form, file_url=file_url, dropdown_options=dropdown_options, dropdown_options2=dropdown_options2)
@app.route('/output', methods=['GET','POST'])
def output():
    image_file=open(fname, "rb")
    output = replicate.run(
            "jagilley/controlnet-hough:854e8727697a057c525cdb45ab037f64ecca770a1769cc52287c2e56472a247b",
        input={
            "image": image_file,
            "prompt": f"{selected_option1} {selected_option2} Editorial Style Photo, Symmetry, Straight On, Modern Living Room, Large Window, Leather, Glass, Metal, Wood Paneling, Neutral Palette, Ikea, Natural Light, Apartment, Afternoon, Serene, Contemporary, 4k",
            "a_prompt": "best quality, extremely detailed, photo from Pinterest, interior, cinematic photo, ultra-detailed, ultra-realistic, award-winning"
        }
        )
    
    source=output[1]
    source1=output[0]
    return render_template("Output.html", source=source, source1=source1)
if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
