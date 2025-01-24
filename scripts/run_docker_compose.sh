#!/bin/bash -e

docker compose -f docker/compose.yaml --env-file docker/docker.env up -d --build
# To enter shell in a container `docker exec -it <container-name> sh`
# To rebuild this image you must use `docker compose -f docker/compose.yaml build` or `docker compose -f dockerß/compose.yaml up --build` to run the image as well.
