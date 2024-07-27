docker exec $(docker ps --filter name=migrate --format "{{.ID}}") sql-migrate down --env=local --config=/migrate/dbconfig.yml
