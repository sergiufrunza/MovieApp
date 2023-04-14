# Fetching the latest nginx image
FROM public.ecr.aws/nginx/nginx:1.24-alpine

# Removing default nginx.conf
RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-enabled