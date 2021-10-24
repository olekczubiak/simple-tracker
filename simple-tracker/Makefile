run-db:
	docker run --name simple-tracker-db -p 5432:5432 -e POSTGRES_PASSWORD=mysuperpassword -e POSTGRES_DB=simple-tracker -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres

run-pgagmin:
	docker run --name pgadmin -e "PGADMIN_DEFAULT_EMAIL=name@example.com" -e "PGADMIN_DEFAULT_PASSWORD=admin" -p 5050:80 -d dpage/pgadmin4 
