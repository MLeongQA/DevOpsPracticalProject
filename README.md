# DevOpsPracticalProject

## Contents

- [Introduction](#Introduction)
  - [Objective](#Objective)
  - [My Proposition](#My-Proposition)
- [Architecture](#Architecture)
  - [Risk Assessment](#Risk)
  - [Project Tracking](#Project)
  - [Analysis of Testing](#Analysis)
- [Infrastructure](#Infrastructure)
  - [CICD Pipeline](#CICD-Pipeline)
  - [ER Diagram](#ER-Diagram)
  - [Interaction Diagram](#Interaction)
  - [Services Diagram](#Services)
- [Development](#Development)
  - [Unit Testing](#Unit)
  - [Front-end Development](#Front-end-Development)
- [Evaluation](#Evaluation)
  - [Points of Improvement](#Points-of-Improvement)
  - [Authors](#Authors)
  - [Acknowledgements](#Acknowledgements)

## Introduction

### Objective

The objective of this project is as follows:
>You are required to create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.

To go into further detail, the 4 services should be comprised of:
- A core front-end service that will communicate with the other three services, and input some data into a database.
- Two back end services that will generate a random object.
- One back end service that will generate a object based on the randomly generated object from the other two back end services.

In addition, the project is expected to utilise the following technologies:
- Kanban Board: Asana or an equivalent Kanban Board
- Version Control: Git
- CI Server: Jenkins
- Configuration Management: Ansible
- Cloud server: GCP virtual machines
- Containerisation: Docker
- Orchestration Tool: Docker Swarm
- Reverse Proxy: NGINX

### My Proposition

My proposal for this project is to create a password generating website.

- Service 1 : The front end of the application, that will list the history of passwords generated, alongside some additional data such as password strength.
- Service 2 : Will generate a random set of string.
- Service 3 : Will generate a random two digit integer.
- Service 4 : Will produce a password score based on the random generation from service 2 and service 3.

## Architecture

### Risk Assessment

A screenshot of my risk assessment can be found below.

![Risk Assessment](https://i.imgur.com/Kn5YllJ.png)

**Update**: The risk assessment has been updated with potential risks of broken versions being pushed onto github, causing the website not function if built. In response to this, the pipeline was implemented to not process if the build if the unit tests fail.

The full risk Assessment can be found [here](https://docs.google.com/spreadsheets/d/18LOucbo6bNB233hZN950s-zoDuAG8sb8tvt1NYHw6a0/edit?usp=sharing).

### Project Tracking

### Analysis of Testing

## Infrastructure

### CICD Pipeline

### ER Diagram

![ER Diagram](https://i.imgur.com/6LSYy0d.png)

![ER Diagram2](https://i.imgur.com/Ap8J8lV.png)

### Interaction Diagram

## Development

### Unit Testing

### Front-end Development

## Evaluation

### Points of Improvement

### Authors

### Acknowledgements
