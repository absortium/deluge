# ------------------------------------
# Docker alias and function
# ------------------------------------

# Get latest container ID
alias dl="docker ps -l -q"

# Get container process
alias dps="docker ps"

# Get process included stop container
alias dpsa="docker ps -a"

# Get images
alias di="docker images"

# Get container IP
alias dip="docker inspect --format '{{ .NetworkSettings.IPAddress }}'"

# Run deamonized container, e.g., $dkd base /bin/echo hello
alias dkd="docker run -d -P"

# Run interactive container, e.g., $dki base /bin/bash
alias dki="docker run -i -t -P"

# Execute command in container, e.g., $dex base /bin/bash
alias dex="docker exec -i -t"

func_dstop() { docker stop $(docker ps -a -q); }
# Stop all containers
alias dstop=func_dstop

func_drmc() { docker ps -a | egrep "$1" | grep -v "CONTAINER" | awk '{ printf "%s\n", $1}' | xargs docker rm -f; }
# Stop and Remove choisen containers
# drmc "postgres" - delete postgres container
# drmc "[a-z]" - delete all containers
alias drmc=func_drmc

func_drmi() { docker images -a | egrep "$1" | grep -v "IMAGE" | awk '{ printf "%s\n", $3}' | xargs docker rmi -f; }
# Remove choisen images
# drmi "postgres" - delete postgres image
# drmi "[a-z]" - delete all images
alias drmi=func_drmi

func_dbu() { docker build -t=$1 .; }
# Dockerfile build, e.g., $dbu tcnksm/test 
alias dbu=func_dbu
