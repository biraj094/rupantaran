# Project variables
PACKAGE = rupantaran  # Change this to your actual package name

# Enable debug mode (prints each command before execution)
.SHELLFLAGS = -ex

# Formatting and Linting
format:
	@echo "🛠 Formatting code with black..."
	black $(PACKAGE)
	@echo "Formattind DONE!"
lint:
	@echo "🔍 Running flake8 for linting..."
	flake8 $(PACKAGE)

# Testing and Coverage
test:
	@echo "🧪 Running tests with pytest..."
	pytest --cov=$(PACKAGE)

test-html:
	@echo "📊 Generating HTML test coverage report..."
	pytest --cov=$(PACKAGE) --cov-report=html

# Documentation
docs:
	@echo "📖 Generating documentation..."
	cd docs && make html

docs-clean:
	@echo "🗑 Cleaning documentation files..."
	cd docs && make clean

# Clean temporary files
clean:
	@echo "🗑 Removing temporary files..."
	rm -rf .pytest_cache dist build *.egg-info htmlcov
	find . -name "__pycache__" -type d -exec rm -rf {} +

# Run all checks in correct order
check: format lint test

# Run everything in the correct order
all: format lint test docs
	@echo "✅ All checks passed successfully!"

.PHONY: format lint test test-html docs docs-clean clean check all