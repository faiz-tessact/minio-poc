FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY conf/proxy.conf /etc/nginx/conf.d/default.conf
#RUN rm /etc/nginx/sites-enabled/default
#ADD sites-enabled/ /etc/nginx/sites-enabled
