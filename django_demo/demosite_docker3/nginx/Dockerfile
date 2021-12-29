# pull image
FROM nginx:latest
# copy file to docker
COPY nginx.conf /etc/nginx/nginx.conf
COPY my_nginx.conf /etc/nginx/sites-available/
# create sites-enabled and connect my_nginx.conf
RUN mkdir -p /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/
# exec to start nginx
CMD ["nginx", "-g", "daemon off;"]