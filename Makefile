DC=docker-compose -f docker-compose.yaml

.PHONY: help
help: ## 지금 보고계신 도움말
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: build
build: ## 빌드
	$(DC) build

.PHONY: up
up: ## 실행
	$(DC) up -d

.PHONY: down
down: ## 종료
	$(DC) down

.PHONY: ps
ps: ## 실행중인 컨테이너 확인
	$(DC) ps

.PHONY: logs
logs: ## 로그 확인
	$(DC) logs
