DC=docker-compose -f docker-compose.yaml

build:
	$(DC) build

up:
	$(DC) up -d

down:
	$(DC) down

ps:
	$(DC) ps

logs:
	$(DC) logs

