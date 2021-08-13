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

Trello was decided as my project tracking app. The diagram can be found [here](https://trello.com/b/J1EhFbkm/password-project-board)

![Trello Board](https://i.imgur.com/eCt4mzA.png)

I have divided my trello board into multiple lists to categorise each task and be able to see the task progress.

- Project Resources: A list of handy resources for my project that can be quickly accessed.
- User Stories: A collection of stories to document the requirements of my project
- To Do: A list of tasks that are required to be initalised.
- In Progress: A list of tasks that have been started and requires completion
- Completed: A list of tasks that have been completed.

**Update**: The board was changed to implement the CRUD functionality + Form functionality.

### Analysis of Testing

Testing was a essential part of this project, as a failed product could not be allowed to be built on my Jenkins. Therefore each functionality of each services had to be tested properly.

![Analysis of Testing](https://i.imgur.com/poWIxoi.png)

This testing document was used to keep track of what tests were required to be implemented, as well as listing details on how they were to be tested.

## Infrastructure

### CICD Pipeline

![CICD Diagram](https://i.imgur.com/WZk6oex.png)

### ER Diagram

![ER Diagram](https://i.imgur.com/6LSYy0d.png)

![ER Diagram2](https://i.imgur.com/Ap8J8lV.png)

### Interaction Diagram

### Services Diagram

![Services Diagram](https://i.imgur.com/KVOmvDc.png)
![Services Diagram2](https://i.imgur.com/0I9H5T2.png)

## Development

### Unit Testing

### Front-end Development

## Evaluation

### Points of Improvement

### Authors

### Acknowledgements
