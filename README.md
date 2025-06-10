# Web Scraping with Docker & Selenium

---

## Overview

This project demonstrates how to run a **Selenium-based web scraper** inside Docker containers. We leverage a combination of the following technologies for an efficient and isolated solution:

* **Docker Compose** for container orchestration, allowing you to manage multiple containers together with ease.
* **Selenium Standalone Firefox** as the browser that will be used for the scraping process. This ensures a consistent browser environment.
* **Python** for the core scraping logic, which will interact with the browser and process the data.
* **Volume mounting** to save the scraping results locally on your machine, so the data persists even if the containers are stopped.

---

## Prerequisites

Before getting started, please ensure you have the following software installed on your system:

* **Docker**: If you don't have it yet, you can download and install it from [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).
* **Docker Compose**: Follow the installation instructions at [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/) to ensure Docker Compose is properly set up.
* **Python** (Optional): While not strictly required to run this project within Docker, Python can be useful if you wish to perform local testing or development of the script before integrating it into the container.

---

## Project Structure

Here's an overview of the project's directory structure:
```
our_project/
├── docker-compose.yml          # Main Docker Compose configuration
├── selenium-script/
│   ├── Dockerfile              # Docker image definition for the Python scraper container
│   ├── scraper.py              # The main Python script containing the scraping logic
│   └── requirements.txt        # List of Python dependencies required by scraper.py
└── data/                       # Output directory where scraping results will be saved (automatically created on run)
```

## Quick Start Guide

Follow these simple steps to build and run your web scraper:

### 1. Clone the Repository

First, clone this repository to your local machine using Git:
```bash
git clone [your-repo-url]
cd your_project
```

### 2. Build and Run the Containers
```bash 
docker-compose up --build
```
This command will do several things:

- Pull the selenium/standalone-firefox image if it's not already on your system.
- Build the Python scraper container based on the Dockerfile in selenium-script/.
- Run the scraper and automatically save its results in the ./data/ directory at your project root.

### 3. Monitor the Scraping Process

Access the Selenium web browser to see the process at:
[http://localhost:4444](http://localhost:4444)
