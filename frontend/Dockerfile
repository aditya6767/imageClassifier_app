FROM node:14.17-alpine
WORKDIR /code
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]