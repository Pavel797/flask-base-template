# navigator_bot

## Requirements

* [Docker](https://docs.docker.com/install/)
* [Docker-compose](https://docs.docker.com/compose/install/)

## Run

### Develop
```bash
docker-compose up
```

### Deploy
```bash
docker-compose -f docker-compose.yml build
cp navigator_bot.service.example navigator_bot.service
sed -i -e 's\{{path_to_project}}\'$PWD'\g' navigator_bot.service
cp navigator_bot.service /etc/systemd/system/
systemctl enable navigator_bot.service
systemctl start navigator_bot.service
```
