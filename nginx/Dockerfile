# Fetching the latest nginx image
FROM public.ecr.aws/nginx/nginx:1.24-alpine

# Removing default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Copying our nginx.conf
COPY nginx.conf /etc/nginx/conf.d