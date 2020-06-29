run:
	docker-compose up

test:
	docker-compose up -d
	docker exec flask_api_1 pytest

pylint:
	docker-compose up -d
	docker exec flask_api_1 pylint --load-plugins pylint_flask_sqlalchemy app.py

