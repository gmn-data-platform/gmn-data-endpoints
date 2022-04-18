.ONESHELL:
SHELL=/bin/bash

build_all_services:
	docker-compose build

run_all_services:
	docker-compose up -d

stop_all_services:
	echo "Stopping database services"
	docker-compose down --remove-orphans

view_all_logs:
	echo "Viewing all logs"
	docker-compos logs -f

stop_and_clean_all_services:
	read -r -p "Are you sure you want to stop and clean all services (this will remove the database volume)? [y/N] " response
	case "$response" in
		[yY][eE][sS]|[yY])
			do_something
			;;
		*)
			do_something_else
			;;
	esac
	echo "Stopping and cleaning all services"
	docker-compose down -v --rmi all

restart_all_services:
	echo "Restarting all services"
	docker-compose restart
