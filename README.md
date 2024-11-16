# Simple Attendance Form

## Description

This is a simple attendance tracking system built using Docker Compose, Docker, Nginx, Sentry, PostgreSQL, Flask, and an HTML Form. The project also includes a CI/CD pipeline setup to streamline the build, test, and deployment process.


## Topology
<img src="img/Topology.svg"> 

Features:

- **Frontend**: HTML form to submit attendance details.
- **Backend**: Flask application to handle form submissions and store data.
- **Database**: PostgreSQL to manage attendance records.
- **Error Monitoring**: Sentry integration for tracking and managing application errors.
- **Reverse Proxy**: Nginx to serve the Flask app.
- **CI/CD**: Build pipeline to automate testing and deployment.
- **Containerized**: Fully containerized using Docker and orchestrated with Docker Compose.

## CI/CD Workflows
Continuous Integration

<img src="img/CI.png"> 

Continuous Delivery and Continuous Deployment

<img src="img/CD.png"> 
<img src="img/CD1.png"> 
<img src="img/CD2.png"> 

## Sentry Monitoring
<img src="img/Sentry.png"> 

## Requirements
- `Docker`
- `Python 3.8`
- `Sentry`
- `Nginx`
- `Virtualenv`
