echo Info :- Local docker registry should be running for this to work

sudo docker-compose --env-file env-vagrant.txt --file docker-compose-template.yml up
