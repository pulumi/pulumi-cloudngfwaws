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

__all__ = [
    'GetSecurityRuleResult',
    'AwaitableGetSecurityRuleResult',
    'get_security_rule',
    'get_security_rule_output',
]

@pulumi.output_type
class GetSecurityRuleResult:
    """
    A collection of values returned by getSecurityRule.
    """
    def __init__(__self__, action=None, applications=None, audit_comment=None, categories=None, config_type=None, decryption_rule_type=None, description=None, destinations=None, enabled=None, id=None, logging=None, name=None, negate_destination=None, negate_source=None, priority=None, prot_port_lists=None, protocol=None, rule_list=None, rulestack=None, scope=None, sources=None, tags=None, update_token=None):
        if action and not isinstance(action, str):
            raise TypeError("Expected argument 'action' to be a str")
        pulumi.set(__self__, "action", action)
        if applications and not isinstance(applications, list):
            raise TypeError("Expected argument 'applications' to be a list")
        pulumi.set(__self__, "applications", applications)
        if audit_comment and not isinstance(audit_comment, str):
            raise TypeError("Expected argument 'audit_comment' to be a str")
        pulumi.set(__self__, "audit_comment", audit_comment)
        if categories and not isinstance(categories, list):
            raise TypeError("Expected argument 'categories' to be a list")
        pulumi.set(__self__, "categories", categories)
        if config_type and not isinstance(config_type, str):
            raise TypeError("Expected argument 'config_type' to be a str")
        pulumi.set(__self__, "config_type", config_type)
        if decryption_rule_type and not isinstance(decryption_rule_type, str):
            raise TypeError("Expected argument 'decryption_rule_type' to be a str")
        pulumi.set(__self__, "decryption_rule_type", decryption_rule_type)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if destinations and not isinstance(destinations, list):
            raise TypeError("Expected argument 'destinations' to be a list")
        pulumi.set(__self__, "destinations", destinations)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if logging and not isinstance(logging, bool):
            raise TypeError("Expected argument 'logging' to be a bool")
        pulumi.set(__self__, "logging", logging)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if negate_destination and not isinstance(negate_destination, bool):
            raise TypeError("Expected argument 'negate_destination' to be a bool")
        pulumi.set(__self__, "negate_destination", negate_destination)
        if negate_source and not isinstance(negate_source, bool):
            raise TypeError("Expected argument 'negate_source' to be a bool")
        pulumi.set(__self__, "negate_source", negate_source)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if prot_port_lists and not isinstance(prot_port_lists, list):
            raise TypeError("Expected argument 'prot_port_lists' to be a list")
        pulumi.set(__self__, "prot_port_lists", prot_port_lists)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if rule_list and not isinstance(rule_list, str):
            raise TypeError("Expected argument 'rule_list' to be a str")
        pulumi.set(__self__, "rule_list", rule_list)
        if rulestack and not isinstance(rulestack, str):
            raise TypeError("Expected argument 'rulestack' to be a str")
        pulumi.set(__self__, "rulestack", rulestack)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if sources and not isinstance(sources, list):
            raise TypeError("Expected argument 'sources' to be a list")
        pulumi.set(__self__, "sources", sources)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if update_token and not isinstance(update_token, str):
            raise TypeError("Expected argument 'update_token' to be a str")
        pulumi.set(__self__, "update_token", update_token)

    @property
    @pulumi.getter
    def action(self) -> builtins.str:
        """
        The action to take. Valid values are `Allow`, `DenySilent`, `DenyResetServer`, or `DenyResetBoth`.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def applications(self) -> Sequence[builtins.str]:
        """
        The list of applications.
        """
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> builtins.str:
        """
        The audit comment.
        """
        return pulumi.get(self, "audit_comment")

    @property
    @pulumi.getter
    def categories(self) -> Sequence['outputs.GetSecurityRuleCategoryResult']:
        """
        The category spec.
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter(name="configType")
    def config_type(self) -> Optional[builtins.str]:
        """
        Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
        """
        return pulumi.get(self, "config_type")

    @property
    @pulumi.getter(name="decryptionRuleType")
    def decryption_rule_type(self) -> builtins.str:
        """
        Decryption rule type. Valid values are ``or`SSLOutboundInspection`.
        """
        return pulumi.get(self, "decryption_rule_type")

    @property
    @pulumi.getter
    def description(self) -> builtins.str:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def destinations(self) -> Sequence['outputs.GetSecurityRuleDestinationResult']:
        """
        The destination spec.
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def enabled(self) -> builtins.bool:
        """
        Set to false to disable this rule.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def logging(self) -> builtins.bool:
        """
        Enable logging at end.
        """
        return pulumi.get(self, "logging")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="negateDestination")
    def negate_destination(self) -> builtins.bool:
        """
        Negate the destination definition.
        """
        return pulumi.get(self, "negate_destination")

    @property
    @pulumi.getter(name="negateSource")
    def negate_source(self) -> builtins.bool:
        """
        Negate the source definition.
        """
        return pulumi.get(self, "negate_source")

    @property
    @pulumi.getter
    def priority(self) -> builtins.int:
        """
        The rule priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="protPortLists")
    def prot_port_lists(self) -> Sequence[builtins.str]:
        """
        Protocol port list.
        """
        return pulumi.get(self, "prot_port_lists")

    @property
    @pulumi.getter
    def protocol(self) -> builtins.str:
        """
        The protocol.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="ruleList")
    def rule_list(self) -> Optional[builtins.str]:
        """
        The rulebase. Valid values are `PreRule`, `PostRule`, or `LocalRule`. Defaults to `PreRule`.
        """
        return pulumi.get(self, "rule_list")

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
    def sources(self) -> Sequence['outputs.GetSecurityRuleSourceResult']:
        """
        The source spec.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, builtins.str]:
        """
        The tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> builtins.str:
        """
        The update token.
        """
        return pulumi.get(self, "update_token")


class AwaitableGetSecurityRuleResult(GetSecurityRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityRuleResult(
            action=self.action,
            applications=self.applications,
            audit_comment=self.audit_comment,
            categories=self.categories,
            config_type=self.config_type,
            decryption_rule_type=self.decryption_rule_type,
            description=self.description,
            destinations=self.destinations,
            enabled=self.enabled,
            id=self.id,
            logging=self.logging,
            name=self.name,
            negate_destination=self.negate_destination,
            negate_source=self.negate_source,
            priority=self.priority,
            prot_port_lists=self.prot_port_lists,
            protocol=self.protocol,
            rule_list=self.rule_list,
            rulestack=self.rulestack,
            scope=self.scope,
            sources=self.sources,
            tags=self.tags,
            update_token=self.update_token)


def get_security_rule(config_type: Optional[builtins.str] = None,
                      priority: Optional[builtins.int] = None,
                      rule_list: Optional[builtins.str] = None,
                      rulestack: Optional[builtins.str] = None,
                      scope: Optional[builtins.str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityRuleResult:
    """
    Data source for retrieving security rule information.

    ## Admin Permission Type

    * `Rulestack` (for `scope="Local"`)
    * `Global Rulestack` (for `scope="Global"`)


    :param builtins.str config_type: Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
    :param builtins.int priority: The rule priority.
    :param builtins.str rule_list: The rulebase. Valid values are `PreRule`, `PostRule`, or `LocalRule`. Defaults to `PreRule`.
    :param builtins.str rulestack: The rulestack.
    :param builtins.str scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
    """
    __args__ = dict()
    __args__['configType'] = config_type
    __args__['priority'] = priority
    __args__['ruleList'] = rule_list
    __args__['rulestack'] = rulestack
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudngfwaws:index/getSecurityRule:getSecurityRule', __args__, opts=opts, typ=GetSecurityRuleResult).value

    return AwaitableGetSecurityRuleResult(
        action=pulumi.get(__ret__, 'action'),
        applications=pulumi.get(__ret__, 'applications'),
        audit_comment=pulumi.get(__ret__, 'audit_comment'),
        categories=pulumi.get(__ret__, 'categories'),
        config_type=pulumi.get(__ret__, 'config_type'),
        decryption_rule_type=pulumi.get(__ret__, 'decryption_rule_type'),
        description=pulumi.get(__ret__, 'description'),
        destinations=pulumi.get(__ret__, 'destinations'),
        enabled=pulumi.get(__ret__, 'enabled'),
        id=pulumi.get(__ret__, 'id'),
        logging=pulumi.get(__ret__, 'logging'),
        name=pulumi.get(__ret__, 'name'),
        negate_destination=pulumi.get(__ret__, 'negate_destination'),
        negate_source=pulumi.get(__ret__, 'negate_source'),
        priority=pulumi.get(__ret__, 'priority'),
        prot_port_lists=pulumi.get(__ret__, 'prot_port_lists'),
        protocol=pulumi.get(__ret__, 'protocol'),
        rule_list=pulumi.get(__ret__, 'rule_list'),
        rulestack=pulumi.get(__ret__, 'rulestack'),
        scope=pulumi.get(__ret__, 'scope'),
        sources=pulumi.get(__ret__, 'sources'),
        tags=pulumi.get(__ret__, 'tags'),
        update_token=pulumi.get(__ret__, 'update_token'))
def get_security_rule_output(config_type: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                             priority: Optional[pulumi.Input[builtins.int]] = None,
                             rule_list: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                             rulestack: Optional[pulumi.Input[builtins.str]] = None,
                             scope: Optional[pulumi.Input[Optional[builtins.str]]] = None,
                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetSecurityRuleResult]:
    """
    Data source for retrieving security rule information.

    ## Admin Permission Type

    * `Rulestack` (for `scope="Local"`)
    * `Global Rulestack` (for `scope="Global"`)


    :param builtins.str config_type: Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
    :param builtins.int priority: The rule priority.
    :param builtins.str rule_list: The rulebase. Valid values are `PreRule`, `PostRule`, or `LocalRule`. Defaults to `PreRule`.
    :param builtins.str rulestack: The rulestack.
    :param builtins.str scope: The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
    """
    __args__ = dict()
    __args__['configType'] = config_type
    __args__['priority'] = priority
    __args__['ruleList'] = rule_list
    __args__['rulestack'] = rulestack
    __args__['scope'] = scope
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudngfwaws:index/getSecurityRule:getSecurityRule', __args__, opts=opts, typ=GetSecurityRuleResult)
    return __ret__.apply(lambda __response__: GetSecurityRuleResult(
        action=pulumi.get(__response__, 'action'),
        applications=pulumi.get(__response__, 'applications'),
        audit_comment=pulumi.get(__response__, 'audit_comment'),
        categories=pulumi.get(__response__, 'categories'),
        config_type=pulumi.get(__response__, 'config_type'),
        decryption_rule_type=pulumi.get(__response__, 'decryption_rule_type'),
        description=pulumi.get(__response__, 'description'),
        destinations=pulumi.get(__response__, 'destinations'),
        enabled=pulumi.get(__response__, 'enabled'),
        id=pulumi.get(__response__, 'id'),
        logging=pulumi.get(__response__, 'logging'),
        name=pulumi.get(__response__, 'name'),
        negate_destination=pulumi.get(__response__, 'negate_destination'),
        negate_source=pulumi.get(__response__, 'negate_source'),
        priority=pulumi.get(__response__, 'priority'),
        prot_port_lists=pulumi.get(__response__, 'prot_port_lists'),
        protocol=pulumi.get(__response__, 'protocol'),
        rule_list=pulumi.get(__response__, 'rule_list'),
        rulestack=pulumi.get(__response__, 'rulestack'),
        scope=pulumi.get(__response__, 'scope'),
        sources=pulumi.get(__response__, 'sources'),
        tags=pulumi.get(__response__, 'tags'),
        update_token=pulumi.get(__response__, 'update_token')))
