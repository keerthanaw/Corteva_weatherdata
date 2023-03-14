# Deploy App on AWS 
To deploy the API, database, and scheduled data ingestion code, I would use the following AWS services:

```
1.	Amazon EC2 (Elastic Compute Cloud): To launch a virtual machine instance and install the necessary software for our API and database. EC2 provides flexibility and scalability to handle a large number of requests and to accommodate changes in traffic patterns.

2.	Amazon RDS (Relational Database Service): To create and manage a relational database. RDS provides several options for database engines such as MySQL, PostgreSQL, Oracle, and Microsoft SQL Server. We can choose the database engine that is best suited for our application.

3.	AWS Lambda: To run our data ingestion code on a scheduled basis. Lambda allows us to execute code without the need to provision or manage servers. Additionally, we can use the AWS CloudWatch to schedule our Lambda function.

4.	Amazon API Gateway: To create, manage, and secure APIs. API Gateway can handle requests from clients, route them to the appropriate backend service, and return the response to the client.

5.	AWS CloudFormation: To automate the deployment and management of our infrastructure as code. Itallows us to create and provision AWS resources in a repeatable and predictable manner.

6.	Amazon S3 (Simple Storage Service): To store our data files. S3 provides durability, scalability, and security for our data. We can also use S3 to host our static website content.

7.	AWS IAM (Identity and Access Management): To manage access to AWS resources. IAM allows us to create and manage users, groups, and roles, and to assign permissions to them.
```

#Here is an overview of my approach

##For infrastructure set up

```
1.	Use AWS CloudFormation to create and provision the necessary resources for our application. 
2.	Create an EC2 instance and install the necessary software for our API and database. 
3.	Create an RDS instance and choose the appropriate database engine.
4.	Use Lambda to run our data ingestion code on a scheduled basis and API Gateway to create and manage our API. 
5.	Store data files in S3 and utilize IAM to manage access to resources.
```

##Once infrastructure is set up

```
1.	Deploy API code and database schema to the EC2 instance. 
2.	Configure the API Gateway to route requests to the appropriate backend service. 
3.	Schedule our Lambda function to run at the desired intervals to ingest the data files into the database. 
4.	Additionally, monitor the application using AWS CloudWatch to ensure it is running smoothly and to troubleshoot any issues that arise.
```

Overall, this approach provides a scalable and cost-effective solution for deploying an API, database, and scheduled data ingestion code in the cloud using AWS.

