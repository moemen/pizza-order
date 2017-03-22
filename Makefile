up:
	docker-compose -f dev.yml up -d $(filter-out $@,$(MAKECMDGOALS))

build:
	docker-compose -f dev.yml build $(filter-out $@,$(MAKECMDGOALS))

run:
	docker-compose -f dev.yml run --rm $(filter-out $@,$(MAKECMDGOALS))

restart:
	docker-compose -f dev.yml restart $(filter-out $@,$(MAKECMDGOALS))

shell:
	docker-compose -f dev.yml run --rm django python manage.py shell_plus

bash:
	docker-compose -f dev.yml run --rm django bash

makemigrations:
	docker-compose -f dev.yml run --rm django python manage.py makemigrations $(filter-out $@,$(MAKECMDGOALS))

migrate:
	docker-compose -f dev.yml run --rm django python manage.py migrate $(filter-out $@,$(MAKECMDGOALS))

urls:
	docker-compose -f dev.yml run --rm django python manage.py show_urls

logs:
	docker-compose -f dev.yml logs -f --tail=70 $(filter-out $@,$(MAKECMDGOALS))

test:
	docker-compose -f dev.yml run --service-port --rm django python manage.py test $(filter-out $@,$(MAKECMDGOALS))

debug:
	docker-compose -f dev.yml run --service-port --rm $(filter-out $@,$(MAKECMDGOALS))
