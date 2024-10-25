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
from . import outputs

__all__ = [
    'GetNgfwLogProfileResult',
    'AwaitableGetNgfwLogProfileResult',
    'get_ngfw_log_profile',
    'get_ngfw_log_profile_output',
]

@pulumi.output_type
class GetNgfwLogProfileResult:
    """
    A collection of values returned by getNgfwLogProfile.
    """
    def __init__(__self__, account_id=None, advanced_threat_log=None, cloud_watch_metric_namespace=None, cloudwatch_metric_fields=None, id=None, log_destinations=None, ngfw=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if advanced_threat_log and not isinstance(advanced_threat_log, bool):
            raise TypeError("Expected argument 'advanced_threat_log' to be a bool")
        pulumi.set(__self__, "advanced_threat_log", advanced_threat_log)
        if cloud_watch_metric_namespace and not isinstance(cloud_watch_metric_namespace, str):
            raise TypeError("Expected argument 'cloud_watch_metric_namespace' to be a str")
        pulumi.set(__self__, "cloud_watch_metric_namespace", cloud_watch_metric_namespace)
        if cloudwatch_metric_fields and not isinstance(cloudwatch_metric_fields, list):
            raise TypeError("Expected argument 'cloudwatch_metric_fields' to be a list")
        pulumi.set(__self__, "cloudwatch_metric_fields", cloudwatch_metric_fields)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if log_destinations and not isinstance(log_destinations, list):
            raise TypeError("Expected argument 'log_destinations' to be a list")
        pulumi.set(__self__, "log_destinations", log_destinations)
        if ngfw and not isinstance(ngfw, str):
            raise TypeError("Expected argument 'ngfw' to be a str")
        pulumi.set(__self__, "ngfw", ngfw)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The unique ID of the account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="advancedThreatLog")
    def advanced_threat_log(self) -> bool:
        """
        Enable advanced threat logging.
        """
        return pulumi.get(self, "advanced_threat_log")

    @property
    @pulumi.getter(name="cloudWatchMetricNamespace")
    def cloud_watch_metric_namespace(self) -> str:
        """
        The CloudWatch metric namespace.
        """
        return pulumi.get(self, "cloud_watch_metric_namespace")

    @property
    @pulumi.getter(name="cloudwatchMetricFields")
    def cloudwatch_metric_fields(self) -> Sequence[str]:
        """
        Cloudwatch metric fields.
        """
        return pulumi.get(self, "cloudwatch_metric_fields")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logDestinations")
    def log_destinations(self) -> Sequence['outputs.GetNgfwLogProfileLogDestinationResult']:
        """
        List of log destinations.
        """
        return pulumi.get(self, "log_destinations")

    @property
    @pulumi.getter
    def ngfw(self) -> str:
        """
        The name of the NGFW.
        """
        return pulumi.get(self, "ngfw")


class AwaitableGetNgfwLogProfileResult(GetNgfwLogProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNgfwLogProfileResult(
            account_id=self.account_id,
            advanced_threat_log=self.advanced_threat_log,
            cloud_watch_metric_namespace=self.cloud_watch_metric_namespace,
            cloudwatch_metric_fields=self.cloudwatch_metric_fields,
            id=self.id,
            log_destinations=self.log_destinations,
            ngfw=self.ngfw)


def get_ngfw_log_profile(account_id: Optional[str] = None,
                         ngfw: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNgfwLogProfileResult:
    """
    Data source for retrieving log profile information.

    ## Admin Permission Type

    * `Firewall`

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudngfwaws as cloudngfwaws

    example = cloudngfwaws.get_ngfw_log_profile(ngfw="example-instance",
        account_id="123456789")
    ```


    :param str account_id: The unique ID of the account.
    :param str ngfw: The name of the NGFW.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['ngfw'] = ngfw
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudngfwaws:index/getNgfwLogProfile:getNgfwLogProfile', __args__, opts=opts, typ=GetNgfwLogProfileResult).value

    return AwaitableGetNgfwLogProfileResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        advanced_threat_log=pulumi.get(__ret__, 'advanced_threat_log'),
        cloud_watch_metric_namespace=pulumi.get(__ret__, 'cloud_watch_metric_namespace'),
        cloudwatch_metric_fields=pulumi.get(__ret__, 'cloudwatch_metric_fields'),
        id=pulumi.get(__ret__, 'id'),
        log_destinations=pulumi.get(__ret__, 'log_destinations'),
        ngfw=pulumi.get(__ret__, 'ngfw'))
def get_ngfw_log_profile_output(account_id: Optional[pulumi.Input[str]] = None,
                                ngfw: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNgfwLogProfileResult]:
    """
    Data source for retrieving log profile information.

    ## Admin Permission Type

    * `Firewall`

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudngfwaws as cloudngfwaws

    example = cloudngfwaws.get_ngfw_log_profile(ngfw="example-instance",
        account_id="123456789")
    ```


    :param str account_id: The unique ID of the account.
    :param str ngfw: The name of the NGFW.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['ngfw'] = ngfw
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudngfwaws:index/getNgfwLogProfile:getNgfwLogProfile', __args__, opts=opts, typ=GetNgfwLogProfileResult)
    return __ret__.apply(lambda __response__: GetNgfwLogProfileResult(
        account_id=pulumi.get(__response__, 'account_id'),
        advanced_threat_log=pulumi.get(__response__, 'advanced_threat_log'),
        cloud_watch_metric_namespace=pulumi.get(__response__, 'cloud_watch_metric_namespace'),
        cloudwatch_metric_fields=pulumi.get(__response__, 'cloudwatch_metric_fields'),
        id=pulumi.get(__response__, 'id'),
        log_destinations=pulumi.get(__response__, 'log_destinations'),
        ngfw=pulumi.get(__response__, 'ngfw')))
