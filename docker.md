sudo docker run --gpus '"device=1"' --rm -i -d --net host {REPOSITORY}:{TAG} /bin/bash

sudo docker run --rm -i -d --net host {IMAGE ID} /bin/bash

sudo docker exec -it {CONTAINER ID} /bin/bash
