# Bitcoin Alert Project Make File

VIRTUALENV = $(shell which virtualenv)
REDIS = redis-stable

clean: # shutdown
	rm -fr microservices.egg-info
	rm -fr venv

venv:
	$(VIRTUALENV) venv

install: clean venv
	. venv/bin/activate; python setup.py install
	# . venv/bin/activate; python setup.py develop

launch: venv # shutdown
	. venv/bin/activate; python server.py &

shutdown:
	ps -ef | grep "server.py" | grep -v grep | awk '{print $$2}' | xargs kill

tox:
	. venv/bin/activate; tox

redis: bin/redis-server
	# bin/redis-server path/to/redis.conf
	bin/redis-server

bin/redis-server: src/$(REDIS)/src/redis-server
	mkdir -p bin
	cp $< $@

src/$(REDIS)/src/redis-server: src/$(REDIS)/README
	cd src/$(REDIS) && make

src/$(REDIS)/README: src/$(REDIS).tar.gz
	cd src && tar -xvf $(REDIS).tar.gz
	@touch $@ # Ensure we do not untar every time, by updating README time.

src/$(REDIS).tar.gz:
	mkdir -p src
	cd src && wget http://download.redis.io/$(REDIS).tar.gz

clean:
	rm -fr bin/redis-server src/$(REDIS)*
