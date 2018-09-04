from flask import Flask, render_template, request
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, SubmitField

app = Flask(__name__)

list_centers = [{"name": "Biomass Ergonomics Lab", "img": "laptop0.jpg", "director": "Juan Rulfo, PhD"},
                {"name": "Magnetronic Disphoria Center", "img": "laptop1.jpg"},
                {"name": "Arthropod Genome Project", "img": "laptop2.jpg", "director": "Prof. Margareta Philo"}
               ]


@app.route('/')
def index():
    return render_template('index.html', img=list_centers[0]["img"])


@app.route('/signup')
def signup():
    return render_template('signup.html', img=list_centers[0]["img"])


@app.route('/thankyou')
def thankyou():
    center_name = request.args.get('center_name')
    director = request.args.get('director')
    comment = ''
    if 'PhD' in director:
        comment='Aha! A qualified academic administrator!'
    else:
        comment='(Temporarily until we find a fully academically qualified adminstrator)'
    return render_template('thankyou.html', comment=comment,center_name=center_name, director=director,  img=list_centers[0]["img"])


@app.route('/centers/<int:idx>')
def centers(idx):
    center_name = list_centers[idx]["name"]
    img = list_centers[idx]["img"]
    return render_template('index.html', center_name=center_name, img=img, centers=list_centers)

@app.route('/center/<int:idx>')
def center(idx):
    return render_template('center.html', center=list_centers[idx])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__  == "__main__":
    app.run(debug=True)