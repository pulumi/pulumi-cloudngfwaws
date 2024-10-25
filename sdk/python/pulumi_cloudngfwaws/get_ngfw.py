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
    'GetNgfwResult',
    'AwaitableGetNgfwResult',
    'get_ngfw',
    'get_ngfw_output',
]

@pulumi.output_type
class GetNgfwResult:
    """
    A collection of values returned by getNgfw.
    """
    def __init__(__self__, account_id=None, app_id_version=None, automatic_upgrade_app_id_version=None, description=None, endpoint_mode=None, endpoint_service_name=None, firewall_id=None, global_rulestack=None, id=None, link_id=None, link_status=None, multi_vpc=None, name=None, rulestack=None, statuses=None, subnet_mappings=None, tags=None, update_token=None, vpc_id=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if app_id_version and not isinstance(app_id_version, str):
            raise TypeError("Expected argument 'app_id_version' to be a str")
        pulumi.set(__self__, "app_id_version", app_id_version)
        if automatic_upgrade_app_id_version and not isinstance(automatic_upgrade_app_id_version, bool):
            raise TypeError("Expected argument 'automatic_upgrade_app_id_version' to be a bool")
        pulumi.set(__self__, "automatic_upgrade_app_id_version", automatic_upgrade_app_id_version)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if endpoint_mode and not isinstance(endpoint_mode, str):
            raise TypeError("Expected argument 'endpoint_mode' to be a str")
        pulumi.set(__self__, "endpoint_mode", endpoint_mode)
        if endpoint_service_name and not isinstance(endpoint_service_name, str):
            raise TypeError("Expected argument 'endpoint_service_name' to be a str")
        pulumi.set(__self__, "endpoint_service_name", endpoint_service_name)
        if firewall_id and not isinstance(firewall_id, str):
            raise TypeError("Expected argument 'firewall_id' to be a str")
        pulumi.set(__self__, "firewall_id", firewall_id)
        if global_rulestack and not isinstance(global_rulestack, str):
            raise TypeError("Expected argument 'global_rulestack' to be a str")
        pulumi.set(__self__, "global_rulestack", global_rulestack)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if link_id and not isinstance(link_id, str):
            raise TypeError("Expected argument 'link_id' to be a str")
        pulumi.set(__self__, "link_id", link_id)
        if link_status and not isinstance(link_status, str):
            raise TypeError("Expected argument 'link_status' to be a str")
        pulumi.set(__self__, "link_status", link_status)
        if multi_vpc and not isinstance(multi_vpc, bool):
            raise TypeError("Expected argument 'multi_vpc' to be a bool")
        pulumi.set(__self__, "multi_vpc", multi_vpc)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if rulestack and not isinstance(rulestack, str):
            raise TypeError("Expected argument 'rulestack' to be a str")
        pulumi.set(__self__, "rulestack", rulestack)
        if statuses and not isinstance(statuses, list):
            raise TypeError("Expected argument 'statuses' to be a list")
        pulumi.set(__self__, "statuses", statuses)
        if subnet_mappings and not isinstance(subnet_mappings, list):
            raise TypeError("Expected argument 'subnet_mappings' to be a list")
        pulumi.set(__self__, "subnet_mappings", subnet_mappings)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if update_token and not isinstance(update_token, str):
            raise TypeError("Expected argument 'update_token' to be a str")
        pulumi.set(__self__, "update_token", update_token)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[str]:
        """
        The account ID. This field is mandatory if using multiple accounts.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="appIdVersion")
    def app_id_version(self) -> str:
        """
        App-ID version number.
        """
        return pulumi.get(self, "app_id_version")

    @property
    @pulumi.getter(name="automaticUpgradeAppIdVersion")
    def automatic_upgrade_app_id_version(self) -> bool:
        """
        Automatic App-ID upgrade version number.
        """
        return pulumi.get(self, "automatic_upgrade_app_id_version")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endpointMode")
    def endpoint_mode(self) -> str:
        """
        Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
        """
        return pulumi.get(self, "endpoint_mode")

    @property
    @pulumi.getter(name="endpointServiceName")
    def endpoint_service_name(self) -> str:
        """
        The endpoint service name.
        """
        return pulumi.get(self, "endpoint_service_name")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> str:
        """
        The Id of the NGFW.
        """
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter(name="globalRulestack")
    def global_rulestack(self) -> str:
        """
        The global rulestack for this NGFW.
        """
        return pulumi.get(self, "global_rulestack")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="linkId")
    def link_id(self) -> str:
        """
        The link ID.
        """
        return pulumi.get(self, "link_id")

    @property
    @pulumi.getter(name="linkStatus")
    def link_status(self) -> str:
        """
        The link status.
        """
        return pulumi.get(self, "link_status")

    @property
    @pulumi.getter(name="multiVpc")
    def multi_vpc(self) -> bool:
        """
        Share NGFW with Multiple VPCs. This feature can be enabled only if the endpoint_mode is CustomerManaged.
        """
        return pulumi.get(self, "multi_vpc")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The NGFW name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rulestack(self) -> str:
        """
        The rulestack for this NGFW.
        """
        return pulumi.get(self, "rulestack")

    @property
    @pulumi.getter
    def statuses(self) -> Sequence['outputs.GetNgfwStatusResult']:
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(self) -> Sequence['outputs.GetNgfwSubnetMappingResult']:
        """
        Subnet mappings.
        """
        return pulumi.get(self, "subnet_mappings")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        The tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> str:
        """
        The update token.
        """
        return pulumi.get(self, "update_token")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        The vpc id.
        """
        return pulumi.get(self, "vpc_id")


class AwaitableGetNgfwResult(GetNgfwResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNgfwResult(
            account_id=self.account_id,
            app_id_version=self.app_id_version,
            automatic_upgrade_app_id_version=self.automatic_upgrade_app_id_version,
            description=self.description,
            endpoint_mode=self.endpoint_mode,
            endpoint_service_name=self.endpoint_service_name,
            firewall_id=self.firewall_id,
            global_rulestack=self.global_rulestack,
            id=self.id,
            link_id=self.link_id,
            link_status=self.link_status,
            multi_vpc=self.multi_vpc,
            name=self.name,
            rulestack=self.rulestack,
            statuses=self.statuses,
            subnet_mappings=self.subnet_mappings,
            tags=self.tags,
            update_token=self.update_token,
            vpc_id=self.vpc_id)


def get_ngfw(account_id: Optional[str] = None,
             name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNgfwResult:
    """
    Data source for retrieving NGFW information.

    ## Admin Permission Type

    * `Firewall`

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudngfwaws as cloudngfwaws

    example = cloudngfwaws.get_ngfw(name="example-instance")
    ```


    :param str account_id: The account ID. This field is mandatory if using multiple accounts.
    :param str name: The NGFW name.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudngfwaws:index/getNgfw:getNgfw', __args__, opts=opts, typ=GetNgfwResult).value

    return AwaitableGetNgfwResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        app_id_version=pulumi.get(__ret__, 'app_id_version'),
        automatic_upgrade_app_id_version=pulumi.get(__ret__, 'automatic_upgrade_app_id_version'),
        description=pulumi.get(__ret__, 'description'),
        endpoint_mode=pulumi.get(__ret__, 'endpoint_mode'),
        endpoint_service_name=pulumi.get(__ret__, 'endpoint_service_name'),
        firewall_id=pulumi.get(__ret__, 'firewall_id'),
        global_rulestack=pulumi.get(__ret__, 'global_rulestack'),
        id=pulumi.get(__ret__, 'id'),
        link_id=pulumi.get(__ret__, 'link_id'),
        link_status=pulumi.get(__ret__, 'link_status'),
        multi_vpc=pulumi.get(__ret__, 'multi_vpc'),
        name=pulumi.get(__ret__, 'name'),
        rulestack=pulumi.get(__ret__, 'rulestack'),
        statuses=pulumi.get(__ret__, 'statuses'),
        subnet_mappings=pulumi.get(__ret__, 'subnet_mappings'),
        tags=pulumi.get(__ret__, 'tags'),
        update_token=pulumi.get(__ret__, 'update_token'),
        vpc_id=pulumi.get(__ret__, 'vpc_id'))
def get_ngfw_output(account_id: Optional[pulumi.Input[Optional[str]]] = None,
                    name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNgfwResult]:
    """
    Data source for retrieving NGFW information.

    ## Admin Permission Type

    * `Firewall`

    ## Example Usage

    ```python
    import pulumi
    import pulumi_cloudngfwaws as cloudngfwaws

    example = cloudngfwaws.get_ngfw(name="example-instance")
    ```


    :param str account_id: The account ID. This field is mandatory if using multiple accounts.
    :param str name: The NGFW name.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudngfwaws:index/getNgfw:getNgfw', __args__, opts=opts, typ=GetNgfwResult)
    return __ret__.apply(lambda __response__: GetNgfwResult(
        account_id=pulumi.get(__response__, 'account_id'),
        app_id_version=pulumi.get(__response__, 'app_id_version'),
        automatic_upgrade_app_id_version=pulumi.get(__response__, 'automatic_upgrade_app_id_version'),
        description=pulumi.get(__response__, 'description'),
        endpoint_mode=pulumi.get(__response__, 'endpoint_mode'),
        endpoint_service_name=pulumi.get(__response__, 'endpoint_service_name'),
        firewall_id=pulumi.get(__response__, 'firewall_id'),
        global_rulestack=pulumi.get(__response__, 'global_rulestack'),
        id=pulumi.get(__response__, 'id'),
        link_id=pulumi.get(__response__, 'link_id'),
        link_status=pulumi.get(__response__, 'link_status'),
        multi_vpc=pulumi.get(__response__, 'multi_vpc'),
        name=pulumi.get(__response__, 'name'),
        rulestack=pulumi.get(__response__, 'rulestack'),
        statuses=pulumi.get(__response__, 'statuses'),
        subnet_mappings=pulumi.get(__response__, 'subnet_mappings'),
        tags=pulumi.get(__response__, 'tags'),
        update_token=pulumi.get(__response__, 'update_token'),
        vpc_id=pulumi.get(__response__, 'vpc_id')))
