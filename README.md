# Technical challenge / Consorcio

This project include serverless developments based on:
- Python 3.8
- NodeJS v10.16
- NPM 6.14
- AWS CLI 1.16
- PIP 20.1
- Serverless Framework 1.71

Packages listed in [/src/requirements.txt](src/requirements.txt) file

## Tools Instalation 

This documentation assume that the following components are already installed on your system:
- Python 3.8
- NodeJS v10.16
- NPM 6.14
- AWS CLI 1.16
- PIP 20.1

Install Serverless Framework binary globally
```
npm install serverless -g
```

Install NodeJS dependencies
```
npm install
```

Install boto3
```
pip install boto3
```

## Deployment

First, configure your IAM credentials using the following commands
```
aws configure
```

(For this technical challenge purpose, the AWS CLI IAM user has Administrator role.)

Finally, deploy the project to Amazon Web Service using Serverless Framwwork
```
sls deploy
```