#This is my makefile

SHELL=/bin/bash
INSTALL_DIR = ~/bin
WRAPPER_FILE = ${INSTALL_DIR}/find-dead-links
PY_FILE = ${INSTALL_DIR}/find-dead-link.py
ENV = ${INSTALL_DIR}/ENV

install: ${WRAPPER_FILE} ${PY_FILE} ${ENV}


${WRAPPER_FILE}: find-dead-links
	cp find-dead-links ${INSTALL_DIR}
	chmod 700 ${INSTALL_DIR}/find-dead-links

${PY_FILE}: find-dead-links.py
	cp find-dead-links.py ${INSTALL_DIR}
	chmod 700 ${INSTALL_DIR}/find-dead-links.py

${ENV}:
	virtualenv -p python3 ${ENV}
	source ${ENV}/bin/activate && pip install requests && pip install beautifulsoup4
