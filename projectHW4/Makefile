PIP := venv\Scripts\pip
PYTHON3 := venv\Scripts\python

clear:
    rmdir /s /q venv

venv:
    python -m venv venv

install_requirements:
    ${PIP} install -r requirements.txt

run:
    ${PYTHON3} server.py

TESTS := venv\Scripts\pytest -v ./test_controllers.py

test:
    ${TESTS}