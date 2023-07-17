# Удалить/очистить все данные Докера (контейнеры, образы, тома и сети)

## Одной строкой

```bash
docker stop $(docker ps -qa) | docker rm $(docker ps -qa) | docker rmi -f $(docker images -qa) | docker volume rm $(docker volume ls -q) | docker network rm $(docker network ls -q)
```
## Удаление закрытие

### 👊 

```bash
docker system prune
```

### 👊👊: Очистка всех остановленных контейнеров и неиспользуемых образов (а не только образов, не связанных с контейнерами)
```bash
docker system prune -a
```

### :thumbsdown: Остановка всех контейнеров

```bash
docker stop $(docker ps -qa)
```

### :fist: Удаление всех контейнеров

```bash
docker rm $(docker ps -qa)
```

### :v: Удаление всех образов

```bash
docker rmi -f $(docker images -qa)
```

### :wave: Удаление всех томов

```bash
docker volume rm $(docker volume ls -q)
```

### :hand: Удаление всех сетей

```bash
docker network rm $(docker network ls -q)
```

> Ваша инсталяция должна быть чиста :blush:

## Просмотр/сборка:

### :point_down: Остановить и пересобрать образ не трогая инфу в томах
```bash
 docker-compose up -d --no-deps --build
```
### :point_down: Открыть логи запущенного контейнера
```bash
 docker compose logs -f
```
### :point_down: Показать существующие контейнеры
```bash
docker ps -a
```
### :point_down: Показать собранные образы
```bash
docker images -a 
```
### :point_down: Показать смонтированные тома
```bash
docker volume ls
```

### :point_right: Следующая команда показывает только сети по умолчанию:

```bash
docker network ls
```

