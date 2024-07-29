#!/bin/bash

# Define color codes for output
GREEN='\033[0;32m'
RESET='\033[0m' # Reset to default color

# Function to activate the Python virtual environment
activate_env() {
    echo -e "${GREEN}Activating the virtual environment...${RESET}"
    source .venv/bin/activate > /dev/null
}

# Function to install pre-commit and set it up
install_precommit() {
    echo -e "${GREEN}Installing pre-commit...${RESET}"
    pip install pre-commit > /dev/null
    pre-commit install > /dev/null
}

# Main script execution
activate_env
install_precommit
