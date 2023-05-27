# Build stage for Vue.js application
FROM node:20 as build-vue

WORKDIR /app

# Copy and install dependencies
COPY ./package*.json ./
RUN npm install

# Copy the Vue.js application code
COPY . .

# Build the Vue.js application
RUN npm run build