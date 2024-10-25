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

__all__ = [
    'GetCertificateResult',
    'AwaitableGetCertificateResult',
    'get_certificate',
    'get_certificate_output',
]

@pulumi.output_type
class GetCertificateResult:
    """
    A collection of values returned by getCertificate.
    """
    def __init__(__self__, audit_comment=None, config_type=None, description=None, id=None, name=None, rulestack=None, scope=None, self_signed=None, signer_arn=None, update_token=None):
        if audit_comment and not isinstance(audit_comment, str):
            raise TypeError("Expected argument 'audit_comment' to be a str")
        pulumi.set(__self__, "audit_comment", audit_comment)
        if config_type and not isinstance(config_type, str):
            raise TypeError("Expected argument 'config_type' to be a str")
        pulumi.set(__self__, "config_type", config_type)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if rulestack and not isinstance(rulestack, str):
            raise TypeError("Expected argument 'rulestack' to be a str")
        pulumi.set(__self__, "rulestack", rulestack)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if self_signed and not isinstance(self_signed, bool):
            raise TypeError("Expected argument 'self_signed' to be a bool")
        pulumi.set(__self__, "self_signed", self_signed)
        if signer_arn and not isinstance(signer_arn, str):
            raise TypeError("Expected argument 'signer_arn' to be a str")
        pulumi.set(__self__, "signer_arn", signer_arn)
        if update_token and not isinstance(update_token, str):
            raise TypeError("Expected argument 'update_token' to be a str")
        pulumi.set(__self__, "update_token", update_token)

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> str:
        """
        The audit comment.
        """
        return pulumi.get(self, "audit_comment")

    @property
    @pulumi.getter(name="configType")
    def config_type(self) -> Optional[str]:
        """
        Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
        """
        return pulumi.get(self, "config_type")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rulestack(self) -> str:
        """
        The rulestack.
        """
        return pulumi.get(self, "rulestack")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        """
        The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="selfSigned")
    def self_signed(self) -> bool:
        """
        Set to true if certificate is self-signed.
        """
        return pulumi.get(self, "self_signed")

    @property
    @pulumi.getter(name="signerArn")
    def signer_arn(self) -> str:
        """
        The certificate signer ARN.
        """
        return pulumi.get(self, "signer_arn")

    @property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> str:
        """
        The update token.
        """
        return pulumi.get(self, "update_token")


class AwaitableGetCertificateResult(GetCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateResult(
            audit_comment=self.audit_comment,
            config_type=self.config_type,
            description=self.description,
            id=self.id,
            name=self.name,
            rulestack=self.rulestack,
            scope=self.scope,
            self_signed=self.self_signed,
            signer_arn=self.signer_arn,
            update_token=self.update_token)


def get_certificate(config_type: Optional[str] = None,
                    name: Optional[str] = None,
                    rulestack: Optional[str] = None,
                    scope: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateResult:
    """
    Data source for retrieving certificate information.

    ## Admin Permission Type

    * `Rulestack` (for `scope="Local"`)
    * `Global Rulestack` (for `scope="Global"`)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudngfwaws as cloudngfwaws

    r = cloudngfwaws.Rulestack("r",
        name="my-rulestack",
        scope="Local",
        account_id="12345",
        description="Made by Pulumi",
        profile_config={
            "anti_spyware": "BestPractice",
        })
    example = cloudngfwaws.get_certificate_output(rulestack=r.name,
        name="foobar")
    ```


    :param str config_type: Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
    :param str name: The name.
    :param str rulestack: The rulestack.
    :param str scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
    """
    __args__ = dict()
    __args__['configType'] = config_type
    __args__['name'] = name
    __args__['rulestack'] = rulestack
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudngfwaws:index/getCertificate:getCertificate', __args__, opts=opts, typ=GetCertificateResult).value

    return AwaitableGetCertificateResult(
        audit_comment=pulumi.get(__ret__, 'audit_comment'),
        config_type=pulumi.get(__ret__, 'config_type'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        rulestack=pulumi.get(__ret__, 'rulestack'),
        scope=pulumi.get(__ret__, 'scope'),
        self_signed=pulumi.get(__ret__, 'self_signed'),
        signer_arn=pulumi.get(__ret__, 'signer_arn'),
        update_token=pulumi.get(__ret__, 'update_token'))
def get_certificate_output(config_type: Optional[pulumi.Input[Optional[str]]] = None,
                           name: Optional[pulumi.Input[str]] = None,
                           rulestack: Optional[pulumi.Input[str]] = None,
                           scope: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCertificateResult]:
    """
    Data source for retrieving certificate information.

    ## Admin Permission Type

    * `Rulestack` (for `scope="Local"`)
    * `Global Rulestack` (for `scope="Global"`)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudngfwaws as cloudngfwaws

    r = cloudngfwaws.Rulestack("r",
        name="my-rulestack",
        scope="Local",
        account_id="12345",
        description="Made by Pulumi",
        profile_config={
            "anti_spyware": "BestPractice",
        })
    example = cloudngfwaws.get_certificate_output(rulestack=r.name,
        name="foobar")
    ```


    :param str config_type: Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
    :param str name: The name.
    :param str rulestack: The rulestack.
    :param str scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
    """
    __args__ = dict()
    __args__['configType'] = config_type
    __args__['name'] = name
    __args__['rulestack'] = rulestack
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudngfwaws:index/getCertificate:getCertificate', __args__, opts=opts, typ=GetCertificateResult)
    return __ret__.apply(lambda __response__: GetCertificateResult(
        audit_comment=pulumi.get(__response__, 'audit_comment'),
        config_type=pulumi.get(__response__, 'config_type'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        rulestack=pulumi.get(__response__, 'rulestack'),
        scope=pulumi.get(__response__, 'scope'),
        self_signed=pulumi.get(__response__, 'self_signed'),
        signer_arn=pulumi.get(__response__, 'signer_arn'),
        update_token=pulumi.get(__response__, 'update_token')))
