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

__all__ = ['CommitRulestackArgs', 'CommitRulestack']

@pulumi.input_type
class CommitRulestackArgs:
    def __init__(__self__, *,
                 rulestack: pulumi.Input[_builtins.str],
                 scope: Optional[pulumi.Input[_builtins.str]] = None,
                 state: Optional[pulumi.Input[_builtins.str]] = None):
        """
        The set of arguments for constructing a CommitRulestack resource.
        :param pulumi.Input[_builtins.str] rulestack: The rulestack.
        :param pulumi.Input[_builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        :param pulumi.Input[_builtins.str] state: The rulestack state. This can only be the default value. Defaults to `Running`.
        """
        pulumi.set(__self__, "rulestack", rulestack)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if state is not None:
            pulumi.set(__self__, "state", state)

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
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The rulestack state. This can only be the default value. Defaults to `Running`.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class _CommitRulestackState:
    def __init__(__self__, *,
                 commit_errors: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
                 commit_status: Optional[pulumi.Input[_builtins.str]] = None,
                 rulestack: Optional[pulumi.Input[_builtins.str]] = None,
                 scope: Optional[pulumi.Input[_builtins.str]] = None,
                 state: Optional[pulumi.Input[_builtins.str]] = None,
                 validation_errors: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
                 validation_status: Optional[pulumi.Input[_builtins.str]] = None):
        """
        Input properties used for looking up and filtering CommitRulestack resources.
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] commit_errors: Commit error messages.
        :param pulumi.Input[_builtins.str] commit_status: The commit status.
        :param pulumi.Input[_builtins.str] rulestack: The rulestack.
        :param pulumi.Input[_builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        :param pulumi.Input[_builtins.str] state: The rulestack state. This can only be the default value. Defaults to `Running`.
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] validation_errors: Validation error messages.
        :param pulumi.Input[_builtins.str] validation_status: The validation status.
        """
        if commit_errors is not None:
            pulumi.set(__self__, "commit_errors", commit_errors)
        if commit_status is not None:
            pulumi.set(__self__, "commit_status", commit_status)
        if rulestack is not None:
            pulumi.set(__self__, "rulestack", rulestack)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if validation_errors is not None:
            pulumi.set(__self__, "validation_errors", validation_errors)
        if validation_status is not None:
            pulumi.set(__self__, "validation_status", validation_status)

    @_builtins.property
    @pulumi.getter(name="commitErrors")
    def commit_errors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        """
        Commit error messages.
        """
        return pulumi.get(self, "commit_errors")

    @commit_errors.setter
    def commit_errors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]):
        pulumi.set(self, "commit_errors", value)

    @_builtins.property
    @pulumi.getter(name="commitStatus")
    def commit_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The commit status.
        """
        return pulumi.get(self, "commit_status")

    @commit_status.setter
    def commit_status(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "commit_status", value)

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
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The rulestack state. This can only be the default value. Defaults to `Running`.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "state", value)

    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        """
        Validation error messages.
        """
        return pulumi.get(self, "validation_errors")

    @validation_errors.setter
    def validation_errors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]):
        pulumi.set(self, "validation_errors", value)

    @_builtins.property
    @pulumi.getter(name="validationStatus")
    def validation_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        """
        The validation status.
        """
        return pulumi.get(self, "validation_status")

    @validation_status.setter
    def validation_status(self, value: Optional[pulumi.Input[_builtins.str]]):
        pulumi.set(self, "validation_status", value)


@pulumi.type_token("cloudngfwaws:index/commitRulestack:CommitRulestack")
class CommitRulestack(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 rulestack: Optional[pulumi.Input[_builtins.str]] = None,
                 scope: Optional[pulumi.Input[_builtins.str]] = None,
                 state: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        """
        Resource for committing the rulestack config.

        !> **NOTE:** This resource should be placed in a separate plan as the plan that configures the rulestack and its contents.  If you do not, you will have perpetual configuration drift and will need to run your plan twice so the commit is performed.  Placing instances of this resource with instances of NGFW resources (such as `Ngfw`) is fine.

        ## Admin Permission Type

        * `Rulestack` (for `scope="Local"`)
        * `Global Rulestack` (for `scope="Global"`)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudngfwaws as cloudngfwaws

        example = cloudngfwaws.CommitRulestack("example", rulestack="my-rulestack")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[_builtins.str] rulestack: The rulestack.
        :param pulumi.Input[_builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        :param pulumi.Input[_builtins.str] state: The rulestack state. This can only be the default value. Defaults to `Running`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CommitRulestackArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for committing the rulestack config.

        !> **NOTE:** This resource should be placed in a separate plan as the plan that configures the rulestack and its contents.  If you do not, you will have perpetual configuration drift and will need to run your plan twice so the commit is performed.  Placing instances of this resource with instances of NGFW resources (such as `Ngfw`) is fine.

        ## Admin Permission Type

        * `Rulestack` (for `scope="Local"`)
        * `Global Rulestack` (for `scope="Global"`)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudngfwaws as cloudngfwaws

        example = cloudngfwaws.CommitRulestack("example", rulestack="my-rulestack")
        ```

        :param str resource_name: The name of the resource.
        :param CommitRulestackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CommitRulestackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 rulestack: Optional[pulumi.Input[_builtins.str]] = None,
                 scope: Optional[pulumi.Input[_builtins.str]] = None,
                 state: Optional[pulumi.Input[_builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CommitRulestackArgs.__new__(CommitRulestackArgs)

            if rulestack is None and not opts.urn:
                raise TypeError("Missing required property 'rulestack'")
            __props__.__dict__["rulestack"] = rulestack
            __props__.__dict__["scope"] = scope
            __props__.__dict__["state"] = state
            __props__.__dict__["commit_errors"] = None
            __props__.__dict__["commit_status"] = None
            __props__.__dict__["validation_errors"] = None
            __props__.__dict__["validation_status"] = None
        super(CommitRulestack, __self__).__init__(
            'cloudngfwaws:index/commitRulestack:CommitRulestack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            commit_errors: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
            commit_status: Optional[pulumi.Input[_builtins.str]] = None,
            rulestack: Optional[pulumi.Input[_builtins.str]] = None,
            scope: Optional[pulumi.Input[_builtins.str]] = None,
            state: Optional[pulumi.Input[_builtins.str]] = None,
            validation_errors: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = None,
            validation_status: Optional[pulumi.Input[_builtins.str]] = None) -> 'CommitRulestack':
        """
        Get an existing CommitRulestack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] commit_errors: Commit error messages.
        :param pulumi.Input[_builtins.str] commit_status: The commit status.
        :param pulumi.Input[_builtins.str] rulestack: The rulestack.
        :param pulumi.Input[_builtins.str] scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        :param pulumi.Input[_builtins.str] state: The rulestack state. This can only be the default value. Defaults to `Running`.
        :param pulumi.Input[Sequence[pulumi.Input[_builtins.str]]] validation_errors: Validation error messages.
        :param pulumi.Input[_builtins.str] validation_status: The validation status.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CommitRulestackState.__new__(_CommitRulestackState)

        __props__.__dict__["commit_errors"] = commit_errors
        __props__.__dict__["commit_status"] = commit_status
        __props__.__dict__["rulestack"] = rulestack
        __props__.__dict__["scope"] = scope
        __props__.__dict__["state"] = state
        __props__.__dict__["validation_errors"] = validation_errors
        __props__.__dict__["validation_status"] = validation_status
        return CommitRulestack(resource_name, opts=opts, __props__=__props__)

    @_builtins.property
    @pulumi.getter(name="commitErrors")
    def commit_errors(self) -> pulumi.Output[Sequence[_builtins.str]]:
        """
        Commit error messages.
        """
        return pulumi.get(self, "commit_errors")

    @_builtins.property
    @pulumi.getter(name="commitStatus")
    def commit_status(self) -> pulumi.Output[_builtins.str]:
        """
        The commit status.
        """
        return pulumi.get(self, "commit_status")

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
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]:
        """
        The rulestack state. This can only be the default value. Defaults to `Running`.
        """
        return pulumi.get(self, "state")

    @_builtins.property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> pulumi.Output[Sequence[_builtins.str]]:
        """
        Validation error messages.
        """
        return pulumi.get(self, "validation_errors")

    @_builtins.property
    @pulumi.getter(name="validationStatus")
    def validation_status(self) -> pulumi.Output[_builtins.str]:
        """
        The validation status.
        """
        return pulumi.get(self, "validation_status")

