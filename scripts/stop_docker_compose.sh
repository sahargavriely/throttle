#!/bin/bash -e

docker compose -f docker/compose.yaml --env-file docker/docker.env down
# Or `docker compose -f docker/compose.yaml --env-file docker.env down --rmi all` ro remove the image as well.
