all_up:
	docker compose up --build

all_dwn:
	docker compose down

all_bl:
	docker compose build --no-cache

bup:
	docker compose up backend

bdwn:
	docker compose down backend

bbld:
	docker compose build backend

lup:
	docker compose up localnet

ldwn:
	docker compose down localnet

lbld:
	docker compose build localnet

ps:
	docker compose ps

log:
	docker compose logs
