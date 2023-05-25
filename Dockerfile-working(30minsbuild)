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

# Intermediate stage for TensorFlow dependencies
FROM tensorflow/tensorflow:latest as tensorflow
RUN apt-get update && apt-get install -y libhdf5-dev


# Production stage with Nginx and Python dependencies
FROM nginx:stable-alpine as production
WORKDIR /app

# Install Python and required dependencies
RUN apk update && apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache jpeg-dev zlib-dev mariadb-dev libffi-dev openblas-dev libgfortran lapack-dev build-base openssl-dev
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk add --no-cache \
    build-base \
	hdf5-dev \
    python3-dev \
    py3-pip \
    py3-numpy \
    py3-scipy \
    py3-matplotlib \
 py3-scikit-learn
	

# Copy built assets from the build-vue stage
COPY --from=build-vue /app/dist /usr/share/nginx/html

# Copy Nginx configuration
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

# Copy Python requirements and install them
COPY ./server/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --ignore-installed -r requirements.txt
RUN pip install gunicorn

# Copy the server code
COPY ./server .

# Start Gunicorn and Nginx
CMD gunicorn -b 0.0.0.0:5000 app:app --daemon && \
      sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && \
      nginx -g 'daemon off;'