##───────────────────
##     Targets 
##───────────────────

.PHONY: default help all install dist hooks format lint test check clean artifact docs docs-clean check-docs

PACKAGE_NAME = velvetlib

help: ## Display this message
	@grep -E '(^[a-zA-Z0-9_\.\-]+:.*?##.*$$)|(^##)' Makefile \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[34m%-30s\033[0m %s\n", $$1, $$2}' \
		| sed -e 's/\[34m##/[36m/'

##
##      Utils
##───────────────────

init: hooks ## Initialize your local copy of the repo
	git config --local blame.ignoreRevsFile .git-blame-ignore-revs

install: ## Install minimal dependencies with uv
	uv venv
	uv pip install -e .

install-dev: ## Install all (+dev) dependencies with uv
	uv venv
	uv pip install -e ".[dev]"

local-install: ## Install package (editable) with dev PyPI dependencies
	uv venv
	uv pip install -e ".[dev]"

hooks: ## Install hooks locally
	cp -f .gitlab/hooks/* .git/hooks/
	chmod +x .git/hooks/*

artifact: clean-dist ## Build package
	uv pip install build
	uv run python -m build

publish: artifact ## Pulish package to Google Artifact Registry
	#flit publish --repository rf-pypi --pypirc .pypirc --no-use-vcs
	twine upload \
		--repository rf-pypi --config-file .pypirc \
		-u ${NEXUS_PYPY_DEPLOY_USER} \
		-p ${NEXUS_PYPY_DEPLOY_PASSWORD} \
		dist/*

##
##    Maintain/QA
##───────────────────

check: check-format typecheck lint check-docs ## Run all checks

check-format: ## Check if code is compliant with formatter
	uv run ruff format --check

format: ## Perform codebase formatting
	uv run ruff format

fix: ## Fix QA mistakes
	uv run ruff check --fix .

fix-unsafe: ## Fix QA mistakes
	uv run ruff check --fix --unsafe-fixes .

ci: check-format lint typecheck ## Perform CI tasks
	$(MAKE) -s test

lint: ## Assess code quality
	uv run ruff check

typecheck: ## Typecheck codebase
	uv run mypy .

test: ## Run test cases
	uv pip install -e .
	uv run pytest $(RUN_ARGS)

##
##      Cleanup
##───────────────────

clean: clean-dist clean-pyc clean-mypy ## Perform all clean recipes

clean-pyc: ## Remove python bytecode cache
	find . -type f -name '*.py[co]' -delete ;\
	find . -type d -name '__pycache__' -delete ;\
	find . -type d -name '.pytest_cache' -exec rm -rf {} +

clean-dist: ## Remove distribution folder
	rm -rf dist

clean-mypy: ## Remove mypy cache
	rm -rf .mypy_cache

##
##   Documentation
##───────────────────

docs: ## Generate API documentation
	uv pip install -e .
	uv pip install lazydocs pydocstyle
	uv run lazydocs \
		--output-path="./docs/api-docs" \
		--overview-file="README.md" \
		--src-base-url="https://github.com/velvet-compute/velvet-lib/blob/main/" \
		\
		APOLLO_LIBRARY

docs-clean: ## Clean generated documentation
	rm -rf docs/api-docs/*

check-docs: ## Check if documentation is valid
	uv pip install -e .
	uv pip install pydocstyle
	uv run pydocstyle APOLLO_LIBRARY
