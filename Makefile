run:
    ENV DB_USER=postgres
    ENV DB_PASSWORD=postgres
    ENV DB_NAME=postgres
    docker-compose up
test:
    ENV DB_USER=postgres
    ENV DB_PASSWORD=postgres
    ENV DB_NAME=postgres_test
    docker-compose exec -t app pytest

migrate:
    flask db init
    flask db migrate

pylit:
    python pylint app.py