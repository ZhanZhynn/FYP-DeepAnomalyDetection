# FYP-DeepAnomalyDetection
Deployed Machine Learning Model using Flask + Vue + Tensorflow + XAI + Gunicorn + Nginx + Docker

It's a Desktop Web App, not ready for mobile view yet.

Explanation on XAI coming soon...

This is done as a student web dev project.

## How to build project
### Node.js (Vue) + Flask (Python)
1. Download & install Python <a href ="https://www.python.org/downloads/" target="blank"> here</a>.
2. Download the LTS version of Node.js from the <a href ="" target="blank">  official website</a>.
3. Clone/Fork this repo using git bash or any methods.
4. Open the terminal in the project directory, then run the following code to get Node.js running:

#### *Install Node dependencies*
```
cd client
npm install
npm run dev
*Click on the link in the terminal to launch the web application in localhost.*
```

#### *Install Python dependencies*

Open another terminal in the project directory, then run the following code to run the Flask (Python) server:

*Recommended but optional to run this code in a python virtual environment*
```
cd server
pip install --ignore-installed -r requirements.txt
python app.py
```

## How to run project in Docker
### Docker 
Make sure you have Docker Desktop installed, if not download from <a href ="https://www.docker.com/products/docker-desktop/" target="blank"> here</a>.

First open the project in terminal, then run the following code:
```
docker build -t web-tf-nginx:latest
docker run -d --name flask-vue-tf -e "PORT=8766" -p 8008:8766 web-tf-nginx:latest
*Launch the docker container in localhost.*
```
Alternatively, you may refer this <a href ="https://testdriven.io/blog/deploying-flask-to-heroku-with-docker-and-gitlab/" target="blank"> guide</a> by testdriven.io.


## Dependencies
- Node.js 
- Python 3.10
- Docker (optional)

## References:
- https://testdriven.io/blog/deploying-flask-to-heroku-with-docker-and-gitlab/
- https://royleekiat.com/2020/11/27/how-to-deploy-your-machine-learning-web-application-vue-js-and-python-poc/
- https://github.com/ivanpanshin/flask_gunicorn_nginx_docker
