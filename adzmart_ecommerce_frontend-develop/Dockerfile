FROM node:16-alpine as builder
WORKDIR /app
COPY ./package.json ./
COPY ./yarn.lock ./
#COPY ./yarn.lock ./
RUN yarn install
COPY . .
RUN yarn run build

FROM nginx:latest
#EXPOSE 8181
COPY ./nginx-default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/build /usr/share/nginx/html
