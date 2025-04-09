# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
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
from . import outputs
from ._inputs import *

__all__ = ['RulestackArgs', 'Rulestack']

@pulumi.input_type
class RulestackArgs:
    def __init__(__self__, *,
                 profile_config: pulumi.Input['RulestackProfileConfigArgs'],
                 account_group: Optional[pulumi.Input[builtins.str]] = None,
                 account_id: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 lookup_x_forwarded_for: Optional[pulumi.Input[builtins.str]] = None,
                 minimum_app_id_version: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 scope: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        The set of arguments for constructing a Rulestack resource.
        :param pulumi.Input[builtins.str] account_group: Account group.
        :param pulumi.Input[builtins.str] account_id: The account ID.
        :param pulumi.Input[builtins.str] description: The description.
        :param pulumi.Input[builtins.str] lookup_x_forwarded_for: Lookup x forwarded for.
        :param pulumi.Input[builtins.str] minimum_app_id_version: Minimum App-ID version number.
        :param pulumi.Input[builtins.str] name: The name.
        :param pulumi.Input[builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The tags.
        """
        pulumi.set(__self__, "profile_config", profile_config)
        if account_group is not None:
            pulumi.set(__self__, "account_group", account_group)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if lookup_x_forwarded_for is not None:
            pulumi.set(__self__, "lookup_x_forwarded_for", lookup_x_forwarded_for)
        if minimum_app_id_version is not None:
            pulumi.set(__self__, "minimum_app_id_version", minimum_app_id_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="profileConfig")
    def profile_config(self) -> pulumi.Input['RulestackProfileConfigArgs']:
        return pulumi.get(self, "profile_config")

    @profile_config.setter
    def profile_config(self, value: pulumi.Input['RulestackProfileConfigArgs']):
        pulumi.set(self, "profile_config", value)

    @property
    @pulumi.getter(name="accountGroup")
    def account_group(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Account group.
        """
        return pulumi.get(self, "account_group")

    @account_group.setter
    def account_group(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "account_group", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The account ID.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="lookupXForwardedFor")
    def lookup_x_forwarded_for(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Lookup x forwarded for.
        """
        return pulumi.get(self, "lookup_x_forwarded_for")

    @lookup_x_forwarded_for.setter
    def lookup_x_forwarded_for(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "lookup_x_forwarded_for", value)

    @property
    @pulumi.getter(name="minimumAppIdVersion")
    def minimum_app_id_version(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Minimum App-ID version number.
        """
        return pulumi.get(self, "minimum_app_id_version")

    @minimum_app_id_version.setter
    def minimum_app_id_version(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "minimum_app_id_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        The tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _RulestackState:
    def __init__(__self__, *,
                 account_group: Optional[pulumi.Input[builtins.str]] = None,
                 account_id: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 lookup_x_forwarded_for: Optional[pulumi.Input[builtins.str]] = None,
                 minimum_app_id_version: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 profile_config: Optional[pulumi.Input['RulestackProfileConfigArgs']] = None,
                 scope: Optional[pulumi.Input[builtins.str]] = None,
                 state: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None):
        """
        Input properties used for looking up and filtering Rulestack resources.
        :param pulumi.Input[builtins.str] account_group: Account group.
        :param pulumi.Input[builtins.str] account_id: The account ID.
        :param pulumi.Input[builtins.str] description: The description.
        :param pulumi.Input[builtins.str] lookup_x_forwarded_for: Lookup x forwarded for.
        :param pulumi.Input[builtins.str] minimum_app_id_version: Minimum App-ID version number.
        :param pulumi.Input[builtins.str] name: The name.
        :param pulumi.Input[builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        :param pulumi.Input[builtins.str] state: The rulestack state.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The tags.
        """
        if account_group is not None:
            pulumi.set(__self__, "account_group", account_group)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if lookup_x_forwarded_for is not None:
            pulumi.set(__self__, "lookup_x_forwarded_for", lookup_x_forwarded_for)
        if minimum_app_id_version is not None:
            pulumi.set(__self__, "minimum_app_id_version", minimum_app_id_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if profile_config is not None:
            pulumi.set(__self__, "profile_config", profile_config)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accountGroup")
    def account_group(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Account group.
        """
        return pulumi.get(self, "account_group")

    @account_group.setter
    def account_group(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "account_group", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The account ID.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="lookupXForwardedFor")
    def lookup_x_forwarded_for(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Lookup x forwarded for.
        """
        return pulumi.get(self, "lookup_x_forwarded_for")

    @lookup_x_forwarded_for.setter
    def lookup_x_forwarded_for(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "lookup_x_forwarded_for", value)

    @property
    @pulumi.getter(name="minimumAppIdVersion")
    def minimum_app_id_version(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Minimum App-ID version number.
        """
        return pulumi.get(self, "minimum_app_id_version")

    @minimum_app_id_version.setter
    def minimum_app_id_version(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "minimum_app_id_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="profileConfig")
    def profile_config(self) -> Optional[pulumi.Input['RulestackProfileConfigArgs']]:
        return pulumi.get(self, "profile_config")

    @profile_config.setter
    def profile_config(self, value: Optional[pulumi.Input['RulestackProfileConfigArgs']]):
        pulumi.set(self, "profile_config", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The rulestack state.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        The tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "tags", value)


class Rulestack(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_group: Optional[pulumi.Input[builtins.str]] = None,
                 account_id: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 lookup_x_forwarded_for: Optional[pulumi.Input[builtins.str]] = None,
                 minimum_app_id_version: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 profile_config: Optional[pulumi.Input[Union['RulestackProfileConfigArgs', 'RulestackProfileConfigArgsDict']]] = None,
                 scope: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        """
        Resource for rulestack manipulation.

        ## Admin Permission Type

        * `Rulestack` (for `scope="Local"`)
        * `Global Rulestack` (for `scope="Global"`)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudngfwaws as cloudngfwaws

        example = cloudngfwaws.Rulestack("example",
            name="terraform-rulestack",
            scope="Local",
            account_id="123456789",
            description="Made by Pulumi",
            profile_config={
                "anti_spyware": "BestPractice",
            })
        ```

        ## Import

        import name is <scope>:<rulestack>

        ```sh
        $ pulumi import cloudngfwaws:index/rulestack:Rulestack example Local:terraform-rulestack
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] account_group: Account group.
        :param pulumi.Input[builtins.str] account_id: The account ID.
        :param pulumi.Input[builtins.str] description: The description.
        :param pulumi.Input[builtins.str] lookup_x_forwarded_for: Lookup x forwarded for.
        :param pulumi.Input[builtins.str] minimum_app_id_version: Minimum App-ID version number.
        :param pulumi.Input[builtins.str] name: The name.
        :param pulumi.Input[builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RulestackArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for rulestack manipulation.

        ## Admin Permission Type

        * `Rulestack` (for `scope="Local"`)
        * `Global Rulestack` (for `scope="Global"`)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudngfwaws as cloudngfwaws

        example = cloudngfwaws.Rulestack("example",
            name="terraform-rulestack",
            scope="Local",
            account_id="123456789",
            description="Made by Pulumi",
            profile_config={
                "anti_spyware": "BestPractice",
            })
        ```

        ## Import

        import name is <scope>:<rulestack>

        ```sh
        $ pulumi import cloudngfwaws:index/rulestack:Rulestack example Local:terraform-rulestack
        ```

        :param str resource_name: The name of the resource.
        :param RulestackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RulestackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_group: Optional[pulumi.Input[builtins.str]] = None,
                 account_id: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 lookup_x_forwarded_for: Optional[pulumi.Input[builtins.str]] = None,
                 minimum_app_id_version: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 profile_config: Optional[pulumi.Input[Union['RulestackProfileConfigArgs', 'RulestackProfileConfigArgsDict']]] = None,
                 scope: Optional[pulumi.Input[builtins.str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RulestackArgs.__new__(RulestackArgs)

            __props__.__dict__["account_group"] = account_group
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["description"] = description
            __props__.__dict__["lookup_x_forwarded_for"] = lookup_x_forwarded_for
            __props__.__dict__["minimum_app_id_version"] = minimum_app_id_version
            __props__.__dict__["name"] = name
            if profile_config is None and not opts.urn:
                raise TypeError("Missing required property 'profile_config'")
            __props__.__dict__["profile_config"] = profile_config
            __props__.__dict__["scope"] = scope
            __props__.__dict__["tags"] = tags
            __props__.__dict__["state"] = None
        super(Rulestack, __self__).__init__(
            'cloudngfwaws:index/rulestack:Rulestack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_group: Optional[pulumi.Input[builtins.str]] = None,
            account_id: Optional[pulumi.Input[builtins.str]] = None,
            description: Optional[pulumi.Input[builtins.str]] = None,
            lookup_x_forwarded_for: Optional[pulumi.Input[builtins.str]] = None,
            minimum_app_id_version: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            profile_config: Optional[pulumi.Input[Union['RulestackProfileConfigArgs', 'RulestackProfileConfigArgsDict']]] = None,
            scope: Optional[pulumi.Input[builtins.str]] = None,
            state: Optional[pulumi.Input[builtins.str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None) -> 'Rulestack':
        """
        Get an existing Rulestack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] account_group: Account group.
        :param pulumi.Input[builtins.str] account_id: The account ID.
        :param pulumi.Input[builtins.str] description: The description.
        :param pulumi.Input[builtins.str] lookup_x_forwarded_for: Lookup x forwarded for.
        :param pulumi.Input[builtins.str] minimum_app_id_version: Minimum App-ID version number.
        :param pulumi.Input[builtins.str] name: The name.
        :param pulumi.Input[builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        :param pulumi.Input[builtins.str] state: The rulestack state.
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] tags: The tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RulestackState.__new__(_RulestackState)

        __props__.__dict__["account_group"] = account_group
        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["description"] = description
        __props__.__dict__["lookup_x_forwarded_for"] = lookup_x_forwarded_for
        __props__.__dict__["minimum_app_id_version"] = minimum_app_id_version
        __props__.__dict__["name"] = name
        __props__.__dict__["profile_config"] = profile_config
        __props__.__dict__["scope"] = scope
        __props__.__dict__["state"] = state
        __props__.__dict__["tags"] = tags
        return Rulestack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountGroup")
    def account_group(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Account group.
        """
        return pulumi.get(self, "account_group")

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The account ID.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lookupXForwardedFor")
    def lookup_x_forwarded_for(self) -> pulumi.Output[builtins.str]:
        """
        Lookup x forwarded for.
        """
        return pulumi.get(self, "lookup_x_forwarded_for")

    @property
    @pulumi.getter(name="minimumAppIdVersion")
    def minimum_app_id_version(self) -> pulumi.Output[builtins.str]:
        """
        Minimum App-ID version number.
        """
        return pulumi.get(self, "minimum_app_id_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profileConfig")
    def profile_config(self) -> pulumi.Output['outputs.RulestackProfileConfig']:
        return pulumi.get(self, "profile_config")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[builtins.str]:
        """
        The rulestack state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, builtins.str]]]:
        """
        The tags.
        """
        return pulumi.get(self, "tags")

