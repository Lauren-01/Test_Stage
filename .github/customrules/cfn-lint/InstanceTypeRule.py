"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch


class InstanceTypeRule(CloudFormationLintRule):
    id = 'W9998' # New Rule ID
    shortdesc = 'Check if the instance type is T2.Micro' # A short description about the rule
    description = 'This custom rule will check if the EC2 Instance had T2.Micro as instance type.' # (Longer) description about the rule
    #source_url = '' # A url to the source of the rule, e.g. documentation, AWS Blog posts etc
    #tags = [] # A set of tags (strings) for searching

    def match(self, cfn):
        """Basic Rule Matching"""

        matches = []
        ec2_instance = cfn.get_resources(['AWS::EC2::Instance'])

        # Your Rule code goes here
        for logical_id, resource in ec2_instance.items():
            properties = resource.get('Properties', {})
            instance_type = properties.get('InstanceType', '')
            
            if instance_type.lower() != 't2.micro':
                message = 'EC2 Instance {} should have T2.Micro as the instance type'.format(logical_id)
                matches.append(RuleMatch(['Resources', logical_id, 'Properties', 'InstanceType'], message))

        return matches
