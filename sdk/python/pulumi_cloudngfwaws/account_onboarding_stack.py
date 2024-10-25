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
from . import _utilities

__all__ = ['AccountOnboardingStackArgs', 'AccountOnboardingStack']

@pulumi.input_type
class AccountOnboardingStackArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 cft_role_name: pulumi.Input[str],
                 external_id: pulumi.Input[str],
                 onboarding_cft: pulumi.Input[str],
                 sns_topic_arn: pulumi.Input[str],
                 trusted_account: pulumi.Input[str],
                 auditlog_group: Optional[pulumi.Input[str]] = None,
                 cloudwatch_log_group: Optional[pulumi.Input[str]] = None,
                 cloudwatch_namespace: Optional[pulumi.Input[str]] = None,
                 decryption_cert: Optional[pulumi.Input[str]] = None,
                 endpoint_mode: Optional[pulumi.Input[str]] = None,
                 kinesis_firehose: Optional[pulumi.Input[str]] = None,
                 s3_bucket: Optional[pulumi.Input[str]] = None,
                 stack_id: Optional[pulumi.Input[str]] = None,
                 stack_status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccountOnboardingStack resource.
        :param pulumi.Input[str] account_id: The account IDs
        :param pulumi.Input[str] cft_role_name: Role name to run the account onboarding CFT in each account to be onboarded.
        :param pulumi.Input[str] external_id: External Id of the onboarded account
        :param pulumi.Input[str] onboarding_cft: Role name to run the account onboarding CFT in each account to be onboarded.
        :param pulumi.Input[str] sns_topic_arn: SNS topic ARN to publish the role ARNs
        :param pulumi.Input[str] trusted_account: PANW Cloud NGFW trusted account Id
        :param pulumi.Input[str] auditlog_group: Audit Log Group Name
        :param pulumi.Input[str] cloudwatch_log_group: Cloudwatch Log Group
        :param pulumi.Input[str] cloudwatch_namespace: Cloudwatch Namespace
        :param pulumi.Input[str] decryption_cert: The CloudNGFW can decrypt inbound and outbound traffic by providing a
               					  certificate stored in secret Manager.
               		 			  The role allows the service to access a certificate configured in the rulestack.
               		 			  Only certificated tagged with PaloAltoCloudNGFW can be accessed
        :param pulumi.Input[str] endpoint_mode: Controls whether cloud NGFW will create firewall endpoints automatitically in customer subnets
        :param pulumi.Input[str] kinesis_firehose: Kinesis Firehose for logging
        :param pulumi.Input[str] s3_bucket: S3 Bucket Name for Logging. Logging roles provide access to create log contents in this bucket.
        :param pulumi.Input[str] stack_id: ID of the account onboarding CFT stack
        :param pulumi.Input[str] stack_status: Status of the account onboarding CFT stack.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "cft_role_name", cft_role_name)
        pulumi.set(__self__, "external_id", external_id)
        pulumi.set(__self__, "onboarding_cft", onboarding_cft)
        pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)
        pulumi.set(__self__, "trusted_account", trusted_account)
        if auditlog_group is not None:
            pulumi.set(__self__, "auditlog_group", auditlog_group)
        if cloudwatch_log_group is not None:
            pulumi.set(__self__, "cloudwatch_log_group", cloudwatch_log_group)
        if cloudwatch_namespace is not None:
            pulumi.set(__self__, "cloudwatch_namespace", cloudwatch_namespace)
        if decryption_cert is not None:
            pulumi.set(__self__, "decryption_cert", decryption_cert)
        if endpoint_mode is not None:
            pulumi.set(__self__, "endpoint_mode", endpoint_mode)
        if kinesis_firehose is not None:
            pulumi.set(__self__, "kinesis_firehose", kinesis_firehose)
        if s3_bucket is not None:
            pulumi.set(__self__, "s3_bucket", s3_bucket)
        if stack_id is not None:
            pulumi.set(__self__, "stack_id", stack_id)
        if stack_status is not None:
            pulumi.set(__self__, "stack_status", stack_status)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        The account IDs
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="cftRoleName")
    def cft_role_name(self) -> pulumi.Input[str]:
        """
        Role name to run the account onboarding CFT in each account to be onboarded.
        """
        return pulumi.get(self, "cft_role_name")

    @cft_role_name.setter
    def cft_role_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cft_role_name", value)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Input[str]:
        """
        External Id of the onboarded account
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="onboardingCft")
    def onboarding_cft(self) -> pulumi.Input[str]:
        """
        Role name to run the account onboarding CFT in each account to be onboarded.
        """
        return pulumi.get(self, "onboarding_cft")

    @onboarding_cft.setter
    def onboarding_cft(self, value: pulumi.Input[str]):
        pulumi.set(self, "onboarding_cft", value)

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Input[str]:
        """
        SNS topic ARN to publish the role ARNs
        """
        return pulumi.get(self, "sns_topic_arn")

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "sns_topic_arn", value)

    @property
    @pulumi.getter(name="trustedAccount")
    def trusted_account(self) -> pulumi.Input[str]:
        """
        PANW Cloud NGFW trusted account Id
        """
        return pulumi.get(self, "trusted_account")

    @trusted_account.setter
    def trusted_account(self, value: pulumi.Input[str]):
        pulumi.set(self, "trusted_account", value)

    @property
    @pulumi.getter(name="auditlogGroup")
    def auditlog_group(self) -> Optional[pulumi.Input[str]]:
        """
        Audit Log Group Name
        """
        return pulumi.get(self, "auditlog_group")

    @auditlog_group.setter
    def auditlog_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auditlog_group", value)

    @property
    @pulumi.getter(name="cloudwatchLogGroup")
    def cloudwatch_log_group(self) -> Optional[pulumi.Input[str]]:
        """
        Cloudwatch Log Group
        """
        return pulumi.get(self, "cloudwatch_log_group")

    @cloudwatch_log_group.setter
    def cloudwatch_log_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloudwatch_log_group", value)

    @property
    @pulumi.getter(name="cloudwatchNamespace")
    def cloudwatch_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Cloudwatch Namespace
        """
        return pulumi.get(self, "cloudwatch_namespace")

    @cloudwatch_namespace.setter
    def cloudwatch_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloudwatch_namespace", value)

    @property
    @pulumi.getter(name="decryptionCert")
    def decryption_cert(self) -> Optional[pulumi.Input[str]]:
        """
        The CloudNGFW can decrypt inbound and outbound traffic by providing a
        					  certificate stored in secret Manager.
        		 			  The role allows the service to access a certificate configured in the rulestack.
        		 			  Only certificated tagged with PaloAltoCloudNGFW can be accessed
        """
        return pulumi.get(self, "decryption_cert")

    @decryption_cert.setter
    def decryption_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "decryption_cert", value)

    @property
    @pulumi.getter(name="endpointMode")
    def endpoint_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Controls whether cloud NGFW will create firewall endpoints automatitically in customer subnets
        """
        return pulumi.get(self, "endpoint_mode")

    @endpoint_mode.setter
    def endpoint_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_mode", value)

    @property
    @pulumi.getter(name="kinesisFirehose")
    def kinesis_firehose(self) -> Optional[pulumi.Input[str]]:
        """
        Kinesis Firehose for logging
        """
        return pulumi.get(self, "kinesis_firehose")

    @kinesis_firehose.setter
    def kinesis_firehose(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kinesis_firehose", value)

    @property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[pulumi.Input[str]]:
        """
        S3 Bucket Name for Logging. Logging roles provide access to create log contents in this bucket.
        """
        return pulumi.get(self, "s3_bucket")

    @s3_bucket.setter
    def s3_bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_bucket", value)

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the account onboarding CFT stack
        """
        return pulumi.get(self, "stack_id")

    @stack_id.setter
    def stack_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stack_id", value)

    @property
    @pulumi.getter(name="stackStatus")
    def stack_status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the account onboarding CFT stack.
        """
        return pulumi.get(self, "stack_status")

    @stack_status.setter
    def stack_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stack_status", value)


@pulumi.input_type
class _AccountOnboardingStackState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 auditlog_group: Optional[pulumi.Input[str]] = None,
                 cft_role_name: Optional[pulumi.Input[str]] = None,
                 cloudwatch_log_group: Optional[pulumi.Input[str]] = None,
                 cloudwatch_namespace: Optional[pulumi.Input[str]] = None,
                 decryption_cert: Optional[pulumi.Input[str]] = None,
                 endpoint_mode: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 kinesis_firehose: Optional[pulumi.Input[str]] = None,
                 onboarding_cft: Optional[pulumi.Input[str]] = None,
                 s3_bucket: Optional[pulumi.Input[str]] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None,
                 stack_id: Optional[pulumi.Input[str]] = None,
                 stack_status: Optional[pulumi.Input[str]] = None,
                 trusted_account: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccountOnboardingStack resources.
        :param pulumi.Input[str] account_id: The account IDs
        :param pulumi.Input[str] auditlog_group: Audit Log Group Name
        :param pulumi.Input[str] cft_role_name: Role name to run the account onboarding CFT in each account to be onboarded.
        :param pulumi.Input[str] cloudwatch_log_group: Cloudwatch Log Group
        :param pulumi.Input[str] cloudwatch_namespace: Cloudwatch Namespace
        :param pulumi.Input[str] decryption_cert: The CloudNGFW can decrypt inbound and outbound traffic by providing a
               					  certificate stored in secret Manager.
               		 			  The role allows the service to access a certificate configured in the rulestack.
               		 			  Only certificated tagged with PaloAltoCloudNGFW can be accessed
        :param pulumi.Input[str] endpoint_mode: Controls whether cloud NGFW will create firewall endpoints automatitically in customer subnets
        :param pulumi.Input[str] external_id: External Id of the onboarded account
        :param pulumi.Input[str] kinesis_firehose: Kinesis Firehose for logging
        :param pulumi.Input[str] onboarding_cft: Role name to run the account onboarding CFT in each account to be onboarded.
        :param pulumi.Input[str] s3_bucket: S3 Bucket Name for Logging. Logging roles provide access to create log contents in this bucket.
        :param pulumi.Input[str] sns_topic_arn: SNS topic ARN to publish the role ARNs
        :param pulumi.Input[str] stack_id: ID of the account onboarding CFT stack
        :param pulumi.Input[str] stack_status: Status of the account onboarding CFT stack.
        :param pulumi.Input[str] trusted_account: PANW Cloud NGFW trusted account Id
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if auditlog_group is not None:
            pulumi.set(__self__, "auditlog_group", auditlog_group)
        if cft_role_name is not None:
            pulumi.set(__self__, "cft_role_name", cft_role_name)
        if cloudwatch_log_group is not None:
            pulumi.set(__self__, "cloudwatch_log_group", cloudwatch_log_group)
        if cloudwatch_namespace is not None:
            pulumi.set(__self__, "cloudwatch_namespace", cloudwatch_namespace)
        if decryption_cert is not None:
            pulumi.set(__self__, "decryption_cert", decryption_cert)
        if endpoint_mode is not None:
            pulumi.set(__self__, "endpoint_mode", endpoint_mode)
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if kinesis_firehose is not None:
            pulumi.set(__self__, "kinesis_firehose", kinesis_firehose)
        if onboarding_cft is not None:
            pulumi.set(__self__, "onboarding_cft", onboarding_cft)
        if s3_bucket is not None:
            pulumi.set(__self__, "s3_bucket", s3_bucket)
        if sns_topic_arn is not None:
            pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)
        if stack_id is not None:
            pulumi.set(__self__, "stack_id", stack_id)
        if stack_status is not None:
            pulumi.set(__self__, "stack_status", stack_status)
        if trusted_account is not None:
            pulumi.set(__self__, "trusted_account", trusted_account)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account IDs
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="auditlogGroup")
    def auditlog_group(self) -> Optional[pulumi.Input[str]]:
        """
        Audit Log Group Name
        """
        return pulumi.get(self, "auditlog_group")

    @auditlog_group.setter
    def auditlog_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auditlog_group", value)

    @property
    @pulumi.getter(name="cftRoleName")
    def cft_role_name(self) -> Optional[pulumi.Input[str]]:
        """
        Role name to run the account onboarding CFT in each account to be onboarded.
        """
        return pulumi.get(self, "cft_role_name")

    @cft_role_name.setter
    def cft_role_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cft_role_name", value)

    @property
    @pulumi.getter(name="cloudwatchLogGroup")
    def cloudwatch_log_group(self) -> Optional[pulumi.Input[str]]:
        """
        Cloudwatch Log Group
        """
        return pulumi.get(self, "cloudwatch_log_group")

    @cloudwatch_log_group.setter
    def cloudwatch_log_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloudwatch_log_group", value)

    @property
    @pulumi.getter(name="cloudwatchNamespace")
    def cloudwatch_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Cloudwatch Namespace
        """
        return pulumi.get(self, "cloudwatch_namespace")

    @cloudwatch_namespace.setter
    def cloudwatch_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloudwatch_namespace", value)

    @property
    @pulumi.getter(name="decryptionCert")
    def decryption_cert(self) -> Optional[pulumi.Input[str]]:
        """
        The CloudNGFW can decrypt inbound and outbound traffic by providing a
        					  certificate stored in secret Manager.
        		 			  The role allows the service to access a certificate configured in the rulestack.
        		 			  Only certificated tagged with PaloAltoCloudNGFW can be accessed
        """
        return pulumi.get(self, "decryption_cert")

    @decryption_cert.setter
    def decryption_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "decryption_cert", value)

    @property
    @pulumi.getter(name="endpointMode")
    def endpoint_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Controls whether cloud NGFW will create firewall endpoints automatitically in customer subnets
        """
        return pulumi.get(self, "endpoint_mode")

    @endpoint_mode.setter
    def endpoint_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_mode", value)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[str]]:
        """
        External Id of the onboarded account
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="kinesisFirehose")
    def kinesis_firehose(self) -> Optional[pulumi.Input[str]]:
        """
        Kinesis Firehose for logging
        """
        return pulumi.get(self, "kinesis_firehose")

    @kinesis_firehose.setter
    def kinesis_firehose(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kinesis_firehose", value)

    @property
    @pulumi.getter(name="onboardingCft")
    def onboarding_cft(self) -> Optional[pulumi.Input[str]]:
        """
        Role name to run the account onboarding CFT in each account to be onboarded.
        """
        return pulumi.get(self, "onboarding_cft")

    @onboarding_cft.setter
    def onboarding_cft(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "onboarding_cft", value)

    @property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[pulumi.Input[str]]:
        """
        S3 Bucket Name for Logging. Logging roles provide access to create log contents in this bucket.
        """
        return pulumi.get(self, "s3_bucket")

    @s3_bucket.setter
    def s3_bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_bucket", value)

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[str]]:
        """
        SNS topic ARN to publish the role ARNs
        """
        return pulumi.get(self, "sns_topic_arn")

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sns_topic_arn", value)

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the account onboarding CFT stack
        """
        return pulumi.get(self, "stack_id")

    @stack_id.setter
    def stack_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stack_id", value)

    @property
    @pulumi.getter(name="stackStatus")
    def stack_status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the account onboarding CFT stack.
        """
        return pulumi.get(self, "stack_status")

    @stack_status.setter
    def stack_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stack_status", value)

    @property
    @pulumi.getter(name="trustedAccount")
    def trusted_account(self) -> Optional[pulumi.Input[str]]:
        """
        PANW Cloud NGFW trusted account Id
        """
        return pulumi.get(self, "trusted_account")

    @trusted_account.setter
    def trusted_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trusted_account", value)


class AccountOnboardingStack(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 auditlog_group: Optional[pulumi.Input[str]] = None,
                 cft_role_name: Optional[pulumi.Input[str]] = None,
                 cloudwatch_log_group: Optional[pulumi.Input[str]] = None,
                 cloudwatch_namespace: Optional[pulumi.Input[str]] = None,
                 decryption_cert: Optional[pulumi.Input[str]] = None,
                 endpoint_mode: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 kinesis_firehose: Optional[pulumi.Input[str]] = None,
                 onboarding_cft: Optional[pulumi.Input[str]] = None,
                 s3_bucket: Optional[pulumi.Input[str]] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None,
                 stack_id: Optional[pulumi.Input[str]] = None,
                 stack_status: Optional[pulumi.Input[str]] = None,
                 trusted_account: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource for Account Onboarding.

        ## Admin Permission Type

        * `Rulestack` (for `scope="Local"`)
        * `Global Rulestack` (for `scope="Global"`)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account IDs
        :param pulumi.Input[str] auditlog_group: Audit Log Group Name
        :param pulumi.Input[str] cft_role_name: Role name to run the account onboarding CFT in each account to be onboarded.
        :param pulumi.Input[str] cloudwatch_log_group: Cloudwatch Log Group
        :param pulumi.Input[str] cloudwatch_namespace: Cloudwatch Namespace
        :param pulumi.Input[str] decryption_cert: The CloudNGFW can decrypt inbound and outbound traffic by providing a
               					  certificate stored in secret Manager.
               		 			  The role allows the service to access a certificate configured in the rulestack.
               		 			  Only certificated tagged with PaloAltoCloudNGFW can be accessed
        :param pulumi.Input[str] endpoint_mode: Controls whether cloud NGFW will create firewall endpoints automatitically in customer subnets
        :param pulumi.Input[str] external_id: External Id of the onboarded account
        :param pulumi.Input[str] kinesis_firehose: Kinesis Firehose for logging
        :param pulumi.Input[str] onboarding_cft: Role name to run the account onboarding CFT in each account to be onboarded.
        :param pulumi.Input[str] s3_bucket: S3 Bucket Name for Logging. Logging roles provide access to create log contents in this bucket.
        :param pulumi.Input[str] sns_topic_arn: SNS topic ARN to publish the role ARNs
        :param pulumi.Input[str] stack_id: ID of the account onboarding CFT stack
        :param pulumi.Input[str] stack_status: Status of the account onboarding CFT stack.
        :param pulumi.Input[str] trusted_account: PANW Cloud NGFW trusted account Id
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountOnboardingStackArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for Account Onboarding.

        ## Admin Permission Type

        * `Rulestack` (for `scope="Local"`)
        * `Global Rulestack` (for `scope="Global"`)

        :param str resource_name: The name of the resource.
        :param AccountOnboardingStackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountOnboardingStackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 auditlog_group: Optional[pulumi.Input[str]] = None,
                 cft_role_name: Optional[pulumi.Input[str]] = None,
                 cloudwatch_log_group: Optional[pulumi.Input[str]] = None,
                 cloudwatch_namespace: Optional[pulumi.Input[str]] = None,
                 decryption_cert: Optional[pulumi.Input[str]] = None,
                 endpoint_mode: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 kinesis_firehose: Optional[pulumi.Input[str]] = None,
                 onboarding_cft: Optional[pulumi.Input[str]] = None,
                 s3_bucket: Optional[pulumi.Input[str]] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None,
                 stack_id: Optional[pulumi.Input[str]] = None,
                 stack_status: Optional[pulumi.Input[str]] = None,
                 trusted_account: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountOnboardingStackArgs.__new__(AccountOnboardingStackArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["auditlog_group"] = auditlog_group
            if cft_role_name is None and not opts.urn:
                raise TypeError("Missing required property 'cft_role_name'")
            __props__.__dict__["cft_role_name"] = cft_role_name
            __props__.__dict__["cloudwatch_log_group"] = cloudwatch_log_group
            __props__.__dict__["cloudwatch_namespace"] = cloudwatch_namespace
            __props__.__dict__["decryption_cert"] = decryption_cert
            __props__.__dict__["endpoint_mode"] = endpoint_mode
            if external_id is None and not opts.urn:
                raise TypeError("Missing required property 'external_id'")
            __props__.__dict__["external_id"] = external_id
            __props__.__dict__["kinesis_firehose"] = kinesis_firehose
            if onboarding_cft is None and not opts.urn:
                raise TypeError("Missing required property 'onboarding_cft'")
            __props__.__dict__["onboarding_cft"] = onboarding_cft
            __props__.__dict__["s3_bucket"] = s3_bucket
            if sns_topic_arn is None and not opts.urn:
                raise TypeError("Missing required property 'sns_topic_arn'")
            __props__.__dict__["sns_topic_arn"] = sns_topic_arn
            __props__.__dict__["stack_id"] = stack_id
            __props__.__dict__["stack_status"] = stack_status
            if trusted_account is None and not opts.urn:
                raise TypeError("Missing required property 'trusted_account'")
            __props__.__dict__["trusted_account"] = trusted_account
        super(AccountOnboardingStack, __self__).__init__(
            'cloudngfwaws:index/accountOnboardingStack:AccountOnboardingStack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            auditlog_group: Optional[pulumi.Input[str]] = None,
            cft_role_name: Optional[pulumi.Input[str]] = None,
            cloudwatch_log_group: Optional[pulumi.Input[str]] = None,
            cloudwatch_namespace: Optional[pulumi.Input[str]] = None,
            decryption_cert: Optional[pulumi.Input[str]] = None,
            endpoint_mode: Optional[pulumi.Input[str]] = None,
            external_id: Optional[pulumi.Input[str]] = None,
            kinesis_firehose: Optional[pulumi.Input[str]] = None,
            onboarding_cft: Optional[pulumi.Input[str]] = None,
            s3_bucket: Optional[pulumi.Input[str]] = None,
            sns_topic_arn: Optional[pulumi.Input[str]] = None,
            stack_id: Optional[pulumi.Input[str]] = None,
            stack_status: Optional[pulumi.Input[str]] = None,
            trusted_account: Optional[pulumi.Input[str]] = None) -> 'AccountOnboardingStack':
        """
        Get an existing AccountOnboardingStack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account IDs
        :param pulumi.Input[str] auditlog_group: Audit Log Group Name
        :param pulumi.Input[str] cft_role_name: Role name to run the account onboarding CFT in each account to be onboarded.
        :param pulumi.Input[str] cloudwatch_log_group: Cloudwatch Log Group
        :param pulumi.Input[str] cloudwatch_namespace: Cloudwatch Namespace
        :param pulumi.Input[str] decryption_cert: The CloudNGFW can decrypt inbound and outbound traffic by providing a
               					  certificate stored in secret Manager.
               		 			  The role allows the service to access a certificate configured in the rulestack.
               		 			  Only certificated tagged with PaloAltoCloudNGFW can be accessed
        :param pulumi.Input[str] endpoint_mode: Controls whether cloud NGFW will create firewall endpoints automatitically in customer subnets
        :param pulumi.Input[str] external_id: External Id of the onboarded account
        :param pulumi.Input[str] kinesis_firehose: Kinesis Firehose for logging
        :param pulumi.Input[str] onboarding_cft: Role name to run the account onboarding CFT in each account to be onboarded.
        :param pulumi.Input[str] s3_bucket: S3 Bucket Name for Logging. Logging roles provide access to create log contents in this bucket.
        :param pulumi.Input[str] sns_topic_arn: SNS topic ARN to publish the role ARNs
        :param pulumi.Input[str] stack_id: ID of the account onboarding CFT stack
        :param pulumi.Input[str] stack_status: Status of the account onboarding CFT stack.
        :param pulumi.Input[str] trusted_account: PANW Cloud NGFW trusted account Id
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountOnboardingStackState.__new__(_AccountOnboardingStackState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["auditlog_group"] = auditlog_group
        __props__.__dict__["cft_role_name"] = cft_role_name
        __props__.__dict__["cloudwatch_log_group"] = cloudwatch_log_group
        __props__.__dict__["cloudwatch_namespace"] = cloudwatch_namespace
        __props__.__dict__["decryption_cert"] = decryption_cert
        __props__.__dict__["endpoint_mode"] = endpoint_mode
        __props__.__dict__["external_id"] = external_id
        __props__.__dict__["kinesis_firehose"] = kinesis_firehose
        __props__.__dict__["onboarding_cft"] = onboarding_cft
        __props__.__dict__["s3_bucket"] = s3_bucket
        __props__.__dict__["sns_topic_arn"] = sns_topic_arn
        __props__.__dict__["stack_id"] = stack_id
        __props__.__dict__["stack_status"] = stack_status
        __props__.__dict__["trusted_account"] = trusted_account
        return AccountOnboardingStack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account IDs
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="auditlogGroup")
    def auditlog_group(self) -> pulumi.Output[Optional[str]]:
        """
        Audit Log Group Name
        """
        return pulumi.get(self, "auditlog_group")

    @property
    @pulumi.getter(name="cftRoleName")
    def cft_role_name(self) -> pulumi.Output[str]:
        """
        Role name to run the account onboarding CFT in each account to be onboarded.
        """
        return pulumi.get(self, "cft_role_name")

    @property
    @pulumi.getter(name="cloudwatchLogGroup")
    def cloudwatch_log_group(self) -> pulumi.Output[Optional[str]]:
        """
        Cloudwatch Log Group
        """
        return pulumi.get(self, "cloudwatch_log_group")

    @property
    @pulumi.getter(name="cloudwatchNamespace")
    def cloudwatch_namespace(self) -> pulumi.Output[Optional[str]]:
        """
        Cloudwatch Namespace
        """
        return pulumi.get(self, "cloudwatch_namespace")

    @property
    @pulumi.getter(name="decryptionCert")
    def decryption_cert(self) -> pulumi.Output[Optional[str]]:
        """
        The CloudNGFW can decrypt inbound and outbound traffic by providing a
        					  certificate stored in secret Manager.
        		 			  The role allows the service to access a certificate configured in the rulestack.
        		 			  Only certificated tagged with PaloAltoCloudNGFW can be accessed
        """
        return pulumi.get(self, "decryption_cert")

    @property
    @pulumi.getter(name="endpointMode")
    def endpoint_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Controls whether cloud NGFW will create firewall endpoints automatitically in customer subnets
        """
        return pulumi.get(self, "endpoint_mode")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[str]:
        """
        External Id of the onboarded account
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter(name="kinesisFirehose")
    def kinesis_firehose(self) -> pulumi.Output[Optional[str]]:
        """
        Kinesis Firehose for logging
        """
        return pulumi.get(self, "kinesis_firehose")

    @property
    @pulumi.getter(name="onboardingCft")
    def onboarding_cft(self) -> pulumi.Output[str]:
        """
        Role name to run the account onboarding CFT in each account to be onboarded.
        """
        return pulumi.get(self, "onboarding_cft")

    @property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Output[Optional[str]]:
        """
        S3 Bucket Name for Logging. Logging roles provide access to create log contents in this bucket.
        """
        return pulumi.get(self, "s3_bucket")

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Output[str]:
        """
        SNS topic ARN to publish the role ARNs
        """
        return pulumi.get(self, "sns_topic_arn")

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> pulumi.Output[str]:
        """
        ID of the account onboarding CFT stack
        """
        return pulumi.get(self, "stack_id")

    @property
    @pulumi.getter(name="stackStatus")
    def stack_status(self) -> pulumi.Output[str]:
        """
        Status of the account onboarding CFT stack.
        """
        return pulumi.get(self, "stack_status")

    @property
    @pulumi.getter(name="trustedAccount")
    def trusted_account(self) -> pulumi.Output[str]:
        """
        PANW Cloud NGFW trusted account Id
        """
        return pulumi.get(self, "trusted_account")

