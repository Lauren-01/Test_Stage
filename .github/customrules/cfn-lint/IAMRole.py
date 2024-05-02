"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch


class IAMRoleRule(CloudFormationLintRule):
    id = 'W1234' # New Rule ID
    shortdesc = 'Check if IAM Role is not referenced in the template' # A short description about the rule
    description = 'This custom rule will check if an iAM Role is defined but not referenced in the template' # (Longer) description about the rule

    def match(self, cfn):
        matches = []

        IAM_role = cfn.get_resources(['AWS::IAM::Role'])

        all_roles = cfn.get_resource_properties(['Ref'])

        for ID, IAM_role in IAM_role.items():
            if ID not in all_roles:
                message = 'IAM Role "{}" is defined but not referenced'.format(ID)
                matches.append(RuleMatch(['Resources', ID], message))
        
        return matches