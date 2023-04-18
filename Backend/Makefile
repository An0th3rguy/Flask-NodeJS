system-packages:
	apt update
	apt install python3-pip -y

python-packages:
	pip install -r requirements.txt

install: system-packages python-packages

run:
	flask run --host=0.0.0.0

db-upgrade:
	flask db upgrade

db-downgrade:
	flask db downgrade

init-db:
	flask db init
	flask db migrate --message 'initial database migration'
	make db-upgrade