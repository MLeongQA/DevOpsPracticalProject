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

As I would not be able to interact with other services during the unit testing, I implemented requests.mock() onto the unit tests, which would allow me to simulate how the services may interact with each other. Service 1 will also have interaction with the database, making it crucial that the tests function correctly.

## Infrastructure

### CICD Pipeline

Continuous Deployment was a neccessity for the project, to allow a smooth and rapid development to build process. The CICD diagram is shown below.

![CICD Diagram](https://i.imgur.com/WZk6oex.png)

The steps were as follows:

1. Tasks that were set up on the trello board were coded, and uploaded to github.
2. The Jenkins webhook that is set up, will detect any pushes onto the dev branch, and proceeded to line the pipeline found in the Jenkins file.
3. The unit tests were ran first, to ensure that the new code does not break the application.
4. The docker images were built and pushed onto dockerhub. Jenkins credentials was used to handle the dockerhub login information.
5. Ansible was used to configure the load balancer, swarm manager and it's workers to be ready for the application deployment.
6. The Jenkins VM deployed the stacks onto each VM.

![Pipeline](https://i.imgur.com/0C5O9Au.png)

### ER Diagram

![ER Diagram](https://i.imgur.com/6LSYy0d.png)

The initial ER Diagram is as shown as above. The password ID is used to uniquely identify each password, the password field contained the actual password as the string, and the password rating was stored as a integer.

**Update**: The ER diagram was updated to feature the "In Use" column which will identify whether a password is already being utilised or not. 

![ER Diagram2](https://i.imgur.com/Ap8J8lV.png)

### Interaction Diagram

![Interaction Diagram](https://i.imgur.com/vBvTFc9.png)

The interaction diagram, as shown above, shows my swarm network, where a load-balancer will direct the user to the VM with the least load. The user is also unable to access each of the VMs outside of the load balancer directly, increasing the security of my network.

### Services Diagram

![Services Diagram](https://i.imgur.com/KVOmvDc.png)

The above services diagram shows the front-end (service-1) sending a GET request to both services-2, and services-3 where the responses would be sent to services-4 to recieve a password rating. Finally all the data would be uploaded onto the mysql database, and service-1 is able to SELECT old entries from the MySQL Database to display all the passwords generated.

**Update**: The services diagram was updated to change the GET request to service-2 into a POST request, to implement the form and CRUD functionality.

![Services Diagram2](https://i.imgur.com/0I9H5T2.png)

## Development

### Unit Testing

Unit testing is used to ensure the back-end of my application was functional and data manipulation in the database was done correctly. Assertions were used to ensure that the correct output was being produced, and requests_mock was used to simulate the interaction of the services. These tests are run automatically after every Git push
onto the dev branch, using Jenkins. Jenkins will then prints out whether the test succeeded and gave a coverage report noting the percentage of the application that was tested.

![Unit Tests](https://i.imgur.com/exwNqEa.png)

The code used in the Jenkinsfile for testing are:

>python3 -m venv venv
>
>source venv/bin/activate
>
>pip3 install -r requirements.txt
>
>python3 -m pytest --cov --cov-report=term-missing --cov-report xml --junitxml junit.xml

This installs all the packages required to run the unit tests, and then runs the test in each service. 

A .coveragerc was used so that only the relevant files were tested and excluded lines that were not required to be tested. This also saved having to change directories to each unit test and run them seperately. The JUnit plugin was used in Jenkins to utilise the junit.xml and create advanced testing reports in case of a testing failure.

![Testreport](https://i.imgur.com/ufbzlTs.png)

### Front-end Development

Navigating to port 80 of the load-balancer will bring users to the index page as shown below. The pages are generated using HTML and flask.

![Index](https://i.imgur.com/PS3tla1.png)

From this page, users are able to enter the create page, by clicking on the "Generate Password" button.

![Create](https://i.imgur.com/QOfc76D.png)

Here, the user is prompted on the length of the password length, which is entered in the form.

![Read](https://i.imgur.com/85ep02A.png)

Once the password has been created, it can be seen from the index page. The password can be "updated" to display whether if it's in use or not, and also deleted using "delete"

## Evaluation

### Points of Improvement

- Improving the aesthetics of the website. Better layouts.
- In use passwords potentially being censored for security.
- Explanation of the password score on the site.

### Authors

Mikito Leong

### Acknowledgements

- Oliver Nichols
- Ryan Wright
- 21JunDevOps2 Course Mates
