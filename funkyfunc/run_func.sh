#!/bin/bash

/usr/bin/docker build . --tag=func

trap '/usr/bin/docker stop func' SIGINT SIGTERM

while true
do
    /usr/bin/docker run --rm -d --name func -p 1337:1337 -p 31337:31337 func
    /usr/bin/sleep 1500
    /usr/bin/docker stop func
done
