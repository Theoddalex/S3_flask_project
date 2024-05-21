# Flask and AWS Project

This project is a Flask web application that connects to a PostgreSQL database and integrates with AWS S3 for storing images or videos. The application allows users to enter their name and email, which are then stored in the database. Upon successful submission, the user is greeted with a message and an image/video fetched from an AWS S3 bucket.

## Features

- User registration with name and email.
- User data stored in PostgreSQL database.
- Integration with AWS S3 to display images or videos.
- Dockerized setup for easy deployment.

## Prerequisites

- Python 3.9
- Docker and Docker Compose
- AWS account with access to S3
- AWS CLI
- boto3

## Setup

### Clone the Repository

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

## Create a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

## Install Dependencies (Optional for Local Development)
```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a .env file in the root directory and add the following environment variables:
```bash

POSTGRES_DB=mydatabase
POSTGRES_USER=yourusername
POSTGRES_PASSWORD=yourpassword
FLASK_APP=app.py
SQLALCHEMY_DATABASE_URI=postgresql://yourusername:yourpassword@db/mydatabase
BUCKET_NAME='yourbucketname'
IMAGE_NAME='yourimagename'
```

## AWS S3 Setup

Ensure you have an AWS S3 bucket set up and accessible.

# Local setup 

Add your AWS credentials to the ~/.aws/credentials file:


```bash

[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```
# EC2 setup
Since the bucket is private we'll have to give the EC2 a permission to access the S3 bucket.

## Step 1: Create an IAM Role

### Open the IAM Console:


Go to the IAM Console at https://console.aws.amazon.com/iam/.

### Create a New Role:
Click on Roles in the left-hand menu. 

Click on the Create role button.

### Select Trusted Entity:

Choose AWS service.

Under Use case, select EC2.

Click Next: Permissions.

### Attach Policies:

Search for and select the AmazonS3FullAccess policy. This policy provides full access to S3.

Click Next: Tags.

Note: If you want to give more granular permissions, you can create a custom policy.

### Name and Create the Role:

Provide a name for your role (e.g., EC2S3AccessRole).

Click Create role.

## Step 2: Attach the IAM Role to Your EC2 Instance

### Open the EC2 Console:

Go to the EC2 Console at https://console.aws.amazon.com/ec2/.

### Select Your Instance:

Find and select the EC2 instance you want to grant access to.

### Attach the IAM Role:

Click on the Actions button.

Select Security > Modify IAM Role.

In the IAM Role dropdown, select the role you created (e.g., EC2S3AccessRole).

Click Update IAM role.

### Verify the IAM Role:

SSH into your EC2 instance.

Ensure the AWS CLI is installed.

Verify access with aws sts get-caller-identity.

Access the S3 bucket with aws s3 ls s3://your-bucket-name.

By following these steps, your EC2 instance will have the necessary permissions to access your S3 bucket.



# Running the Application

## Using Docker

Build the Docker images:

```bash
docker-compose build
```
Start the containers:
```bash

docker-compose up
```
The application will be available at http://localhost:5001.


## Running the Application Locally

1.Initialize and upgrade the database(Optional for local development):

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

2.Run the application:

```bash
flask run
```
The application will be available at http://localhost:5001.


## Usage

1.Navigate to the application URL.

2.Enter your name and email in the registration form.

3.Submit the form to see a greeting message and an image/video from the S3 bucket.



