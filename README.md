create  python env
'''
virtualenv venv -p python3.11
'''
activate venv
'''
venv\Scripts\activate.bat
'''
install packages
'''
pip install -r requirements.txt
'''
set debug =true
'''
set FLASK_DEBUG=1
'''




docker image 
docker build -t flask-blog .

docker run -p 5000:5000 flask-blog
docker ps
