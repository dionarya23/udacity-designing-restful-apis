from flask import Flask
app = Flask(__name__)

@app.route('/puppies')
def puppiesFunction():
    return "Yes, Puppies!!"

@app.route('/puppies/<int:id>')
def puppiesFunctionId(id):
    return "This method will act on the puppy id %s"% id

@app.route('/')
def home():
    return "hello World I am Home"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
