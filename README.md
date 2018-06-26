# aws-cloudformation-web-environment
## Description
Python script to run CloudFormation actions. CloudFormation template can be manually used within AWS console, or used with the included Python utility. The Python utility references the same CloudFormation template, pulled from S3.
## REQUIREMENTS
* Python 2.7
* BOTO3
* AWS Credentials set up within your local environment
## Usage & Examples
```
./cf-control.py --help`
```
```
./cf-control.py --describe --name web-stack-01
```
```
./cf-control.py --create --name web-stack-01
```
```
./cf-control.py --delete --name web-stack-01
```
## CloudFormation Template Features
1. VPC
2. Subnet
3. Internet Gateway
4. Route Table
5. Route to Internet Gateway
6. Security Group with SSH and HTTP open to the world
7. EC2 Instance based on Amazon Linux 2 (t2.micro)
9. Creates Elastic IP & assigns to EC2 instance
10. Installs Apache web server & installs an index.html page
11. CloudFormation outputs the public IP where the idnex.html page can be viewed.
 
