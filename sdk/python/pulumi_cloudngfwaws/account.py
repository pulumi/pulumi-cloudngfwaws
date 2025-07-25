# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins as _builtins
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

__all__ = ['AccountArgs', 'Account']

@pulumi.input_type
class AccountArgs:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[_builtins.str]] = None,
                 cft_url: Optional[pulumi.Input[_builtins.str]] = None,
                 external_id: Optional[pulumi.Input[_builtins.str]] = None,
                 onboarding_status: Optional[pulumi.Input[_builtins.str]] = None,
                 origin: Optional[pulumi.Input[_builtins.str]] = None,
                 service_account_id: Optional[pulumi.Input[_builtins.str]] = None,
                 sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = None,
                 trusted_account: Optional[pulumi.Input[_builtins.str]] = None):
        """
        The set of arguments for constructing a Account resource.
        :param pulumi.Input[_builtins.str] account_id: The account ID
        :param pulumi.Input[_builtins.str] cft_url: The CFT URL.
        :param pulumi.Input[_builtins.str] external_id: The external ID of the account
        :param pulumi.Input[_builtins.str] onboarding_status: The Account onboarding status
        :param pulumi.Input[_builtins.str] origin: Origin of account onboarding
        :param pulumi.Input[_builtins.str] service_account_id: The account ID of cloud NGFW service
        :param pulumi.Input[_builtins.str] sns_topic_arn: The SNS topic ARN
        :param pulumi.Input[_builtins.str] trusted_account: The trusted account ID
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if cft_url is not None:
            pulumi.set(__self__, "cft_url", cft_url)
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if onboarding_status is not None:
            pulumi.set(__self__, "onboarding_status", onboarding_status)
        if origin is not None:
            pulumi.set(__self__, "origin", origin)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)
        if sns_topic_arn is not None:
            pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)
        if trusted_account is not None:
            pulumi.set(__self__, "trusted_account", trusted_account)

    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The account ID
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "account_id", value)

    @_builtins.property
    @pulumi.getter(name="cftUrl")
    def cft_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The CFT URL.
        """
        return pulumi.get(self, "cft_url")

    @cft_url.setter
    def cft_url(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "cft_url", value)

    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The external ID of the account
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "external_id", value)

    @_builtins.property
    @pulumi.getter(name="onboardingStatus")
    def onboarding_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The Account onboarding status
        """
        return pulumi.get(self, "onboarding_status")

    @onboarding_status.setter
    def onboarding_status(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "onboarding_status", value)

    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        Origin of account onboarding
        """
        return pulumi.get(self, "origin")

    @origin.setter
    def origin(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "origin", value)

    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The account ID of cloud NGFW service
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "service_account_id", value)

    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The SNS topic ARN
        """
        return pulumi.get(self, "sns_topic_arn")

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "sns_topic_arn", value)

    @_builtins.property
    @pulumi.getter(name="trustedAccount")
    def trusted_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The trusted account ID
        """
        return pulumi.get(self, "trusted_account")

    @trusted_account.setter
    def trusted_account(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "trusted_account", value)


@pulumi.input_type
class _AccountState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[_builtins.str]] = None,
                 cft_url: Optional[pulumi.Input[_builtins.str]] = None,
                 external_id: Optional[pulumi.Input[_builtins.str]] = None,
                 onboarding_status: Optional[pulumi.Input[_builtins.str]] = None,
                 origin: Optional[pulumi.Input[_builtins.str]] = None,
                 service_account_id: Optional[pulumi.Input[_builtins.str]] = None,
                 sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = None,
                 trusted_account: Optional[pulumi.Input[_builtins.str]] = None,
                 update_token: Optional[pulumi.Input[_builtins.str]] = None):
        """
        Input properties used for looking up and filtering Account resources.
        :param pulumi.Input[_builtins.str] account_id: The account ID
        :param pulumi.Input[_builtins.str] cft_url: The CFT URL.
        :param pulumi.Input[_builtins.str] external_id: The external ID of the account
        :param pulumi.Input[_builtins.str] onboarding_status: The Account onboarding status
        :param pulumi.Input[_builtins.str] origin: Origin of account onboarding
        :param pulumi.Input[_builtins.str] service_account_id: The account ID of cloud NGFW service
        :param pulumi.Input[_builtins.str] sns_topic_arn: The SNS topic ARN
        :param pulumi.Input[_builtins.str] trusted_account: The trusted account ID
        :param pulumi.Input[_builtins.str] update_token: The update token.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if cft_url is not None:
            pulumi.set(__self__, "cft_url", cft_url)
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if onboarding_status is not None:
            pulumi.set(__self__, "onboarding_status", onboarding_status)
        if origin is not None:
            pulumi.set(__self__, "origin", origin)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)
        if sns_topic_arn is not None:
            pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)
        if trusted_account is not None:
            pulumi.set(__self__, "trusted_account", trusted_account)
        if update_token is not None:
            pulumi.set(__self__, "update_token", update_token)

    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The account ID
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "account_id", value)

    @_builtins.property
    @pulumi.getter(name="cftUrl")
    def cft_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The CFT URL.
        """
        return pulumi.get(self, "cft_url")

    @cft_url.setter
    def cft_url(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "cft_url", value)

    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The external ID of the account
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "external_id", value)

    @_builtins.property
    @pulumi.getter(name="onboardingStatus")
    def onboarding_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The Account onboarding status
        """
        return pulumi.get(self, "onboarding_status")

    @onboarding_status.setter
    def onboarding_status(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "onboarding_status", value)

    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        Origin of account onboarding
        """
        return pulumi.get(self, "origin")

    @origin.setter
    def origin(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "origin", value)

    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The account ID of cloud NGFW service
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "service_account_id", value)

    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The SNS topic ARN
        """
        return pulumi.get(self, "sns_topic_arn")

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "sns_topic_arn", value)

    @_builtins.property
    @pulumi.getter(name="trustedAccount")
    def trusted_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The trusted account ID
        """
        return pulumi.get(self, "trusted_account")

    @trusted_account.setter
    def trusted_account(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "trusted_account", value)

    @_builtins.property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The update token.
        """
        return pulumi.get(self, "update_token")

    @update_token.setter
    def update_token(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "update_token", value)


@pulumi.type_token("cloudngfwaws:index/account:Account")
class Account(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[_builtins.str]] = None,
                 cft_url: Optional[pulumi.Input[_builtins.str]] = None,
                 external_id: Optional[pulumi.Input[_builtins.str]] = None,
                 onboarding_status: Optional[pulumi.Input[_builtins.str]] = None,
                 origin: Optional[pulumi.Input[_builtins.str]] = None,
                 service_account_id: Optional[pulumi.Input[_builtins.str]] = None,
                 sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = None,
                 trusted_account: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        """
        Resource for Account manipulation.

        ## Admin Permission Type

        * `Rulestack` (for `scope="Local"`)
        * `Global Rulestack` (for `scope="Global"`)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[_builtins.str] account_id: The account ID
        :param pulumi.Input[_builtins.str] cft_url: The CFT URL.
        :param pulumi.Input[_builtins.str] external_id: The external ID of the account
        :param pulumi.Input[_builtins.str] onboarding_status: The Account onboarding status
        :param pulumi.Input[_builtins.str] origin: Origin of account onboarding
        :param pulumi.Input[_builtins.str] service_account_id: The account ID of cloud NGFW service
        :param pulumi.Input[_builtins.str] sns_topic_arn: The SNS topic ARN
        :param pulumi.Input[_builtins.str] trusted_account: The trusted account ID
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AccountArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for Account manipulation.

        ## Admin Permission Type

        * `Rulestack` (for `scope="Local"`)
        * `Global Rulestack` (for `scope="Global"`)

        :param str resource_name: The name of the resource.
        :param AccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[_builtins.str]] = None,
                 cft_url: Optional[pulumi.Input[_builtins.str]] = None,
                 external_id: Optional[pulumi.Input[_builtins.str]] = None,
                 onboarding_status: Optional[pulumi.Input[_builtins.str]] = None,
                 origin: Optional[pulumi.Input[_builtins.str]] = None,
                 service_account_id: Optional[pulumi.Input[_builtins.str]] = None,
                 sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = None,
                 trusted_account: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountArgs.__new__(AccountArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["cft_url"] = cft_url
            __props__.__dict__["external_id"] = external_id
            __props__.__dict__["onboarding_status"] = onboarding_status
            __props__.__dict__["origin"] = origin
            __props__.__dict__["service_account_id"] = service_account_id
            __props__.__dict__["sns_topic_arn"] = sns_topic_arn
            __props__.__dict__["trusted_account"] = trusted_account
            __props__.__dict__["update_token"] = None
        super(Account, __self__).__init__(
            'cloudngfwaws:index/account:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[_builtins.str]] = None,
            cft_url: Optional[pulumi.Input[_builtins.str]] = None,
            external_id: Optional[pulumi.Input[_builtins.str]] = None,
            onboarding_status: Optional[pulumi.Input[_builtins.str]] = None,
            origin: Optional[pulumi.Input[_builtins.str]] = None,
            service_account_id: Optional[pulumi.Input[_builtins.str]] = None,
            sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = None,
            trusted_account: Optional[pulumi.Input[_builtins.str]] = None,
            update_token: Optional[pulumi.Input[_builtins.str]] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[_builtins.str] account_id: The account ID
        :param pulumi.Input[_builtins.str] cft_url: The CFT URL.
        :param pulumi.Input[_builtins.str] external_id: The external ID of the account
        :param pulumi.Input[_builtins.str] onboarding_status: The Account onboarding status
        :param pulumi.Input[_builtins.str] origin: Origin of account onboarding
        :param pulumi.Input[_builtins.str] service_account_id: The account ID of cloud NGFW service
        :param pulumi.Input[_builtins.str] sns_topic_arn: The SNS topic ARN
        :param pulumi.Input[_builtins.str] trusted_account: The trusted account ID
        :param pulumi.Input[_builtins.str] update_token: The update token.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountState.__new__(_AccountState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["cft_url"] = cft_url
        __props__.__dict__["external_id"] = external_id
        __props__.__dict__["onboarding_status"] = onboarding_status
        __props__.__dict__["origin"] = origin
        __props__.__dict__["service_account_id"] = service_account_id
        __props__.__dict__["sns_topic_arn"] = sns_topic_arn
        __props__.__dict__["trusted_account"] = trusted_account
        __props__.__dict__["update_token"] = update_token
        return Account(resource_name, opts=opts, __props__=__props__)

    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        """
        The account ID
        """
        return pulumi.get(self, "account_id")

    @_builtins.property
    @pulumi.getter(name="cftUrl")
    def cft_url(self) -> pulumi.Output[_builtins.str]:
        """
        The CFT URL.
        """
        return pulumi.get(self, "cft_url")

    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[_builtins.str]:
        """
        The external ID of the account
        """
        return pulumi.get(self, "external_id")

    @_builtins.property
    @pulumi.getter(name="onboardingStatus")
    def onboarding_status(self) -> pulumi.Output[_builtins.str]:
        """
        The Account onboarding status
        """
        return pulumi.get(self, "onboarding_status")

    @_builtins.property
    @pulumi.getter
    def origin(self) -> pulumi.Output[_builtins.str]:
        """
        Origin of account onboarding
        """
        return pulumi.get(self, "origin")

    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Output[_builtins.str]:
        """
        The account ID of cloud NGFW service
        """
        return pulumi.get(self, "service_account_id")

    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Output[_builtins.str]:
        """
        The SNS topic ARN
        """
        return pulumi.get(self, "sns_topic_arn")

    @_builtins.property
    @pulumi.getter(name="trustedAccount")
    def trusted_account(self) -> pulumi.Output[_builtins.str]:
        """
        The trusted account ID
        """
        return pulumi.get(self, "trusted_account")

    @_builtins.property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> pulumi.Output[_builtins.str]:
        """
        The update token.
        """
        return pulumi.get(self, "update_token")

