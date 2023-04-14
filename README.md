# Task Manager

Task Manager is a simple web application built with Flask that allows users to manage their tasks. Users can add new tasks, list all existing tasks, and remove a task. This application is a great starting point for beginners who want to learn Flask or hackathon colleagues who want to quickly build a simple application.

## Installation

To use this application, first clone the repository to your local machine:

`git clone https://github.com/MuhammadNoorani/flask-taskmanagement-app.git`

Then, navigate to the project directory and install the required dependencies:

`cd <repository-name>`
`pip install -r requirements.txt`


## Usage

To run the application, execute the following command from the project directory:

`python app.py`


The application will start running at `http://localhost:5000`. Navigate to this URL in your web browser to use the application.

## How to use the application

The home page of the application (`http://localhost:5000/`) displays a form to add new tasks. You can enter a task and click on "Add another task" to add more tasks. Once you have entered all the tasks you want to add, click on "Submit tasks" to add them to the task list.

The home page also displays a list of all the tasks that have been added so far. Each task in the list is numbered, and you can use the task number to remove a task. To remove a task, enter the task number in the "Enter task number" input field and click on "Remove task".

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. Be sure to document your changes and add appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Docker

This project can be deployed as a Docker container. A Dockerfile is included in the project. To build the Docker image, navigate to the project directory and run the following command:

`docker build -t <image-name>`


To run the Docker container, execute the following command:

`docker run -p 5000:5000 <image-name>


Replace `<image-name>` with the name you want to give to the Docker image. Once the container is running, you can access the application at `http://localhost:5000`.

Note: Make sure you have Docker installed on your machine before building and running the Docker container.
`
