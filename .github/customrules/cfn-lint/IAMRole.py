"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch
from cfnlint.template import Template


class IAMRoleRule(CloudFormationLintRule):
    id = 'W1234'  # New Rule ID
    shortdesc = 'Check if IAM Role is not referenced in the template'  # A short description about the rule
    description = 'This custom rule will check if an iAM Role is defined but not referenced in the template'  # (Longer) description about the rule

    def match(self, cfn):
        assert isinstance(cfn, Template), "The object cfn should be a template"

        matches = []

        IAM_roles = cfn.get_resources(['AWS::IAM::Role'])

        for role in IAM_roles:
            if cfn.graph.graph.in_degree(role) == 0:
                message = 'IAM Role "{}" is defined but not referenced'.format(role)
                matches.append(RuleMatch(['Resources', role], message))

        return matches

