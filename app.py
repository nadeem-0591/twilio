from flask import Flask, render_template, request
from twilio.rest import Client

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    message = request.form['message']
    
    account_sid = 'AC58f5ea5f9ab7fefd024602e426190905'
    auth_token = '55427144a89bf386a78146e52ce96725'
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=message,
    to='whatsapp:+917396097276'
    )
    
    return 'Message sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
