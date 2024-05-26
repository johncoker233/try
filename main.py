from flask import Flask, session, redirect, url_for, request, render_template_string
from flask_session import Session

app = Flask(__name__)

# 配置 Flask-Session
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'  # 使用文件系统来存储会话数据
Session(app)

# 模板字符串，包含一个简单的登录表单
login_form = '''
    <form method="POST" action="/login">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password">
        <button type="submit">Login</button>
    </form>
'''

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f'Logged in as {username}. <a href="/logout">Logout</a>'
    return 'You are not logged in. <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template_string(login_form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
