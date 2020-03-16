from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/tuto/')
def home():
	return render_template('le_tuto_entier.html')


@app.route('/contact/')
def contact():
	return render_template('contact.html')



if __name__ == '__main__':
	app.run(debug=True)

@app.errorhandler(404)
def page_not_found(erreur_404):
    return render_template('erreur_404.html'), 404
