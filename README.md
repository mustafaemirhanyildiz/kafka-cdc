# Kafka CDC  


# Introduction
This project focuses on building a simple Change Data Capture (CDC) application using Apache Kafka. CDC is a technique used to capture and propagate data changes in a database in real-time.
Apache Kafka ile Basit CDC Uygulaması Geliştirme Projesi

# Project Description
The project consists of the following components:

1-Apache Kafka: A distributed streaming platform that allows the publishing and subscribing of streams of records.

2-MongoDB: A NoSQL document database used as the data source for this CDC application.

3-Producer: A component that captures the changes made to the MongoDB database and sends them to the Kafka server.

4-Consumers: Components that consume the data from the Kafka server and print it to the console.

# Getting Started
To set up the project, follow the steps mentioned below:

-Clone the project repository to your local machine.

-Navigate to the project directory using the command line or terminal.

-Run the command docker compose up to start the required services (Kafka and MongoDB).

-Wait for 15-20 seconds to allow the services to start successfully.

-Open MongoDB Compass or any other MongoDB client.

-Connect to the MongoDB instance using the connection string mongodb://localhost:27020.

-Create a new database named "meydb".

-Within the "meydb" database, create a collection named "kafka".

-Now, whenever you add data to the "kafka" collection in the "meydb" database, the producer component will capture the changes and send them to the Kafka server.

-The consumer components will consume these data changes and print them to the console.

-Please note that the project assumes you have Docker installed on your machine. If not, make sure to install Docker before proceeding with the above steps.

Feel free to modify and enhance the project according to your requirements. Happy coding!
# Project Diagram
![image](https://github.com/mustafaemirhanyildiz/kafka-cdc/assets/92929045/a8414501-93f1-458d-ab1f-c821b831f7ba)

