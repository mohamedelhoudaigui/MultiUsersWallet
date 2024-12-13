dup:
	docker-compose up --build

dwn:
	docker-compose down

dbl:
	docker-compose build --no-cache

dps:
	docker-compose ps

re: dwn dbl dup

log:
	docker-compose logs
