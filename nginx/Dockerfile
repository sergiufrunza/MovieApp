# Fetching the latest nginx image
FROM public.ecr.aws/nginx/nginx:1.24-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d