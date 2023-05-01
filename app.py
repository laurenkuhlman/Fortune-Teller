# Import the Flask library
from flask import Flask, render_template, request

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the root URL
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for the fortune URL
@app.route('/fortune', methods=['POST'])
def fortune():
    user = request.form['user']
    color = request.form['color']
    number = request.form['number']

    if color == 'red' and number == '1':
        fortune_string = 'Your future is full of possibilities.'
    elif color == 'red' and number == '2':
        fortune_string = 'You will have great success in life.'
    elif color == 'red' and number == '3':
        fortune_string = 'Your dreams will come true.'
    elif color == 'red' and number == '4':
        fortune_string = 'You will be rewarded for your hard work.'
    elif color == 'yellow' and number == '1':
        fortune_string = 'You will find love and happiness in the near future.'
    elif color == 'yellow' and number == '2':
        fortune_string = 'You will have a long and prosperous life.'
    elif color == 'yellow' and number == '3':
        fortune_string = 'You will make a great impact on the world.'
    elif color == 'yellow' and number == '4':
        fortune_string = 'You will find the answer to your problems.'
    elif color == 'blue' and number == '1':
        fortune_string = 'You will be surrounded by positive people.'
    elif color == 'blue' and number == '2':
        fortune_string = 'You will learn something new every day.'
    elif color == 'blue' and number == '3':
        fortune_string = 'You will have a bright future.'
    elif color == 'blue' and number == '4':
        fortune_string = 'You will achieve great things.'
    elif color == 'green' and number == '1':
        fortune_string = 'You will have a strong and supportive network.'
    elif color == 'green' and number == '2':
        fortune_string = 'You will find joy in the little things.'
    elif color == 'green' and number == '3':
        fortune_string = 'You will have a positive outlook on life.'
    elif color == 'green' and number == '4':
        fortune_string = 'You will be rewarded for your kindness.'
    else:
        fortune_string = 'Error: no fortune selected'

    return render_template('fortune.html', user=user, fortune=fortune_string)

# Run the app on port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)