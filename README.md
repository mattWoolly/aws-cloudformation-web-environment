# aws-cloudformation-web-environment
## CloudFormation Template
### Provisions:
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
 
