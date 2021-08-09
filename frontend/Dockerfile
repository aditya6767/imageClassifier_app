FROM node:14.17-alpine
WORKDIR /code
ENV PATH ./node_modules/.bin:$PATH
COPY . .
RUN npm run build
CMD ["npm", "start"]



# FROM node:16.6.1-alpine
# WORKDIR /app
#
# COPY frontend/package.json ./
# COPY frontend/package-lock.json ./
#
# RUN npm install -g npm@7.20.5
# RUN npm install react-scripts -g
#
# COPY frontend/ /app
#
# CMD ["npm", "start"]