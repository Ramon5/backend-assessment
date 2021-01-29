dev_setup:
	docker-compose build

run:
	docker-compose up

run_dev:
	docker-compose run --service-ports app

rebuild:
	docker-compose down
	docker-compose build

statics:
	docker-compose run app python manage.py collectstatic --noinput

migrate:
	docker-compose run app python manage.py makemigrations
	docker-compose run app python manage.py migrate

test: compilemessages
	docker-compose run app pytest -vv . --cov apps/

shell:
	docker-compose run app python manage.py shell_plus

super_user:
	docker-compose run app python manage.py createsuperuser

makemessages:
	docker-compose run app python manage.py makemessages --locale=pt_BR

compilemessages:
	docker-compose run app python manage.py compilemessages

format_code:
	docker-compose run app isort apps/
	docker-compose run app black apps/