# Flask-taskmanagement-app

Flask Task Management is a web application built using the Flask framework that allows users to manage and track their tasks. Users can create, update, and delete tasks while keeping track of their progress and status.

## Features

- User-friendly interface for task management
- Create, update, and delete tasks

## Deployment

The application is packaged as a Docker image and can be deployed on any platform supporting containerized applications. In this example, we are using the Nappitive Playground to deploy the application.

To deploy the Flask Task Management application, you can use the provided `flask-taskmanagement.app.yaml` file. This file contains the necessary configuration for deploying the application with a public endpoint using the Nappitive Playground.

Once the application is deployed, you can access it using the public endpoint provided by the Nappitive Playground. The application will be available on port 5000 at the root path.

## Usage

1. Access the Flask Task Management application using the public endpoint provided by the Nappitive Playground.
2. Create a new task by clicking the "Add Task" button and filling out the required information.
3. Update or delete existing tasks by clicking the appropriate buttons in the task list.

## Accessing the Web Application

Once the Flask Task Management application is deployed on the Nappitive Playground, you can access it via a public endpoint created using the `napptive-ingress` trait. The application will be available on port 5000 at the root path.

To find the public endpoint, you can check the Nappitive Playground user interface or use the Nappitive CLI to get the public URL. Once you have the URL, you can access the Flask Task Management application using a web browser or any other HTTP client.


## Contributing

To contribute to the Flask Task Management application, please fork the repository and submit a pull request with your proposed changes. Ensure that your changes are well-documented and tested.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
