from flask import Flask, render_template, request, jsonify
import config.database as DataLogin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        dataRegis = request.json
        email = dataRegis.get('email')
        passWord = dataRegis.get('password')
        
        if email and passWord:
            try:
                db_regis = DataLogin.Database()
                db_regis.insert(email, passWord)
                return jsonify(status='success', message='Registration is successful, please go to the login page')
            except Exception as e:
                return jsonify(status='error', message=str(e))
        else:
            return jsonify(status='error', message='Invalid credentials')
        
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        dataLogin = request.json
        email = dataLogin.get('email')
        passWord = dataLogin.get('password')
        
        if email and passWord:
            try:
                db_login = DataLogin.Database()
                result = db_login.select(email, passWord)
                
                if result:
                    return jsonify(status='success'), 200
                else:
                    return jsonify(status='error', message='Invalid credentials'), 400
            except Exception as e:
                return jsonify(status='error', message=str(e))
        else:
            return jsonify(status='error', message='Invalid credentials'), 400
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0'
    )