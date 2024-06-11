"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch


class NameRule(CloudFormationLintRule):
    id = 'W9999' # New Rule ID
    shortdesc = 'Check if names of resources contain Cloudar' # A short description about the rule
    description = 'This custom rule will check if resources have Cloudar in their name.' # (Longer) description about the rule
    #source_url = '' # A url to the source of the rule, e.g. documentation, AWS Blog posts etc
    #tags = [] # A set of tags (strings) for searching

    def match(self, cfn):
        """Basic Rule Matching"""

        matches = []

        # Your Rule code goes here
        for resource_name, resource_values in cfn.get_resources().items():
            resource_type = resource_values.get('Type')

            if resource_type == 'AWS::EC2::Instance':
                instance_tags = resource_values['Properties'].get('Tags', [])
                instance_name = next((tag['Value'] for tag in instance_tags if tag.get('Key') == 'Name'), '')
                if 'cloudar-' not in instance_name:
                    matches.append(RuleMatch(['Resources', resource_name], 'This EC2 resource name does not contain cloudar-'))
    
            if resource_type == 'AWS::S3::Bucket' and 'cloudar-' not in resource_values['Properties']['BucketName']:
                matches.append(RuleMatch(['Resources', resource_name], 'This bucket name does not contain cloudar-'))
            
            if resource_type == 'AWS::EC2::VPC':
                vpc_tags = resource_values['Properties'].get('Tags', [])
                vpc_name = next((tag['Value'] for tag in vpc_tags if tag.get('Key') == 'Name'), '')
                if 'cloudar-' not in vpc_name:
                    matches.append(RuleMatch(['Resources', resource_name], 'This VPC name does not contain cloudar-'))


        return matches


# AWS::EC2::Instance Tags[?Key=='Name'] REGEX_MATCH "^cloudar-,+" WARNING "Name must contain Cloudar"
