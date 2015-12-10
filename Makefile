install: logs venv db

logs: 
	sudo mkdir -m 775 -p /var/log/phl-microsat
	sudo touch /var/log/phl-microsat/storage-api.uwsgi.log
	sudo touch /var/log/phl-microsat/storage-api.uwsgi.logi
	sudo chmod 775 /var/log/phl-microsat/storage-api.uwsgi.log
	sudo chmod 775 /var/log/phl-microsat/storage-api.uwsgi.logi

	sudo chown $(USER):$(USER) /var/log/phl-microsat/storage-api.uwsgi.log
	sudo chown $(USER):$(USER) /var/log/phl-microsat/storage-api.uwsgi.logi

uwsgi:
	sudo apt-get install build-essential python-dev

venv: uwsgi 
	virtualenv env
	env/bin/pip install -r requirements.txt
	env/bin/nosetests -v

db:
	env/bin/python create_db.py

config:
	cp -nvp uwsgi.config.ini.sample uwsgi.config.ini
