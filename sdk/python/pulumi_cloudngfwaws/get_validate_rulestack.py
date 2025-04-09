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

__all__ = [
    'GetValidateRulestackResult',
    'AwaitableGetValidateRulestackResult',
    'get_validate_rulestack',
    'get_validate_rulestack_output',
]

@pulumi.output_type
class GetValidateRulestackResult:
    """
    A collection of values returned by getValidateRulestack.
    """
    def __init__(__self__, commit_errors=None, commit_status=None, id=None, rulestack=None, scope=None, state=None, validation_errors=None, validation_status=None):
        if commit_errors and not isinstance(commit_errors, list):
            raise TypeError("Expected argument 'commit_errors' to be a list")
        pulumi.set(__self__, "commit_errors", commit_errors)
        if commit_status and not isinstance(commit_status, str):
            raise TypeError("Expected argument 'commit_status' to be a str")
        pulumi.set(__self__, "commit_status", commit_status)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if rulestack and not isinstance(rulestack, str):
            raise TypeError("Expected argument 'rulestack' to be a str")
        pulumi.set(__self__, "rulestack", rulestack)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if validation_errors and not isinstance(validation_errors, list):
            raise TypeError("Expected argument 'validation_errors' to be a list")
        pulumi.set(__self__, "validation_errors", validation_errors)
        if validation_status and not isinstance(validation_status, str):
            raise TypeError("Expected argument 'validation_status' to be a str")
        pulumi.set(__self__, "validation_status", validation_status)

    @property
    @pulumi.getter(name="commitErrors")
    def commit_errors(self) -> Sequence[builtins.str]:
        """
        Commit error messages.
        """
        return pulumi.get(self, "commit_errors")

    @property
    @pulumi.getter(name="commitStatus")
    def commit_status(self) -> builtins.str:
        """
        The commit status.
        """
        return pulumi.get(self, "commit_status")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def rulestack(self) -> builtins.str:
        """
        The rulestack.
        """
        return pulumi.get(self, "rulestack")

    @property
    @pulumi.getter
    def scope(self) -> Optional[builtins.str]:
        """
        The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def state(self) -> builtins.str:
        """
        The rulestack state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="validationErrors")
    def validation_errors(self) -> Sequence[builtins.str]:
        """
        Validation error messages.
        """
        return pulumi.get(self, "validation_errors")

    @property
    @pulumi.getter(name="validationStatus")
    def validation_status(self) -> builtins.str:
        """
        The validation status.
        """
        return pulumi.get(self, "validation_status")


class AwaitableGetValidateRulestackResult(GetValidateRulestackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetValidateRulestackResult(
            commit_errors=self.commit_errors,
            commit_status=self.commit_status,
            id=self.id,
            rulestack=self.rulestack,
            scope=self.scope,
            state=self.state,
            validation_errors=self.validation_errors,
            validation_status=self.validation_status)


def get_validate_rulestack(rulestack: Optional[builtins.str] = None,
                           scope: Optional[builtins.str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetValidateRulestackResult:
    """
    Data source to validate the rulestack config.

    ## Admin Permission Type

    * `Rulestack` (for `scope="Local"`)
    * `Global Rulestack` (for `scope="Global"`)


    :param builtins.str rulestack: The rulestack.
    :param builtins.str scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
    """
    __args__ = dict()
    __args__['rulestack'] = rulestack
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudngfwaws:index/getValidateRulestack:getValidateRulestack', __args__, opts=opts, typ=GetValidateRulestackResult).value

    return AwaitableGetValidateRulestackResult(
        commit_errors=pulumi.get(__ret__, 'commit_errors'),
        commit_status=pulumi.get(__ret__, 'commit_status'),
        id=pulumi.get(__ret__, 'id'),
        rulestack=pulumi.get(__ret__, 'rulestack'),
        scope=pulumi.get(__ret__, 'scope'),
        state=pulumi.get(__ret__, 'state'),
        validation_errors=pulumi.get(__ret__, 'validation_errors'),
        validation_status=pulumi.get(__ret__, 'validation_status'))
def get_validate_rulestack_output(rulestack: Optional[pulumi.Input[builtins.str]] = None,
                                  scope: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                                  opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetValidateRulestackResult]:
    """
    Data source to validate the rulestack config.

    ## Admin Permission Type

    * `Rulestack` (for `scope="Local"`)
    * `Global Rulestack` (for `scope="Global"`)


    :param builtins.str rulestack: The rulestack.
    :param builtins.str scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
    """
    __args__ = dict()
    __args__['rulestack'] = rulestack
    __args__['scope'] = scope
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudngfwaws:index/getValidateRulestack:getValidateRulestack', __args__, opts=opts, typ=GetValidateRulestackResult)
    return __ret__.apply(lambda __response__: GetValidateRulestackResult(
        commit_errors=pulumi.get(__response__, 'commit_errors'),
        commit_status=pulumi.get(__response__, 'commit_status'),
        id=pulumi.get(__response__, 'id'),
        rulestack=pulumi.get(__response__, 'rulestack'),
        scope=pulumi.get(__response__, 'scope'),
        state=pulumi.get(__response__, 'state'),
        validation_errors=pulumi.get(__response__, 'validation_errors'),
        validation_status=pulumi.get(__response__, 'validation_status')))
