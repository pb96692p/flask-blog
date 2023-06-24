
# Flask Blog

This project is Flask based API  to run this app locally take these steps





## Deployment

To deploy this project run Create environment

```bash
 virtualenv venv -p python3.11
```

activate venv
```
venv\Scripts\activate.bat
```
install packages
```
pip install -r requirements.txt
```
set debug =true

```
set FLASK_DEBUG=1
```


## Docker Deployment
* NOTE: Docker Desktop is needed to run with docker 

create Docker Image
```bash
docker build -t flaskapp .
```
run the image 
```bash
docker run -p 5000:5000 flaskapp
```
