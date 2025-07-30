from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def show_ip():
    # Получаем IP пользователя
    user_ip = request.remote_addr
    # Получаем заголовки, которые могут указывать на прокси/VPN
    forwarded_for = request.headers.get('X-Forwarded-For', '')
    real_ip = request.headers.get('X-Real-IP', '')
    
    return f"""
    <html>
        <head><title>Ваш IP для SCCM</title></head>
        <body style="font-family: Arial; max-width: 800px; margin: 0 auto;">
            <h1>Ваш IP-адрес для подключения SCCM:</h1>
            <div style="background: #f0f0f0; padding: 20px; border-radius: 5px;">
                <p style="font-size: 24px;"><b>{user_ip}</b></p>
            </div>
            
            <h2>Дополнительная информация:</h2>
            <p>Если вы используете VPN или прокси, сообщите администратору следующие адреса:</p>
            <ul>
                <li>X-Forwarded-For: {forwarded_for if forwarded_for else 'не обнаружено'}</li>
                <li>X-Real-IP: {real_ip if real_ip else 'не обнаружено'}</li>
            </ul>
            
            <p style="margin-top: 30px; color: #666;">
                Сообщите этот IP-адрес администратору для подключения через Microsoft Configuration Manager
            </p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
