# aws-cloudformation-boto3-web-environment
## Description
Python script to run CloudFormation actions. CloudFormation template can be manually used within AWS console, or used with the included Python utility. The Python utility references the same CloudFormation template, pulled from S3.
## REQUIREMENTS
* Python 2.7
* BOTO3
* argparse
* pycurl
* StringIO
* AWS Credentials set up within your local environment
## Usage & Examples
**./cf-control.py --help**
```
usage: cf-control.py [-h] [--describe] [--create] [--delete] [--test] --name
                     NAME

optional arguments:
  -h, --help   show this help message and exit
  --describe   Describes CloudFormation Stack
  --create     Creates CloudFormation Stack
  --delete     Deletes CloudFormation stack
  --test       Tests CloudFormation stack
  --name NAME  Provide name for CloudFormation stack
```
**./cf-control.py --describe --name web-stack-01**
```
AWS::EC2::SubnetRouteTableAssociation >>  CREATE_COMPLETE
AWS::EC2::VPCGatewayAttachment >>  CREATE_COMPLETE
AWS::EC2::Instance >>  CREATE_COMPLETE
AWS::EC2::EIP >>  CREATE_COMPLETE
AWS::EC2::SecurityGroup >>  CREATE_COMPLETE
AWS::EC2::InternetGateway >>  CREATE_COMPLETE
AWS::EC2::Subnet >>  CREATE_COMPLETE
AWS::EC2::Route >>  CREATE_COMPLETE
AWS::EC2::RouteTable >>  CREATE_COMPLETE
AWS::EC2::VPC >>  CREATE_COMPLETE
```
**./cf-control.py --create --name web-stack-01**
```
{u'StackId': 'arn:aws:cloudformation:us-east-1:889054573129:stack/web-stack-02/b9397020-79b9-11e8-8b41-500c28604c82', 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': 'b92fac41-79b9-11e8-928a-d98bdbd0c5c1', 'HTTPHeaders': {'x-amzn-requestid': 'b92fac41-79b9-11e8-928a-d98bdbd0c5c1', 'date': 'Wed, 27 Jun 2018 03:25:22 GMT', 'content-length': '382', 'content-type': 'text/xml'}}}
```
**./cf-control.py --delete --name web-stack-01**
```
{'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': '86732800-79b7-11e8-93a5-272fe73e0132', 'HTTPHeaders': {'x-amzn-requestid': '86732800-79b7-11e8-93a5-272fe73e0132', 'date': 'Wed, 27 Jun 2018 03:09:36 GMT', 'content-length': '212', 'content-type': 'text/xml'}}}
```
**cf-control.py --test --name web-stack-01**
```
AWS::EC2::SubnetRouteTableAssociation >>  CREATE_COMPLETE
AWS::EC2::VPCGatewayAttachment >>  CREATE_COMPLETE
AWS::EC2::Instance >>  CREATE_COMPLETE
AWS::EC2::EIP >>  CREATE_COMPLETE
AWS::EC2::SecurityGroup >>  CREATE_COMPLETE
AWS::EC2::InternetGateway >>  CREATE_COMPLETE
AWS::EC2::Subnet >>  CREATE_COMPLETE
AWS::EC2::Route >>  CREATE_COMPLETE
AWS::EC2::RouteTable >>  CREATE_COMPLETE
AWS::EC2::VPC >>  CREATE_COMPLETE

All resources created successfully

Web Server Displays: <h1>Automation for the People</h1>

Stack Validated
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
11. CloudFormation outputs the public IP where the index.html page can be viewed.

## To-Do
* Python utility pulls CloudFormation template from S3. This should sync from the local copy. I didn't add it to this project since the user won't have write permissions to the S3 bucket used.
* Clean --create and --delete output
* Testing is very basic but shows if the stack creation and web server function. Moto integration would be nice.

## Authors
Matt Woolly

