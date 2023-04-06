#!/usr/bin/env bash

# Setup web server to serve static files
if ! [ -x "$(command -v nginx)" ]; then
    apt-get update && apt-get -y install nginx
fi
mkdir -p /data/web_static/{releases/test,shared}
echo "Testing 123" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n' /etc/nginx/sites-available/default
service nginx restart
