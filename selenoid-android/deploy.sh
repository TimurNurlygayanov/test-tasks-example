# Upload image for selenoid sessions
# docker pull selenoid/android:10.0
# docker pull selenoid/video-recorder

# Stop selenoid
docker compose down

# Stop and delete all running docker containers
export DOCKER_CONTAINERS=$(docker ps -a | awk '{ print $1 }' | grep -v CONT)
for i in $DOCKER_CONTAINERS ; do docker stop $i && docker rm $i ; done

# Run selenoid containers
docker-compose up -d
