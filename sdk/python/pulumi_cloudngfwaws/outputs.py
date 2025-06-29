# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
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

__all__ = [
    'NgfwLogProfileLogDestination',
    'NgfwStatus',
    'NgfwStatusAttachment',
    'NgfwSubnetMapping',
    'RulestackProfileConfig',
    'SecurityRuleCategory',
    'SecurityRuleDestination',
    'SecurityRuleSource',
    'GetAccountsAccountDetailResult',
    'GetNgfwLogProfileLogDestinationResult',
    'GetNgfwStatusResult',
    'GetNgfwStatusAttachmentResult',
    'GetNgfwSubnetMappingResult',
    'GetNgfwsInstanceResult',
    'GetRulestackProfileConfigResult',
    'GetSecurityRuleCategoryResult',
    'GetSecurityRuleDestinationResult',
    'GetSecurityRuleSourceResult',
]

@pulumi.output_type
class NgfwLogProfileLogDestination(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "destinationType":
            suggest = "destination_type"
        elif key == "logType":
            suggest = "log_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NgfwLogProfileLogDestination. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NgfwLogProfileLogDestination.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NgfwLogProfileLogDestination.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 destination: Optional[builtins.str] = None,
                 destination_type: Optional[builtins.str] = None,
                 log_type: Optional[builtins.str] = None):
        """
        :param builtins.str destination: The log destination details.
        :param builtins.str destination_type: The log destination type. Valid values are `S3`, `CloudWatchLogs`, or `KinesisDataFirehose`.
        :param builtins.str log_type: The type of logs. Valid values are `TRAFFIC`, `THREAT`, or `DECRYPTION`.
        """
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if destination_type is not None:
            pulumi.set(__self__, "destination_type", destination_type)
        if log_type is not None:
            pulumi.set(__self__, "log_type", log_type)

    @property
    @pulumi.getter
    def destination(self) -> Optional[builtins.str]:
        """
        The log destination details.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> Optional[builtins.str]:
        """
        The log destination type. Valid values are `S3`, `CloudWatchLogs`, or `KinesisDataFirehose`.
        """
        return pulumi.get(self, "destination_type")

    @property
    @pulumi.getter(name="logType")
    def log_type(self) -> Optional[builtins.str]:
        """
        The type of logs. Valid values are `TRAFFIC`, `THREAT`, or `DECRYPTION`.
        """
        return pulumi.get(self, "log_type")


@pulumi.output_type
class NgfwStatus(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "failureReason":
            suggest = "failure_reason"
        elif key == "firewallStatus":
            suggest = "firewall_status"
        elif key == "rulestackStatus":
            suggest = "rulestack_status"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NgfwStatus. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NgfwStatus.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NgfwStatus.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 attachments: Optional[Sequence['outputs.NgfwStatusAttachment']] = None,
                 failure_reason: Optional[builtins.str] = None,
                 firewall_status: Optional[builtins.str] = None,
                 rulestack_status: Optional[builtins.str] = None):
        """
        :param Sequence['NgfwStatusAttachmentArgs'] attachments: The firewall attachments.
        :param builtins.str failure_reason: The firewall failure reason.
        :param builtins.str firewall_status: The firewall status.
        :param builtins.str rulestack_status: The rulestack status.
        """
        if attachments is not None:
            pulumi.set(__self__, "attachments", attachments)
        if failure_reason is not None:
            pulumi.set(__self__, "failure_reason", failure_reason)
        if firewall_status is not None:
            pulumi.set(__self__, "firewall_status", firewall_status)
        if rulestack_status is not None:
            pulumi.set(__self__, "rulestack_status", rulestack_status)

    @property
    @pulumi.getter
    def attachments(self) -> Optional[Sequence['outputs.NgfwStatusAttachment']]:
        """
        The firewall attachments.
        """
        return pulumi.get(self, "attachments")

    @property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[builtins.str]:
        """
        The firewall failure reason.
        """
        return pulumi.get(self, "failure_reason")

    @property
    @pulumi.getter(name="firewallStatus")
    def firewall_status(self) -> Optional[builtins.str]:
        """
        The firewall status.
        """
        return pulumi.get(self, "firewall_status")

    @property
    @pulumi.getter(name="rulestackStatus")
    def rulestack_status(self) -> Optional[builtins.str]:
        """
        The rulestack status.
        """
        return pulumi.get(self, "rulestack_status")


@pulumi.output_type
class NgfwStatusAttachment(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endpointId":
            suggest = "endpoint_id"
        elif key == "rejectedReason":
            suggest = "rejected_reason"
        elif key == "subnetId":
            suggest = "subnet_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NgfwStatusAttachment. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NgfwStatusAttachment.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NgfwStatusAttachment.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 endpoint_id: Optional[builtins.str] = None,
                 rejected_reason: Optional[builtins.str] = None,
                 status: Optional[builtins.str] = None,
                 subnet_id: Optional[builtins.str] = None):
        """
        :param builtins.str endpoint_id: The endpoint id.
        :param builtins.str rejected_reason: The reject reason.
        :param builtins.str status: The attachment status.
        :param builtins.str subnet_id: The subnet id.
        """
        if endpoint_id is not None:
            pulumi.set(__self__, "endpoint_id", endpoint_id)
        if rejected_reason is not None:
            pulumi.set(__self__, "rejected_reason", rejected_reason)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[builtins.str]:
        """
        The endpoint id.
        """
        return pulumi.get(self, "endpoint_id")

    @property
    @pulumi.getter(name="rejectedReason")
    def rejected_reason(self) -> Optional[builtins.str]:
        """
        The reject reason.
        """
        return pulumi.get(self, "rejected_reason")

    @property
    @pulumi.getter
    def status(self) -> Optional[builtins.str]:
        """
        The attachment status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[builtins.str]:
        """
        The subnet id.
        """
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class NgfwSubnetMapping(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "availabilityZone":
            suggest = "availability_zone"
        elif key == "availabilityZoneId":
            suggest = "availability_zone_id"
        elif key == "subnetId":
            suggest = "subnet_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NgfwSubnetMapping. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NgfwSubnetMapping.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NgfwSubnetMapping.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 availability_zone: Optional[builtins.str] = None,
                 availability_zone_id: Optional[builtins.str] = None,
                 subnet_id: Optional[builtins.str] = None):
        """
        :param builtins.str availability_zone: The availability zone, for when the endpoint mode is customer managed.
        :param builtins.str availability_zone_id: The availability zone ID, for when the endpoint mode is customer managed.
        :param builtins.str subnet_id: The subnet id, for when the endpoint mode is service managed.
        """
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if availability_zone_id is not None:
            pulumi.set(__self__, "availability_zone_id", availability_zone_id)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[builtins.str]:
        """
        The availability zone, for when the endpoint mode is customer managed.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[builtins.str]:
        """
        The availability zone ID, for when the endpoint mode is customer managed.
        """
        return pulumi.get(self, "availability_zone_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[builtins.str]:
        """
        The subnet id, for when the endpoint mode is service managed.
        """
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class RulestackProfileConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "antiSpyware":
            suggest = "anti_spyware"
        elif key == "antiVirus":
            suggest = "anti_virus"
        elif key == "fileBlocking":
            suggest = "file_blocking"
        elif key == "outboundTrustCertificate":
            suggest = "outbound_trust_certificate"
        elif key == "outboundUntrustCertificate":
            suggest = "outbound_untrust_certificate"
        elif key == "urlFiltering":
            suggest = "url_filtering"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RulestackProfileConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RulestackProfileConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RulestackProfileConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 anti_spyware: Optional[builtins.str] = None,
                 anti_virus: Optional[builtins.str] = None,
                 file_blocking: Optional[builtins.str] = None,
                 outbound_trust_certificate: Optional[builtins.str] = None,
                 outbound_untrust_certificate: Optional[builtins.str] = None,
                 url_filtering: Optional[builtins.str] = None,
                 vulnerability: Optional[builtins.str] = None):
        """
        :param builtins.str anti_spyware: Anti-spyware profile setting. Defaults to `BestPractice`.
        :param builtins.str anti_virus: Anti-virus profile setting. Defaults to `BestPractice`.
        :param builtins.str file_blocking: File blocking profile setting. Defaults to `BestPractice`.
        :param builtins.str outbound_trust_certificate: Outbound trust certificate.
        :param builtins.str outbound_untrust_certificate: Outbound untrust certificate.
        :param builtins.str url_filtering: URL filtering profile setting. Defaults to `None`.
        :param builtins.str vulnerability: Vulnerability profile setting. Defaults to `BestPractice`.
        """
        if anti_spyware is not None:
            pulumi.set(__self__, "anti_spyware", anti_spyware)
        if anti_virus is not None:
            pulumi.set(__self__, "anti_virus", anti_virus)
        if file_blocking is not None:
            pulumi.set(__self__, "file_blocking", file_blocking)
        if outbound_trust_certificate is not None:
            pulumi.set(__self__, "outbound_trust_certificate", outbound_trust_certificate)
        if outbound_untrust_certificate is not None:
            pulumi.set(__self__, "outbound_untrust_certificate", outbound_untrust_certificate)
        if url_filtering is not None:
            pulumi.set(__self__, "url_filtering", url_filtering)
        if vulnerability is not None:
            pulumi.set(__self__, "vulnerability", vulnerability)

    @property
    @pulumi.getter(name="antiSpyware")
    def anti_spyware(self) -> Optional[builtins.str]:
        """
        Anti-spyware profile setting. Defaults to `BestPractice`.
        """
        return pulumi.get(self, "anti_spyware")

    @property
    @pulumi.getter(name="antiVirus")
    def anti_virus(self) -> Optional[builtins.str]:
        """
        Anti-virus profile setting. Defaults to `BestPractice`.
        """
        return pulumi.get(self, "anti_virus")

    @property
    @pulumi.getter(name="fileBlocking")
    def file_blocking(self) -> Optional[builtins.str]:
        """
        File blocking profile setting. Defaults to `BestPractice`.
        """
        return pulumi.get(self, "file_blocking")

    @property
    @pulumi.getter(name="outboundTrustCertificate")
    def outbound_trust_certificate(self) -> Optional[builtins.str]:
        """
        Outbound trust certificate.
        """
        return pulumi.get(self, "outbound_trust_certificate")

    @property
    @pulumi.getter(name="outboundUntrustCertificate")
    def outbound_untrust_certificate(self) -> Optional[builtins.str]:
        """
        Outbound untrust certificate.
        """
        return pulumi.get(self, "outbound_untrust_certificate")

    @property
    @pulumi.getter(name="urlFiltering")
    def url_filtering(self) -> Optional[builtins.str]:
        """
        URL filtering profile setting. Defaults to `None`.
        """
        return pulumi.get(self, "url_filtering")

    @property
    @pulumi.getter
    def vulnerability(self) -> Optional[builtins.str]:
        """
        Vulnerability profile setting. Defaults to `BestPractice`.
        """
        return pulumi.get(self, "vulnerability")


@pulumi.output_type
class SecurityRuleCategory(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "urlCategoryNames":
            suggest = "url_category_names"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SecurityRuleCategory. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SecurityRuleCategory.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SecurityRuleCategory.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 feeds: Optional[Sequence[builtins.str]] = None,
                 url_category_names: Optional[Sequence[builtins.str]] = None):
        """
        :param Sequence[builtins.str] feeds: List of feeds.
        :param Sequence[builtins.str] url_category_names: List of URL category names.
        """
        if feeds is not None:
            pulumi.set(__self__, "feeds", feeds)
        if url_category_names is not None:
            pulumi.set(__self__, "url_category_names", url_category_names)

    @property
    @pulumi.getter
    def feeds(self) -> Optional[Sequence[builtins.str]]:
        """
        List of feeds.
        """
        return pulumi.get(self, "feeds")

    @property
    @pulumi.getter(name="urlCategoryNames")
    def url_category_names(self) -> Optional[Sequence[builtins.str]]:
        """
        List of URL category names.
        """
        return pulumi.get(self, "url_category_names")


@pulumi.output_type
class SecurityRuleDestination(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fqdnLists":
            suggest = "fqdn_lists"
        elif key == "prefixLists":
            suggest = "prefix_lists"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SecurityRuleDestination. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SecurityRuleDestination.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SecurityRuleDestination.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cidrs: Optional[Sequence[builtins.str]] = None,
                 countries: Optional[Sequence[builtins.str]] = None,
                 feeds: Optional[Sequence[builtins.str]] = None,
                 fqdn_lists: Optional[Sequence[builtins.str]] = None,
                 prefix_lists: Optional[Sequence[builtins.str]] = None):
        """
        :param Sequence[builtins.str] cidrs: List of CIDRs.
        :param Sequence[builtins.str] countries: List of countries.
        :param Sequence[builtins.str] feeds: List of feeds.
        :param Sequence[builtins.str] fqdn_lists: List of FQDN lists.
        :param Sequence[builtins.str] prefix_lists: List of prefix list.
        """
        if cidrs is not None:
            pulumi.set(__self__, "cidrs", cidrs)
        if countries is not None:
            pulumi.set(__self__, "countries", countries)
        if feeds is not None:
            pulumi.set(__self__, "feeds", feeds)
        if fqdn_lists is not None:
            pulumi.set(__self__, "fqdn_lists", fqdn_lists)
        if prefix_lists is not None:
            pulumi.set(__self__, "prefix_lists", prefix_lists)

    @property
    @pulumi.getter
    def cidrs(self) -> Optional[Sequence[builtins.str]]:
        """
        List of CIDRs.
        """
        return pulumi.get(self, "cidrs")

    @property
    @pulumi.getter
    def countries(self) -> Optional[Sequence[builtins.str]]:
        """
        List of countries.
        """
        return pulumi.get(self, "countries")

    @property
    @pulumi.getter
    def feeds(self) -> Optional[Sequence[builtins.str]]:
        """
        List of feeds.
        """
        return pulumi.get(self, "feeds")

    @property
    @pulumi.getter(name="fqdnLists")
    def fqdn_lists(self) -> Optional[Sequence[builtins.str]]:
        """
        List of FQDN lists.
        """
        return pulumi.get(self, "fqdn_lists")

    @property
    @pulumi.getter(name="prefixLists")
    def prefix_lists(self) -> Optional[Sequence[builtins.str]]:
        """
        List of prefix list.
        """
        return pulumi.get(self, "prefix_lists")


@pulumi.output_type
class SecurityRuleSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "prefixLists":
            suggest = "prefix_lists"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SecurityRuleSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SecurityRuleSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SecurityRuleSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cidrs: Optional[Sequence[builtins.str]] = None,
                 countries: Optional[Sequence[builtins.str]] = None,
                 feeds: Optional[Sequence[builtins.str]] = None,
                 prefix_lists: Optional[Sequence[builtins.str]] = None):
        """
        :param Sequence[builtins.str] cidrs: List of CIDRs.
        :param Sequence[builtins.str] countries: List of countries.
        :param Sequence[builtins.str] feeds: List of feeds.
        :param Sequence[builtins.str] prefix_lists: List of prefix list.
        """
        if cidrs is not None:
            pulumi.set(__self__, "cidrs", cidrs)
        if countries is not None:
            pulumi.set(__self__, "countries", countries)
        if feeds is not None:
            pulumi.set(__self__, "feeds", feeds)
        if prefix_lists is not None:
            pulumi.set(__self__, "prefix_lists", prefix_lists)

    @property
    @pulumi.getter
    def cidrs(self) -> Optional[Sequence[builtins.str]]:
        """
        List of CIDRs.
        """
        return pulumi.get(self, "cidrs")

    @property
    @pulumi.getter
    def countries(self) -> Optional[Sequence[builtins.str]]:
        """
        List of countries.
        """
        return pulumi.get(self, "countries")

    @property
    @pulumi.getter
    def feeds(self) -> Optional[Sequence[builtins.str]]:
        """
        List of feeds.
        """
        return pulumi.get(self, "feeds")

    @property
    @pulumi.getter(name="prefixLists")
    def prefix_lists(self) -> Optional[Sequence[builtins.str]]:
        """
        List of prefix list.
        """
        return pulumi.get(self, "prefix_lists")


@pulumi.output_type
class GetAccountsAccountDetailResult(dict):
    def __init__(__self__, *,
                 account_id: builtins.str,
                 external_id: builtins.str,
                 onboarding_status: builtins.str):
        """
        :param builtins.str account_id: The account id.
        :param builtins.str external_id: External Id of the onboarded account
        :param builtins.str onboarding_status: Onboarding status of the account.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "external_id", external_id)
        pulumi.set(__self__, "onboarding_status", onboarding_status)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> builtins.str:
        """
        The account id.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> builtins.str:
        """
        External Id of the onboarded account
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter(name="onboardingStatus")
    def onboarding_status(self) -> builtins.str:
        """
        Onboarding status of the account.
        """
        return pulumi.get(self, "onboarding_status")


@pulumi.output_type
class GetNgfwLogProfileLogDestinationResult(dict):
    def __init__(__self__, *,
                 destination: builtins.str,
                 destination_type: builtins.str,
                 log_type: builtins.str):
        """
        :param builtins.str destination: The log destination details.
        :param builtins.str destination_type: The log destination type. Valid values are `S3`, `CloudWatchLogs`, or `KinesisDataFirehose`.
        :param builtins.str log_type: The type of logs. Valid values are `TRAFFIC`, `THREAT`, or `DECRYPTION`.
        """
        pulumi.set(__self__, "destination", destination)
        pulumi.set(__self__, "destination_type", destination_type)
        pulumi.set(__self__, "log_type", log_type)

    @property
    @pulumi.getter
    def destination(self) -> builtins.str:
        """
        The log destination details.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> builtins.str:
        """
        The log destination type. Valid values are `S3`, `CloudWatchLogs`, or `KinesisDataFirehose`.
        """
        return pulumi.get(self, "destination_type")

    @property
    @pulumi.getter(name="logType")
    def log_type(self) -> builtins.str:
        """
        The type of logs. Valid values are `TRAFFIC`, `THREAT`, or `DECRYPTION`.
        """
        return pulumi.get(self, "log_type")


@pulumi.output_type
class GetNgfwStatusResult(dict):
    def __init__(__self__, *,
                 attachments: Sequence['outputs.GetNgfwStatusAttachmentResult'],
                 failure_reason: builtins.str,
                 firewall_status: builtins.str,
                 rulestack_status: builtins.str):
        """
        :param Sequence['GetNgfwStatusAttachmentArgs'] attachments: The firewall attachments.
        :param builtins.str failure_reason: The firewall failure reason.
        :param builtins.str firewall_status: The firewall status.
        :param builtins.str rulestack_status: The rulestack status.
        """
        pulumi.set(__self__, "attachments", attachments)
        pulumi.set(__self__, "failure_reason", failure_reason)
        pulumi.set(__self__, "firewall_status", firewall_status)
        pulumi.set(__self__, "rulestack_status", rulestack_status)

    @property
    @pulumi.getter
    def attachments(self) -> Sequence['outputs.GetNgfwStatusAttachmentResult']:
        """
        The firewall attachments.
        """
        return pulumi.get(self, "attachments")

    @property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> builtins.str:
        """
        The firewall failure reason.
        """
        return pulumi.get(self, "failure_reason")

    @property
    @pulumi.getter(name="firewallStatus")
    def firewall_status(self) -> builtins.str:
        """
        The firewall status.
        """
        return pulumi.get(self, "firewall_status")

    @property
    @pulumi.getter(name="rulestackStatus")
    def rulestack_status(self) -> builtins.str:
        """
        The rulestack status.
        """
        return pulumi.get(self, "rulestack_status")


@pulumi.output_type
class GetNgfwStatusAttachmentResult(dict):
    def __init__(__self__, *,
                 endpoint_id: builtins.str,
                 rejected_reason: builtins.str,
                 status: builtins.str,
                 subnet_id: builtins.str):
        """
        :param builtins.str endpoint_id: The endpoint id.
        :param builtins.str rejected_reason: The reject reason.
        :param builtins.str status: The attachment status.
        :param builtins.str subnet_id: The subnet id.
        """
        pulumi.set(__self__, "endpoint_id", endpoint_id)
        pulumi.set(__self__, "rejected_reason", rejected_reason)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> builtins.str:
        """
        The endpoint id.
        """
        return pulumi.get(self, "endpoint_id")

    @property
    @pulumi.getter(name="rejectedReason")
    def rejected_reason(self) -> builtins.str:
        """
        The reject reason.
        """
        return pulumi.get(self, "rejected_reason")

    @property
    @pulumi.getter
    def status(self) -> builtins.str:
        """
        The attachment status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> builtins.str:
        """
        The subnet id.
        """
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class GetNgfwSubnetMappingResult(dict):
    def __init__(__self__, *,
                 availability_zone: builtins.str,
                 availability_zone_id: builtins.str,
                 subnet_id: builtins.str):
        """
        :param builtins.str availability_zone: The availability zone, for when the endpoint mode is customer managed.
        :param builtins.str availability_zone_id: The availability zone ID, for when the endpoint mode is customer managed.
        :param builtins.str subnet_id: The subnet id, for when the endpoint mode is service managed.
        """
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "availability_zone_id", availability_zone_id)
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        """
        The availability zone, for when the endpoint mode is customer managed.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> builtins.str:
        """
        The availability zone ID, for when the endpoint mode is customer managed.
        """
        return pulumi.get(self, "availability_zone_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> builtins.str:
        """
        The subnet id, for when the endpoint mode is service managed.
        """
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class GetNgfwsInstanceResult(dict):
    def __init__(__self__, *,
                 account_id: builtins.str,
                 name: builtins.str):
        """
        :param builtins.str account_id: The account id.
        :param builtins.str name: The NGFW name.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> builtins.str:
        """
        The account id.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The NGFW name.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetRulestackProfileConfigResult(dict):
    def __init__(__self__, *,
                 anti_spyware: builtins.str,
                 anti_virus: builtins.str,
                 file_blocking: builtins.str,
                 outbound_trust_certificate: builtins.str,
                 outbound_untrust_certificate: builtins.str,
                 url_filtering: builtins.str,
                 vulnerability: builtins.str):
        """
        :param builtins.str anti_spyware: Anti-spyware profile setting.
        :param builtins.str anti_virus: Anti-virus profile setting.
        :param builtins.str file_blocking: File blocking profile setting.
        :param builtins.str outbound_trust_certificate: Outbound trust certificate.
        :param builtins.str outbound_untrust_certificate: Outbound untrust certificate.
        :param builtins.str url_filtering: URL filtering profile setting.
        :param builtins.str vulnerability: Vulnerability profile setting.
        """
        pulumi.set(__self__, "anti_spyware", anti_spyware)
        pulumi.set(__self__, "anti_virus", anti_virus)
        pulumi.set(__self__, "file_blocking", file_blocking)
        pulumi.set(__self__, "outbound_trust_certificate", outbound_trust_certificate)
        pulumi.set(__self__, "outbound_untrust_certificate", outbound_untrust_certificate)
        pulumi.set(__self__, "url_filtering", url_filtering)
        pulumi.set(__self__, "vulnerability", vulnerability)

    @property
    @pulumi.getter(name="antiSpyware")
    def anti_spyware(self) -> builtins.str:
        """
        Anti-spyware profile setting.
        """
        return pulumi.get(self, "anti_spyware")

    @property
    @pulumi.getter(name="antiVirus")
    def anti_virus(self) -> builtins.str:
        """
        Anti-virus profile setting.
        """
        return pulumi.get(self, "anti_virus")

    @property
    @pulumi.getter(name="fileBlocking")
    def file_blocking(self) -> builtins.str:
        """
        File blocking profile setting.
        """
        return pulumi.get(self, "file_blocking")

    @property
    @pulumi.getter(name="outboundTrustCertificate")
    def outbound_trust_certificate(self) -> builtins.str:
        """
        Outbound trust certificate.
        """
        return pulumi.get(self, "outbound_trust_certificate")

    @property
    @pulumi.getter(name="outboundUntrustCertificate")
    def outbound_untrust_certificate(self) -> builtins.str:
        """
        Outbound untrust certificate.
        """
        return pulumi.get(self, "outbound_untrust_certificate")

    @property
    @pulumi.getter(name="urlFiltering")
    def url_filtering(self) -> builtins.str:
        """
        URL filtering profile setting.
        """
        return pulumi.get(self, "url_filtering")

    @property
    @pulumi.getter
    def vulnerability(self) -> builtins.str:
        """
        Vulnerability profile setting.
        """
        return pulumi.get(self, "vulnerability")


@pulumi.output_type
class GetSecurityRuleCategoryResult(dict):
    def __init__(__self__, *,
                 feeds: Sequence[builtins.str],
                 url_category_names: Sequence[builtins.str]):
        """
        :param Sequence[builtins.str] feeds: List of feeds.
        :param Sequence[builtins.str] url_category_names: List of URL category names.
        """
        pulumi.set(__self__, "feeds", feeds)
        pulumi.set(__self__, "url_category_names", url_category_names)

    @property
    @pulumi.getter
    def feeds(self) -> Sequence[builtins.str]:
        """
        List of feeds.
        """
        return pulumi.get(self, "feeds")

    @property
    @pulumi.getter(name="urlCategoryNames")
    def url_category_names(self) -> Sequence[builtins.str]:
        """
        List of URL category names.
        """
        return pulumi.get(self, "url_category_names")


@pulumi.output_type
class GetSecurityRuleDestinationResult(dict):
    def __init__(__self__, *,
                 cidrs: Sequence[builtins.str],
                 countries: Sequence[builtins.str],
                 feeds: Sequence[builtins.str],
                 fqdn_lists: Sequence[builtins.str],
                 prefix_lists: Sequence[builtins.str]):
        """
        :param Sequence[builtins.str] cidrs: List of CIDRs.
        :param Sequence[builtins.str] countries: List of countries.
        :param Sequence[builtins.str] feeds: List of feeds.
        :param Sequence[builtins.str] fqdn_lists: List of FQDN lists.
        :param Sequence[builtins.str] prefix_lists: List of prefix list.
        """
        pulumi.set(__self__, "cidrs", cidrs)
        pulumi.set(__self__, "countries", countries)
        pulumi.set(__self__, "feeds", feeds)
        pulumi.set(__self__, "fqdn_lists", fqdn_lists)
        pulumi.set(__self__, "prefix_lists", prefix_lists)

    @property
    @pulumi.getter
    def cidrs(self) -> Sequence[builtins.str]:
        """
        List of CIDRs.
        """
        return pulumi.get(self, "cidrs")

    @property
    @pulumi.getter
    def countries(self) -> Sequence[builtins.str]:
        """
        List of countries.
        """
        return pulumi.get(self, "countries")

    @property
    @pulumi.getter
    def feeds(self) -> Sequence[builtins.str]:
        """
        List of feeds.
        """
        return pulumi.get(self, "feeds")

    @property
    @pulumi.getter(name="fqdnLists")
    def fqdn_lists(self) -> Sequence[builtins.str]:
        """
        List of FQDN lists.
        """
        return pulumi.get(self, "fqdn_lists")

    @property
    @pulumi.getter(name="prefixLists")
    def prefix_lists(self) -> Sequence[builtins.str]:
        """
        List of prefix list.
        """
        return pulumi.get(self, "prefix_lists")


@pulumi.output_type
class GetSecurityRuleSourceResult(dict):
    def __init__(__self__, *,
                 cidrs: Sequence[builtins.str],
                 countries: Sequence[builtins.str],
                 feeds: Sequence[builtins.str],
                 prefix_lists: Sequence[builtins.str]):
        """
        :param Sequence[builtins.str] cidrs: List of CIDRs.
        :param Sequence[builtins.str] countries: List of countries.
        :param Sequence[builtins.str] feeds: List of feeds.
        :param Sequence[builtins.str] prefix_lists: List of prefix list.
        """
        pulumi.set(__self__, "cidrs", cidrs)
        pulumi.set(__self__, "countries", countries)
        pulumi.set(__self__, "feeds", feeds)
        pulumi.set(__self__, "prefix_lists", prefix_lists)

    @property
    @pulumi.getter
    def cidrs(self) -> Sequence[builtins.str]:
        """
        List of CIDRs.
        """
        return pulumi.get(self, "cidrs")

    @property
    @pulumi.getter
    def countries(self) -> Sequence[builtins.str]:
        """
        List of countries.
        """
        return pulumi.get(self, "countries")

    @property
    @pulumi.getter
    def feeds(self) -> Sequence[builtins.str]:
        """
        List of feeds.
        """
        return pulumi.get(self, "feeds")

    @property
    @pulumi.getter(name="prefixLists")
    def prefix_lists(self) -> Sequence[builtins.str]:
        """
        List of prefix list.
        """
        return pulumi.get(self, "prefix_lists")


