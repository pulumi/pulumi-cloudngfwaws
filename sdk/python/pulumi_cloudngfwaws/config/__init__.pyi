# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

accessKey: Optional[str]
"""
(Used for the initial `sts assume role`) AWS access key. Environment variable: `CLOUDNGFWAWS_ACCESS_KEY`. JSON conf file
variable: `access-key`.
"""

accountAdminArn: Optional[str]
"""
The ARN allowing account admin permissions. Environment variable: `CLOUDNGFWAWS_ACCT_ADMIN_ARN`. JSON conf file
variable: `account-admin-arn`.
"""

arn: Optional[str]
"""
The ARN allowing firewall, rulestack, and global rulestack admin permissions. Global rulestack admin permissions can be
enabled only if the AWS account is onboarded by AWS Firewall Manager. Use 'lfa_arn' and 'lra_arn' if you want to enable
only firewall and rulestack admin permissions. Environment variable: `CLOUDNGFWAWS_ARN`. JSON conf file variable: `arn`.
"""

graArn: Optional[str]
"""
The ARN allowing global rulestack admin permissions. Global rulestack admin permissions can be enabled only if the AWS
account is onboarded by AWS Firewall Manager. 'gra_arn' is preferentially used over the `arn` param if both are
specified. Environment variable: `CLOUDNGFWAWS_GRA_ARN`. JSON conf file variable: `gra-arn`.
"""

headers: Optional[str]
"""
Additional HTTP headers to send with API calls. Environment variable: `CLOUDNGFWAWS_HEADERS`. JSON conf file variable:
`headers`.
"""

host: Optional[str]
"""
The hostname of the API (default: `api.us-east-1.aws.cloudngfw.paloaltonetworks.com`). Environment variable:
`CLOUDNGFWAWS_HOST`. JSON conf file variable: `host`.
"""

jsonConfigFile: Optional[str]
"""
Retrieve provider configuration from this JSON file.
"""

lfaArn: Optional[str]
"""
The ARN allowing firewall admin permissions. This is preferentially used over the `arn` param if both are specified.
Environment variable: `CLOUDNGFWAWS_LFA_ARN`. JSON conf file variable: `lfa-arn`.
"""

loggings: Optional[str]
"""
The logging options for the provider. Environment variable: `CLOUDNGFWAWS_LOGGING`. JSON conf file variable: `logging`.
"""

lraArn: Optional[str]
"""
The ARN allowing rulestack admin permissions. This is preferentially used over the `arn` param if both are specified.
Environment variable: `CLOUDNGFWAWS_LRA_ARN`. JSON conf file variable: `lra-arn`.
"""

mpRegion: Optional[str]
"""
AWS management plane region. Environment variable: `CLOUDNGFWAWS_MP_REGION`. JSON conf file variable: `mp_region`.
"""

mpRegionHost: Optional[str]
"""
AWS management plane MP region host Environment variable: `CLOUDNGFWAWS_MP_REGION_HOST`. JSON conf file variable:
`mp_region_host`.
"""

profile: Optional[str]
"""
(Used for the initial `sts assume role`) AWS PROFILE. Environment variable: `CLOUDNGFWAWS_PROFILE`. JSON conf file
variable: `profile`.
"""

protocol: Optional[str]
"""
The protocol (defaults to `https`). Environment variable: `CLOUDNGFWAWS_PROTOCOL`. JSON conf file variable: `protocol`.
Valid values are `https` or `http`.
"""

region: Optional[str]
"""
AWS region. Environment variable: `CLOUDNGFWAWS_REGION`. JSON conf file variable: `region`.
"""

resourceTimeout: Optional[int]

secretKey: Optional[str]
"""
(Used for the initial `sts assume role`) AWS secret key. Environment variable: `CLOUDNGFWAWS_SECRET_KEY`. JSON conf file
variable: `secret-key`.
"""

skipVerifyCertificate: Optional[bool]
"""
Skip verifying the SSL certificate. Environment variable: `CLOUDNGFWAWS_SKIP_VERIFY_CERTIFICATE`. JSON conf file
variable: `skip-verify-certificate`.
"""

syncMode: Optional[bool]
"""
Enable synchronous mode while creating resources Environment variable: `CLOUDNGFWAWS_SYNC_MODE`. JSON conf file
variable: `sync_mode`.
"""

timeout: Optional[int]
"""
The timeout for any single API call (default: `30`). Environment variable: `CLOUDNGFWAWS_TIMEOUT`. JSON conf file
variable: `timeout`.
"""

