#!/usr/bin/env python

import boto3
import yaml
import argparse

client = boto3.client('cloudformation')

cf_template = 'cloudformation_01.yml'
template_url = 'https://s3.amazonaws.com/mattwoolly-cf-templates/cloudformation_01.yml'
stack_name = 'web01'

def describe_stack(name):
    stacks = client.describe_stacks(
        StackName = name
    )
    print stacks

def validate_template(template_local):
    try:
        response = client.validate_template(
                TemplateBody = 'file://' + template_local
        )
        print response
    except Exception as error:
        print error

def create_stack(name, templateurl):
    try:
        response = client.create_stack(
            StackName = name,
            TemplateURL = templateurl
        )
        print response
    except Exception as error:
        print error

def delete_stack(name):
    try:
        response = client.delete_stack(
            StackName = name
        )
        print response
    except Exception as error:
        print error

# Manual overrides
#validate_template(cf_template)
#create_stack(stack_name, template_url)
#describe_stack(stack_name)
#delete_stack(stack_name)

# Set up argparse for command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--describe', default=False, action='store_true',  help='Describes CloudFormation Stack')
parser.add_argument('--create', default=False, action='store_true', help='Creates CloudFormation Stack')
parser.add_argument('--delete', default=False, action='store_true', help='Deletes CloudFormation stack')
parser.add_argument('--name', required=True, help='Provide name for CloudFormation stack')
args = parser.parse_args()

# Get stack name from argument
if args.name:
    name = args.name
else:
    name = stack_name

# Run functions based on argument
if args.create:
    create_stack(name, template_url)
elif args.describe:
    describe_stack(name)
elif args.delete:
    delete_stack(name)

