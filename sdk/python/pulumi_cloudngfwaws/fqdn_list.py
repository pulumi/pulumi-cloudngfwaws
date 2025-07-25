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

__all__ = ['FqdnListArgs', 'FqdnList']

@pulumi.input_type
class FqdnListArgs:
    def __init__(__self__, *,
                 fqdn_lists: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
                 rulestack: pulumi.Input[_builtins.str],
                 audit_comment: Optional[pulumi.Input[_builtins.str]] = None,
                 description: Optional[pulumi.Input[_builtins.str]] = None,
                 name: Optional[pulumi.Input[_builtins.str]] = None,
                 scope: Optional[pulumi.Input[_builtins.str]] = None):
        """
        The set of arguments for constructing a FqdnList resource.
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] fqdn_lists: The fqdn list.
        :param pulumi.Input[_builtins.str] rulestack: The rulestack.
        :param pulumi.Input[_builtins.str] audit_comment: The audit comment.
        :param pulumi.Input[_builtins.str] description: The description.
        :param pulumi.Input[_builtins.str] name: The name.
        :param pulumi.Input[_builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        """
        pulumi.set(__self__, "fqdn_lists", fqdn_lists)
        pulumi.set(__self__, "rulestack", rulestack)
        if audit_comment is not None:
            pulumi.set(__self__, "audit_comment", audit_comment)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @_builtins.property
    @pulumi.getter(name="fqdnLists")
    def fqdn_lists(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        """
        The fqdn list.
        """
        return pulumi.get(self, "fqdn_lists")

    @fqdn_lists.setter
    def fqdn_lists(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]):
        pulumi.set(self, "fqdn_lists", value)

    @_builtins.property
    @pulumi.getter
    def rulestack(self) -> pulumi.Input[_builtins.str]:
        """
        The rulestack.
        """
        return pulumi.get(self, "rulestack")

    @rulestack.setter
    def rulestack(self, value: pulumi.Input[_builtins.str]):
        pulumi.set(self, "rulestack", value)

    @_builtins.property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The audit comment.
        """
        return pulumi.get(self, "audit_comment")

    @audit_comment.setter
    def audit_comment(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "audit_comment", value)

    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "description", value)

    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "name", value)

    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "scope", value)


@pulumi.input_type
class _FqdnListState:
    def __init__(__self__, *,
                 audit_comment: Optional[pulumi.Input[_builtins.str]] = None,
                 description: Optional[pulumi.Input[_builtins.str]] = None,
                 fqdn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
                 name: Optional[pulumi.Input[_builtins.str]] = None,
                 rulestack: Optional[pulumi.Input[_builtins.str]] = None,
                 scope: Optional[pulumi.Input[_builtins.str]] = None,
                 update_token: Optional[pulumi.Input[_builtins.str]] = None):
        """
        Input properties used for looking up and filtering FqdnList resources.
        :param pulumi.Input[_builtins.str] audit_comment: The audit comment.
        :param pulumi.Input[_builtins.str] description: The description.
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] fqdn_lists: The fqdn list.
        :param pulumi.Input[_builtins.str] name: The name.
        :param pulumi.Input[_builtins.str] rulestack: The rulestack.
        :param pulumi.Input[_builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        :param pulumi.Input[_builtins.str] update_token: The update token.
        """
        if audit_comment is not None:
            pulumi.set(__self__, "audit_comment", audit_comment)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if fqdn_lists is not None:
            pulumi.set(__self__, "fqdn_lists", fqdn_lists)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rulestack is not None:
            pulumi.set(__self__, "rulestack", rulestack)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if update_token is not None:
            pulumi.set(__self__, "update_token", update_token)

    @_builtins.property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The audit comment.
        """
        return pulumi.get(self, "audit_comment")

    @audit_comment.setter
    def audit_comment(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "audit_comment", value)

    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "description", value)

    @_builtins.property
    @pulumi.getter(name="fqdnLists")
    def fqdn_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        """
        The fqdn list.
        """
        return pulumi.get(self, "fqdn_lists")

    @fqdn_lists.setter
    def fqdn_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]):
        pulumi.set(self, "fqdn_lists", value)

    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "name", value)

    @_builtins.property
    @pulumi.getter
    def rulestack(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The rulestack.
        """
        return pulumi.get(self, "rulestack")

    @rulestack.setter
    def rulestack(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "rulestack", value)

    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "scope", value)

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


@pulumi.type_token("cloudngfwaws:index/fqdnList:FqdnList")
class FqdnList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_comment: Optional[pulumi.Input[_builtins.str]] = None,
                 description: Optional[pulumi.Input[_builtins.str]] = None,
                 fqdn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
                 name: Optional[pulumi.Input[_builtins.str]] = None,
                 rulestack: Optional[pulumi.Input[_builtins.str]] = None,
                 scope: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        """
        Resource for fqdn list manipulation.

        ## Admin Permission Type

        * `Rulestack` (for `scope="Local"`)
        * `Global Rulestack` (for `scope="Global"`)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudngfwaws as cloudngfwaws

        r = cloudngfwaws.Rulestack("r",
            name="terraform-rulestack",
            scope="Local",
            account_id="123456789",
            description="Made by Pulumi",
            profile_config={
                "anti_spyware": "BestPractice",
            })
        example = cloudngfwaws.FqdnList("example",
            rulestack=r.name,
            name="tf-fqdn-list",
            description="Also configured by Terraform",
            fqdn_lists=[
                "example.com",
                "foobar.org",
            ],
            audit_comment="initial config")
        ```

        ## Import

        import name is <scope>:<rulestack>:<fqdn_list_name>

        ```sh
        $ pulumi import cloudngfwaws:index/fqdnList:FqdnList example Local:terraform-rulestack:tf-fqdn-list
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[_builtins.str] audit_comment: The audit comment.
        :param pulumi.Input[_builtins.str] description: The description.
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] fqdn_lists: The fqdn list.
        :param pulumi.Input[_builtins.str] name: The name.
        :param pulumi.Input[_builtins.str] rulestack: The rulestack.
        :param pulumi.Input[_builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FqdnListArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for fqdn list manipulation.

        ## Admin Permission Type

        * `Rulestack` (for `scope="Local"`)
        * `Global Rulestack` (for `scope="Global"`)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudngfwaws as cloudngfwaws

        r = cloudngfwaws.Rulestack("r",
            name="terraform-rulestack",
            scope="Local",
            account_id="123456789",
            description="Made by Pulumi",
            profile_config={
                "anti_spyware": "BestPractice",
            })
        example = cloudngfwaws.FqdnList("example",
            rulestack=r.name,
            name="tf-fqdn-list",
            description="Also configured by Terraform",
            fqdn_lists=[
                "example.com",
                "foobar.org",
            ],
            audit_comment="initial config")
        ```

        ## Import

        import name is <scope>:<rulestack>:<fqdn_list_name>

        ```sh
        $ pulumi import cloudngfwaws:index/fqdnList:FqdnList example Local:terraform-rulestack:tf-fqdn-list
        ```

        :param str resource_name: The name of the resource.
        :param FqdnListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FqdnListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_comment: Optional[pulumi.Input[_builtins.str]] = None,
                 description: Optional[pulumi.Input[_builtins.str]] = None,
                 fqdn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
                 name: Optional[pulumi.Input[_builtins.str]] = None,
                 rulestack: Optional[pulumi.Input[_builtins.str]] = None,
                 scope: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FqdnListArgs.__new__(FqdnListArgs)

            __props__.__dict__["audit_comment"] = audit_comment
            __props__.__dict__["description"] = description
            if fqdn_lists is None and not opts.urn:
                raise TypeError("Missing required property 'fqdn_lists'")
            __props__.__dict__["fqdn_lists"] = fqdn_lists
            __props__.__dict__["name"] = name
            if rulestack is None and not opts.urn:
                raise TypeError("Missing required property 'rulestack'")
            __props__.__dict__["rulestack"] = rulestack
            __props__.__dict__["scope"] = scope
            __props__.__dict__["update_token"] = None
        super(FqdnList, __self__).__init__(
            'cloudngfwaws:index/fqdnList:FqdnList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            audit_comment: Optional[pulumi.Input[_builtins.str]] = None,
            description: Optional[pulumi.Input[_builtins.str]] = None,
            fqdn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
            name: Optional[pulumi.Input[_builtins.str]] = None,
            rulestack: Optional[pulumi.Input[_builtins.str]] = None,
            scope: Optional[pulumi.Input[_builtins.str]] = None,
            update_token: Optional[pulumi.Input[_builtins.str]] = None) -> 'FqdnList':
        """
        Get an existing FqdnList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[_builtins.str] audit_comment: The audit comment.
        :param pulumi.Input[_builtins.str] description: The description.
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] fqdn_lists: The fqdn list.
        :param pulumi.Input[_builtins.str] name: The name.
        :param pulumi.Input[_builtins.str] rulestack: The rulestack.
        :param pulumi.Input[_builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        :param pulumi.Input[_builtins.str] update_token: The update token.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FqdnListState.__new__(_FqdnListState)

        __props__.__dict__["audit_comment"] = audit_comment
        __props__.__dict__["description"] = description
        __props__.__dict__["fqdn_lists"] = fqdn_lists
        __props__.__dict__["name"] = name
        __props__.__dict__["rulestack"] = rulestack
        __props__.__dict__["scope"] = scope
        __props__.__dict__["update_token"] = update_token
        return FqdnList(resource_name, opts=opts, __props__=__props__)

    @_builtins.property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> pulumi.Output[Optional[_builtins.str]]:
        """
        The audit comment.
        """
        return pulumi.get(self, "audit_comment")

    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @_builtins.property
    @pulumi.getter(name="fqdnLists")
    def fqdn_lists(self) -> pulumi.Output[Sequence[_builtins.str]]:
        """
        The fqdn list.
        """
        return pulumi.get(self, "fqdn_lists")

    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @_builtins.property
    @pulumi.getter
    def rulestack(self) -> pulumi.Output[_builtins.str]:
        """
        The rulestack.
        """
        return pulumi.get(self, "rulestack")

    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        """
        The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        """
        return pulumi.get(self, "scope")

    @_builtins.property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> pulumi.Output[_builtins.str]:
        """
        The update token.
        """
        return pulumi.get(self, "update_token")

