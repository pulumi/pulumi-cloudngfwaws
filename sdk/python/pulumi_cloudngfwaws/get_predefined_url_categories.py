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
    'GetPredefinedUrlCategoriesResult',
    'AwaitableGetPredefinedUrlCategoriesResult',
    'get_predefined_url_categories',
    'get_predefined_url_categories_output',
]

@pulumi.output_type
class GetPredefinedUrlCategoriesResult:
    """
    A collection of values returned by getPredefinedUrlCategories.
    """
    def __init__(__self__, categories=None, id=None, max_results=None, next_token=None, token=None):
        if categories and not isinstance(categories, list):
            raise TypeError("Expected argument 'categories' to be a list")
        pulumi.set(__self__, "categories", categories)
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

    @property
    @pulumi.getter
    def categories(self) -> Sequence[str]:
        """
        List of predefined URL categories.
        """
        return pulumi.get(self, "categories")

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
        Next pagination token.
        """
        return pulumi.get(self, "next_token")

    @property
    @pulumi.getter
    def token(self) -> Optional[str]:
        """
        Pagination token.
        """
        return pulumi.get(self, "token")


class AwaitableGetPredefinedUrlCategoriesResult(GetPredefinedUrlCategoriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPredefinedUrlCategoriesResult(
            categories=self.categories,
            id=self.id,
            max_results=self.max_results,
            next_token=self.next_token,
            token=self.token)


def get_predefined_url_categories(max_results: Optional[int] = None,
                                  token: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPredefinedUrlCategoriesResult:
    """
    Data source for retrieving the predefined URL categories.

    ## Admin Permission Type

    * `Rulestack` (for `scope="Local"`)
    * `Global Rulestack` (for `scope="Global"`)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudngfwaws as cloudngfwaws

    example = cloudngfwaws.get_predefined_url_categories()
    ```


    :param int max_results: Max results. Defaults to `100`.
    :param str token: Pagination token.
    """
    __args__ = dict()
    __args__['maxResults'] = max_results
    __args__['token'] = token
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudngfwaws:index/getPredefinedUrlCategories:getPredefinedUrlCategories', __args__, opts=opts, typ=GetPredefinedUrlCategoriesResult).value

    return AwaitableGetPredefinedUrlCategoriesResult(
        categories=pulumi.get(__ret__, 'categories'),
        id=pulumi.get(__ret__, 'id'),
        max_results=pulumi.get(__ret__, 'max_results'),
        next_token=pulumi.get(__ret__, 'next_token'),
        token=pulumi.get(__ret__, 'token'))
def get_predefined_url_categories_output(max_results: Optional[pulumi.Input[Optional[int]]] = None,
                                         token: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPredefinedUrlCategoriesResult]:
    """
    Data source for retrieving the predefined URL categories.

    ## Admin Permission Type

    * `Rulestack` (for `scope="Local"`)
    * `Global Rulestack` (for `scope="Global"`)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudngfwaws as cloudngfwaws

    example = cloudngfwaws.get_predefined_url_categories()
    ```


    :param int max_results: Max results. Defaults to `100`.
    :param str token: Pagination token.
    """
    __args__ = dict()
    __args__['maxResults'] = max_results
    __args__['token'] = token
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudngfwaws:index/getPredefinedUrlCategories:getPredefinedUrlCategories', __args__, opts=opts, typ=GetPredefinedUrlCategoriesResult)
    return __ret__.apply(lambda __response__: GetPredefinedUrlCategoriesResult(
        categories=pulumi.get(__response__, 'categories'),
        id=pulumi.get(__response__, 'id'),
        max_results=pulumi.get(__response__, 'max_results'),
        next_token=pulumi.get(__response__, 'next_token'),
        token=pulumi.get(__response__, 'token')))
