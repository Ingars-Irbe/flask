from flask import Flask, render_template
from file_procs import read_file

app = Flask(__name__)

@app.route('/')
def getIndex():
  return "Hi!"

@app.route('/home')
def getHome():
  return render_template('home.html', active_page = 'home')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = '123')

@app.route('/read_file')
def read_form_file():
  file_content = tead_file()
  return file_content

@app.route('/write_to_file', methods)

if __name__== '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5050, debug=True)