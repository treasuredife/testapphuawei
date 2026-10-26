#!/bin/bash
# Paste into the AS configuration's user data. Edit the 4 variables below.
REGION="af-south-1"
IMAGE="swr.${REGION}.myhuaweicloud.com/YOUR_ORG/docker-lab:v1"
# Copy this line from SWR console > Image Resources > Generate Login Command (long-term)
SWR_LOGIN='docker login -u YOUR_LOGIN_USER -p YOUR_LOGIN_PASSWORD swr.af-south-1.myhuaweicloud.com'

if ! command -v docker >/dev/null 2>&1; then
  apt-get update -y && apt-get install -y docker.io
fi
systemctl enable --now docker
eval "$SWR_LOGIN"
docker rm -f app 2>/dev/null
docker pull "$IMAGE"
docker run -d --name app --restart always -p 80:8080 "$IMAGE"
