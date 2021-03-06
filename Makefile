install:
	python setup.py install

install-dev:
	pip install -qr requirements.development.txt

check:
	pyflakes ./
	pep8 --repeat --show-source ./

test:
	PYTHONPATH=".:${PYTHONPATH}" python tests/manage.py test --verbosity=2

publish:
	python setup.py sdist upload

.PHONY: check install install-dev publish test
