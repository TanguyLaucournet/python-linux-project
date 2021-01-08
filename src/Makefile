.PHONY:  help virtual install 

PYTHON = python3
VENV_NAME?=venv
virtual: .venv/bin/pip # Creates an isolated python 3 environment

.venv/bin/pip:
	virtualenv -p /usr/bin/python3 .venv

install:
	.venv/bin/pip3 install -Ur requirements.txt




.DEFAULT: help
help:
	@echo "make exe_1"
	@echo "       run Socket programming exercice"
	@echo "make exe_2"
	@echo "       run Shared memory exercice"
	@echo "make exe_3"
	@echo "       run Semaphore exercice + Extended"
	@echo "make exe_4"
	@echo "       run Signal exercice"
	@echo "make compile"
	@echo "       compile py files to pyc"
	@echo "make clear"
	@echo "       clean all compiled files (pyc files)"
	@echo "make check"
	@echo "       check python version"

exe_1: Socket_programming/server.py  Socket_programming/client.py 
	$(PYTHON) Socket_programming/server.py & $(PYTHON) Socket_programming/client.py
	
exe_2: Shared_memory/server.py Shared_memory/client.py
	$(PYTHON) Shared_memory/server.py & Shared_memory/client.py

exe_3: Semaphore/server.py
	$(PYTHON) Semaphore/server.py
	@echo "Launching extended version"
	$(PYTHON) Semaphore/server2.py

exe_4: Signal/signalex.py
	$(PYTHON) Signal/signalex.py

compile:
	$(PYTHON) -m compileall .

clear:
	
	find . -type f -name '*.pyc' -delete

check:
	
	PYTHON_VERSION=$(shell $(PYTHON) -c 'import sys; print("%d.%d"% sys.version_info[0:2])' )

clean_venv:
	rm -rf .venv
#install: requirements.txt
#	pip3 install -r requirements.txt

	
