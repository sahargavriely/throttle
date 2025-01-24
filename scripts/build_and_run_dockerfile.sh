docker build -f docker/Dockerfile -t tenable .

# you might want to expose some ports using the -p flag
docker run -ti --rm --name my-tenable -v ./shared:/shared tenable
# you might want to connect time volumes with '-v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro -v /usr/share/zoneinfo:/usr/share/zoneinfo:ro'
