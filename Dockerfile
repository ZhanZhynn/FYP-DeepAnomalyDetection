# Build stage for Vue.js application
FROM node:20 as build-vue

WORKDIR /app

# Copy and install dependencies
COPY ./client/package*.json ./
RUN npm install

# Copy the Vue.js application code
COPY ./client .

# Build the Vue.js application
RUN npm run build

FROM nginx:stable-alpine as nginx-stage
WORKDIR /app

# Intermediate stage for TensorFlow dependencies
#python
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

#RUN adduser --system --no-create-home --disabled-login --disabled-password --group nginx
RUN useradd -ms /bin/bash nginx

# Install Nginx
RUN apt-get update && apt-get install -y nginx

#RUN rm /etc/nginx/nginx.conf
#COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

# remove the default nginx.conf and replace with the one from alpine image. Default conf is causing issues
COPY --from=nginx-stage /etc/nginx/nginx.conf /etc/nginx/nginx.conf

# Copy the Nginx configuration file
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

# Copy built assets from the build-vue stage
COPY --from=build-vue /app/dist /usr/share/nginx/html

# Copy Python requirements and install them
COPY ./server/requirements.txt .
RUN pip install --upgrade pip
RUN pip install tensorflow-cpu --no-cache-dir
RUN pip install --ignore-installed -r requirements.txt

# Copy Python requirements and install them
RUN pip install gunicorn

# Copy the server code
COPY ./server .


# Start Gunicorn and Nginx
CMD gunicorn -b 0.0.0.0:5000 app:app --daemon && \
     sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && \
     nginx -g 'daemon off;'


