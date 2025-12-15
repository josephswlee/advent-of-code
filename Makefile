# Variables
VENV_DIR := .venv
PYTHON := python3
UV := uv

# Default target
.PHONY: all
all: install

# 1. SETUP: Create .venv if it doesn't exist
# We point to the directory itself as a target so Make knows when it's created.
$(VENV_DIR):
	@echo "Creating virtual environment in $(VENV_DIR)..."
	$(UV) venv $(VENV_DIR) --python $(PYTHON)

.PHONY: setup
setup: $(VENV_DIR)

# 2. INSTALL: Install dependencies from uv.lock
# We depend on 'setup' to ensure venv exists first.
# 'uv sync' is the command to install strict dependencies from uv.lock.
.PHONY: install
install: setup
	@echo "Syncing dependencies from uv.lock..."
	$(UV) sync --frozen

# 3. CLEAN: Remove venv and cache
.PHONY: clean
clean:
	@echo "Cleaning up environment and cache..."
	rm -rf $(VENV_DIR)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "Clean complete."
