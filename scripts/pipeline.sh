#!/bin/bash

set -e

# Install depenencies
bash scripts/setup.sh

# Run unit and integration tests
bash scripts/test.sh

# Build and push Docker images
bash scripts/build.sh

# Configure hosts for deployment
bash scripts/config.sh

# Deploy stack to manger
bash scripts/deploy.sh

