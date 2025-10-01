# Automated CI/CD Pipeline for a Flask App on AWS EC2



This project demonstrates a complete, automated CI/CD pipeline that tests, containerizes, and deploys a Python Flask application to an AWS EC2 instance using GitHub Actions.

## Overview
This pipeline automates the entire software delivery lifecycle. On every `git push` to the `main` branch, the following automated workflow is triggered:
1.  **CI Stage:** The code is checked out and tested using `pytest` to ensure quality.
2.  **Build Stage:** A Docker image is built from the `Dockerfile` and pushed to Docker Hub.
3.  **CD Stage:** The pipeline securely connects to a target EC2 instance via SSH, pulls the new Docker image, and restarts the container to deploy the update.


## Tech Stack
- **CI/CD:** GitHub Actions
- **Containerization:** Docker & Docker Hub
- **Application:** Python, Flask
- **Testing:** Pytest
- **Cloud Provider:** AWS (EC2)

