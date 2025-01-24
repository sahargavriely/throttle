#!/bin/bash

if docker run --detach -p 6379:6379 -p 8001:8001 --hostname my-redis --name redis redis/redis-stack:latest 2> /dev/null; then
    echo 'Built and started redis-stack from scratch'
else
    docker restart redis &> /dev/null;
    echo 'Started redis-stack from existing image'
fi

echo 'Serving HTTP on 127.0.0.1 port 8001 (http://127.0.0.1:8001/)'
