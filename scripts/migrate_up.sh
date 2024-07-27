docker exec $(docker ps --filter name=migrate --format "{{.ID}}") sql-migrate up --env=local --config=/migrate/dbconfig.yml
