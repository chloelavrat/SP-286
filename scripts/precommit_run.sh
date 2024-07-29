#!/bin/bash

# Define color codes
SUCCESS_COLOR='\033[0;32m'
RESET_COLOR='\033[0m'  # No Color

# Function to activate the Python virtual environment
activate_env() {
    echo -e "${SUCCESS_COLOR}Activating virtual environment...${RESET_COLOR}"
    source .venv/bin/activate > /dev/null
}

# Function to execute pre-commit hooks on all files
run_precommit_hooks() {
    pre-commit run --all-files
}

# Main script execution
activate_env
run_precommit_hooks
