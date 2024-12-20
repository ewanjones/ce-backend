REQ_FILE = requirements.txt
VENV_DIR = venv

$(VENV_DIR):
	python3 -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)"


.PHONY: install
install: $(VENV_DIR)
	$(VENV_DIR)/bin/pip3 install -r $(REQ_FILE)
	@echo "Dependencies installed from $(REQ_FILE)"
