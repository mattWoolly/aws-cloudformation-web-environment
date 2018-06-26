#!/usr/bin/env python

import boto3
import yaml

client = boto3.client('cloudformation')

stacks = client.describe_stacks()
cf_template = 'cloudformation_01.yml'
template_url = 'https://s3.amazonaws.com/mattwoolly-cf-templates/cloudformation_01.yml'
stack_name = 'web02'

stream = file(cf_template, 'r')
yaml.load(stream)

validate = client.validate_template(
    TemplateURL=template_url
)
print validate
new_stack = client.create_stack(
    StackName = 'web-stack-from-boto3-01',
    TemplateURL = template_url
)
new_stack


