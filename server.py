from usuarios_app.controllers import users
from usuarios_app import app

if __name__ == "__main__":
    app.run(debug=True)

from server import app as application
if __name__ == "__main__":
    application.run()

[Unit]
Description=Gunicorn instance
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/user_template_flask
Environment="PATH=/home/ubuntu/user_template_flask/venv/bin"
ExecStart=/home/ubuntu/user_template_flask/venv/bin/gunicorn --workers 3 --bind unix:user_template_flask.sock -m 007 wsgi:application
[Install]
WantedBy=multi-user.target

[Unit]
Description=Gunicorn instance
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/user-template-flask
Environment="PATH=/home/ubuntu/user-template-flask/venv/bin"
ExecStart=/home/ubuntu/user-template-flask/venv/bin/gunicorn --workers 3 --bind unix:user-template-flask.sock -m 007 wsgi:application
[Install]
WantedBy=multi-user.target