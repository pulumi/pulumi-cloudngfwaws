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
    'GetAppIdVersionResult',
    'AwaitableGetAppIdVersionResult',
    'get_app_id_version',
    'get_app_id_version_output',
]

@pulumi.output_type
class GetAppIdVersionResult:
    """
    A collection of values returned by getAppIdVersion.
    """
    def __init__(__self__, applications=None, id=None, max_results=None, next_token=None, token=None, version=None):
        if applications and not isinstance(applications, list):
            raise TypeError("Expected argument 'applications' to be a list")
        pulumi.set(__self__, "applications", applications)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_results and not isinstance(max_results, int):
            raise TypeError("Expected argument 'max_results' to be a int")
        pulumi.set(__self__, "max_results", max_results)
        if next_token and not isinstance(next_token, str):
            raise TypeError("Expected argument 'next_token' to be a str")
        pulumi.set(__self__, "next_token", next_token)
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def applications(self) -> Sequence[str]:
        """
        List of applications.
        """
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxResults")
    def max_results(self) -> Optional[int]:
        """
        Max results. Defaults to `100`.
        """
        return pulumi.get(self, "max_results")

    @property
    @pulumi.getter(name="nextToken")
    def next_token(self) -> str:
        """
        Token for the next page of results.
        """
        return pulumi.get(self, "next_token")

    @property
    @pulumi.getter
    def token(self) -> Optional[str]:
        """
        Pagination token.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The AppId version.
        """
        return pulumi.get(self, "version")


class AwaitableGetAppIdVersionResult(GetAppIdVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppIdVersionResult(
            applications=self.applications,
            id=self.id,
            max_results=self.max_results,
            next_token=self.next_token,
            token=self.token,
            version=self.version)


def get_app_id_version(max_results: Optional[int] = None,
                       token: Optional[str] = None,
                       version: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppIdVersionResult:
    """
    Data source to retrieve information on a given AppId version.

    ## Admin Permission Type

    * `Rulestack`

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudngfwaws as cloudngfwaws

    example = cloudngfwaws.get_app_id_version(version="123-456")
    ```


    :param int max_results: Max results. Defaults to `100`.
    :param str token: Pagination token.
    :param str version: The AppId version.
    """
    __args__ = dict()
    __args__['maxResults'] = max_results
    __args__['token'] = token
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudngfwaws:index/getAppIdVersion:getAppIdVersion', __args__, opts=opts, typ=GetAppIdVersionResult).value

    return AwaitableGetAppIdVersionResult(
        applications=pulumi.get(__ret__, 'applications'),
        id=pulumi.get(__ret__, 'id'),
        max_results=pulumi.get(__ret__, 'max_results'),
        next_token=pulumi.get(__ret__, 'next_token'),
        token=pulumi.get(__ret__, 'token'),
        version=pulumi.get(__ret__, 'version'))
def get_app_id_version_output(max_results: Optional[pulumi.Input[Optional[int]]] = None,
                              token: Optional[pulumi.Input[Optional[str]]] = None,
                              version: Optional[pulumi.Input[str]] = None,
                              opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetAppIdVersionResult]:
    """
    Data source to retrieve information on a given AppId version.

    ## Admin Permission Type

    * `Rulestack`

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudngfwaws as cloudngfwaws

    example = cloudngfwaws.get_app_id_version(version="123-456")
    ```


    :param int max_results: Max results. Defaults to `100`.
    :param str token: Pagination token.
    :param str version: The AppId version.
    """
    __args__ = dict()
    __args__['maxResults'] = max_results
    __args__['token'] = token
    __args__['version'] = version
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudngfwaws:index/getAppIdVersion:getAppIdVersion', __args__, opts=opts, typ=GetAppIdVersionResult)
    return __ret__.apply(lambda __response__: GetAppIdVersionResult(
        applications=pulumi.get(__response__, 'applications'),
        id=pulumi.get(__response__, 'id'),
        max_results=pulumi.get(__response__, 'max_results'),
        next_token=pulumi.get(__response__, 'next_token'),
        token=pulumi.get(__response__, 'token'),
        version=pulumi.get(__response__, 'version')))
