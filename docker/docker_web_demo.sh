#!/usr/bin/env bash
#
# This script will automatically pull docker image from DockerHub, and start a daemon container to run the Aegis-Chat web-demo.

IMAGE_NAME=aegisllm/aegis:cu117
AEGIS_CHECKPOINT_PATH=/path/to/Aegis-7B-Chat
PORT=8901
CONTAINER_NAME=aegis

function usage() {
    echo '
Usage: bash docker/docker_web_demo.sh [-i IMAGE_NAME] -c [/path/to/Aegis-Chat] [-n CONTAINER_NAME] [--port PORT]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -i | --image-name )
            shift
            IMAGE_NAME=$1
            ;;
        -c | --checkpoint )
            shift
            AEGIS_CHECKPOINT_PATH=$1
            ;;
        -n | --container-name )
            shift
            CONTAINER_NAME=$1
            ;;
        --port )
            shift
            PORT=$1
            ;;
        -h | --help )
            usage
            exit 0
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

if [ ! -e ${AEGIS_CHECKPOINT_PATH}/config.json ]; then
    echo "Checkpoint config.json file not found in ${AEGIS_CHECKPOINT_PATH}, exit."
    exit 1
fi

sudo docker pull ${IMAGE_NAME} || {
    echo "Pulling image ${IMAGE_NAME} failed, exit."
    exit 1
}

sudo docker run --gpus all -d --restart always --name ${CONTAINER_NAME} \
    -v /var/run/docker.sock:/var/run/docker.sock -p ${PORT}:80 \
    --mount type=bind,source=${AEGIS_CHECKPOINT_PATH},target=/data/shared/Aegis/Aegis-Chat \
    -it ${IMAGE_NAME} \
    python web_demo.py --server-port 80 --server-name 0.0.0.0 -c /data/shared/Aegis/Aegis-Chat/ && {
    echo "Successfully started web demo. Open 'http://localhost:${PORT}' to try!
Run \`docker logs ${CONTAINER_NAME}\` to check demo status.
Run \`docker rm -f ${CONTAINER_NAME}\` to stop and remove the demo."
}
