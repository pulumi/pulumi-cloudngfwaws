// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws.inputs;

import com.pulumi.cloudngfwaws.inputs.NgfwStatusArgs;
import com.pulumi.cloudngfwaws.inputs.NgfwSubnetMappingArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class NgfwState extends com.pulumi.resources.ResourceArgs {

    public static final NgfwState Empty = new NgfwState();

    /**
     * The account ID. This field is mandatory if using multiple accounts.
     * 
     */
    @Import(name="accountId")
    private @Nullable Output<String> accountId;

    /**
     * @return The account ID. This field is mandatory if using multiple accounts.
     * 
     */
    public Optional<Output<String>> accountId() {
        return Optional.ofNullable(this.accountId);
    }

    /**
     * App-ID version number.
     * 
     */
    @Import(name="appIdVersion")
    private @Nullable Output<String> appIdVersion;

    /**
     * @return App-ID version number.
     * 
     */
    public Optional<Output<String>> appIdVersion() {
        return Optional.ofNullable(this.appIdVersion);
    }

    /**
     * Automatic App-ID upgrade version number. Defaults to `true`.
     * 
     */
    @Import(name="automaticUpgradeAppIdVersion")
    private @Nullable Output<Boolean> automaticUpgradeAppIdVersion;

    /**
     * @return Automatic App-ID upgrade version number. Defaults to `true`.
     * 
     */
    public Optional<Output<Boolean>> automaticUpgradeAppIdVersion() {
        return Optional.ofNullable(this.automaticUpgradeAppIdVersion);
    }

    /**
     * The description.
     * 
     */
    @Import(name="description")
    private @Nullable Output<String> description;

    /**
     * @return The description.
     * 
     */
    public Optional<Output<String>> description() {
        return Optional.ofNullable(this.description);
    }

    /**
     * Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
     * 
     */
    @Import(name="endpointMode")
    private @Nullable Output<String> endpointMode;

    /**
     * @return Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
     * 
     */
    public Optional<Output<String>> endpointMode() {
        return Optional.ofNullable(this.endpointMode);
    }

    /**
     * The endpoint service name.
     * 
     */
    @Import(name="endpointServiceName")
    private @Nullable Output<String> endpointServiceName;

    /**
     * @return The endpoint service name.
     * 
     */
    public Optional<Output<String>> endpointServiceName() {
        return Optional.ofNullable(this.endpointServiceName);
    }

    /**
     * The Id of the NGFW.
     * 
     */
    @Import(name="firewallId")
    private @Nullable Output<String> firewallId;

    /**
     * @return The Id of the NGFW.
     * 
     */
    public Optional<Output<String>> firewallId() {
        return Optional.ofNullable(this.firewallId);
    }

    /**
     * The global rulestack for this NGFW.
     * 
     */
    @Import(name="globalRulestack")
    private @Nullable Output<String> globalRulestack;

    /**
     * @return The global rulestack for this NGFW.
     * 
     */
    public Optional<Output<String>> globalRulestack() {
        return Optional.ofNullable(this.globalRulestack);
    }

    /**
     * A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
     * 
     */
    @Import(name="linkId")
    private @Nullable Output<String> linkId;

    /**
     * @return A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
     * 
     */
    public Optional<Output<String>> linkId() {
        return Optional.ofNullable(this.linkId);
    }

    /**
     * The link status.
     * 
     */
    @Import(name="linkStatus")
    private @Nullable Output<String> linkStatus;

    /**
     * @return The link status.
     * 
     */
    public Optional<Output<String>> linkStatus() {
        return Optional.ofNullable(this.linkStatus);
    }

    /**
     * Share NGFW with Multiple VPCs. This feature can be enabled only if the endpoint_mode is CustomerManaged.
     * 
     */
    @Import(name="multiVpc")
    private @Nullable Output<Boolean> multiVpc;

    /**
     * @return Share NGFW with Multiple VPCs. This feature can be enabled only if the endpoint_mode is CustomerManaged.
     * 
     */
    public Optional<Output<Boolean>> multiVpc() {
        return Optional.ofNullable(this.multiVpc);
    }

    /**
     * The NGFW name.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The NGFW name.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The rulestack for this NGFW.
     * 
     */
    @Import(name="rulestack")
    private @Nullable Output<String> rulestack;

    /**
     * @return The rulestack for this NGFW.
     * 
     */
    public Optional<Output<String>> rulestack() {
        return Optional.ofNullable(this.rulestack);
    }

    @Import(name="statuses")
    private @Nullable Output<List<NgfwStatusArgs>> statuses;

    public Optional<Output<List<NgfwStatusArgs>>> statuses() {
        return Optional.ofNullable(this.statuses);
    }

    /**
     * Subnet mappings.
     * 
     */
    @Import(name="subnetMappings")
    private @Nullable Output<List<NgfwSubnetMappingArgs>> subnetMappings;

    /**
     * @return Subnet mappings.
     * 
     */
    public Optional<Output<List<NgfwSubnetMappingArgs>>> subnetMappings() {
        return Optional.ofNullable(this.subnetMappings);
    }

    /**
     * The tags.
     * 
     */
    @Import(name="tags")
    private @Nullable Output<Map<String,String>> tags;

    /**
     * @return The tags.
     * 
     */
    public Optional<Output<Map<String,String>>> tags() {
        return Optional.ofNullable(this.tags);
    }

    /**
     * The update token.
     * 
     */
    @Import(name="updateToken")
    private @Nullable Output<String> updateToken;

    /**
     * @return The update token.
     * 
     */
    public Optional<Output<String>> updateToken() {
        return Optional.ofNullable(this.updateToken);
    }

    /**
     * The vpc id.
     * 
     */
    @Import(name="vpcId")
    private @Nullable Output<String> vpcId;

    /**
     * @return The vpc id.
     * 
     */
    public Optional<Output<String>> vpcId() {
        return Optional.ofNullable(this.vpcId);
    }

    private NgfwState() {}

    private NgfwState(NgfwState $) {
        this.accountId = $.accountId;
        this.appIdVersion = $.appIdVersion;
        this.automaticUpgradeAppIdVersion = $.automaticUpgradeAppIdVersion;
        this.description = $.description;
        this.endpointMode = $.endpointMode;
        this.endpointServiceName = $.endpointServiceName;
        this.firewallId = $.firewallId;
        this.globalRulestack = $.globalRulestack;
        this.linkId = $.linkId;
        this.linkStatus = $.linkStatus;
        this.multiVpc = $.multiVpc;
        this.name = $.name;
        this.rulestack = $.rulestack;
        this.statuses = $.statuses;
        this.subnetMappings = $.subnetMappings;
        this.tags = $.tags;
        this.updateToken = $.updateToken;
        this.vpcId = $.vpcId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(NgfwState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private NgfwState $;

        public Builder() {
            $ = new NgfwState();
        }

        public Builder(NgfwState defaults) {
            $ = new NgfwState(Objects.requireNonNull(defaults));
        }

        /**
         * @param accountId The account ID. This field is mandatory if using multiple accounts.
         * 
         * @return builder
         * 
         */
        public Builder accountId(@Nullable Output<String> accountId) {
            $.accountId = accountId;
            return this;
        }

        /**
         * @param accountId The account ID. This field is mandatory if using multiple accounts.
         * 
         * @return builder
         * 
         */
        public Builder accountId(String accountId) {
            return accountId(Output.of(accountId));
        }

        /**
         * @param appIdVersion App-ID version number.
         * 
         * @return builder
         * 
         */
        public Builder appIdVersion(@Nullable Output<String> appIdVersion) {
            $.appIdVersion = appIdVersion;
            return this;
        }

        /**
         * @param appIdVersion App-ID version number.
         * 
         * @return builder
         * 
         */
        public Builder appIdVersion(String appIdVersion) {
            return appIdVersion(Output.of(appIdVersion));
        }

        /**
         * @param automaticUpgradeAppIdVersion Automatic App-ID upgrade version number. Defaults to `true`.
         * 
         * @return builder
         * 
         */
        public Builder automaticUpgradeAppIdVersion(@Nullable Output<Boolean> automaticUpgradeAppIdVersion) {
            $.automaticUpgradeAppIdVersion = automaticUpgradeAppIdVersion;
            return this;
        }

        /**
         * @param automaticUpgradeAppIdVersion Automatic App-ID upgrade version number. Defaults to `true`.
         * 
         * @return builder
         * 
         */
        public Builder automaticUpgradeAppIdVersion(Boolean automaticUpgradeAppIdVersion) {
            return automaticUpgradeAppIdVersion(Output.of(automaticUpgradeAppIdVersion));
        }

        /**
         * @param description The description.
         * 
         * @return builder
         * 
         */
        public Builder description(@Nullable Output<String> description) {
            $.description = description;
            return this;
        }

        /**
         * @param description The description.
         * 
         * @return builder
         * 
         */
        public Builder description(String description) {
            return description(Output.of(description));
        }

        /**
         * @param endpointMode Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
         * 
         * @return builder
         * 
         */
        public Builder endpointMode(@Nullable Output<String> endpointMode) {
            $.endpointMode = endpointMode;
            return this;
        }

        /**
         * @param endpointMode Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
         * 
         * @return builder
         * 
         */
        public Builder endpointMode(String endpointMode) {
            return endpointMode(Output.of(endpointMode));
        }

        /**
         * @param endpointServiceName The endpoint service name.
         * 
         * @return builder
         * 
         */
        public Builder endpointServiceName(@Nullable Output<String> endpointServiceName) {
            $.endpointServiceName = endpointServiceName;
            return this;
        }

        /**
         * @param endpointServiceName The endpoint service name.
         * 
         * @return builder
         * 
         */
        public Builder endpointServiceName(String endpointServiceName) {
            return endpointServiceName(Output.of(endpointServiceName));
        }

        /**
         * @param firewallId The Id of the NGFW.
         * 
         * @return builder
         * 
         */
        public Builder firewallId(@Nullable Output<String> firewallId) {
            $.firewallId = firewallId;
            return this;
        }

        /**
         * @param firewallId The Id of the NGFW.
         * 
         * @return builder
         * 
         */
        public Builder firewallId(String firewallId) {
            return firewallId(Output.of(firewallId));
        }

        /**
         * @param globalRulestack The global rulestack for this NGFW.
         * 
         * @return builder
         * 
         */
        public Builder globalRulestack(@Nullable Output<String> globalRulestack) {
            $.globalRulestack = globalRulestack;
            return this;
        }

        /**
         * @param globalRulestack The global rulestack for this NGFW.
         * 
         * @return builder
         * 
         */
        public Builder globalRulestack(String globalRulestack) {
            return globalRulestack(Output.of(globalRulestack));
        }

        /**
         * @param linkId A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
         * 
         * @return builder
         * 
         */
        public Builder linkId(@Nullable Output<String> linkId) {
            $.linkId = linkId;
            return this;
        }

        /**
         * @param linkId A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
         * 
         * @return builder
         * 
         */
        public Builder linkId(String linkId) {
            return linkId(Output.of(linkId));
        }

        /**
         * @param linkStatus The link status.
         * 
         * @return builder
         * 
         */
        public Builder linkStatus(@Nullable Output<String> linkStatus) {
            $.linkStatus = linkStatus;
            return this;
        }

        /**
         * @param linkStatus The link status.
         * 
         * @return builder
         * 
         */
        public Builder linkStatus(String linkStatus) {
            return linkStatus(Output.of(linkStatus));
        }

        /**
         * @param multiVpc Share NGFW with Multiple VPCs. This feature can be enabled only if the endpoint_mode is CustomerManaged.
         * 
         * @return builder
         * 
         */
        public Builder multiVpc(@Nullable Output<Boolean> multiVpc) {
            $.multiVpc = multiVpc;
            return this;
        }

        /**
         * @param multiVpc Share NGFW with Multiple VPCs. This feature can be enabled only if the endpoint_mode is CustomerManaged.
         * 
         * @return builder
         * 
         */
        public Builder multiVpc(Boolean multiVpc) {
            return multiVpc(Output.of(multiVpc));
        }

        /**
         * @param name The NGFW name.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The NGFW name.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param rulestack The rulestack for this NGFW.
         * 
         * @return builder
         * 
         */
        public Builder rulestack(@Nullable Output<String> rulestack) {
            $.rulestack = rulestack;
            return this;
        }

        /**
         * @param rulestack The rulestack for this NGFW.
         * 
         * @return builder
         * 
         */
        public Builder rulestack(String rulestack) {
            return rulestack(Output.of(rulestack));
        }

        public Builder statuses(@Nullable Output<List<NgfwStatusArgs>> statuses) {
            $.statuses = statuses;
            return this;
        }

        public Builder statuses(List<NgfwStatusArgs> statuses) {
            return statuses(Output.of(statuses));
        }

        public Builder statuses(NgfwStatusArgs... statuses) {
            return statuses(List.of(statuses));
        }

        /**
         * @param subnetMappings Subnet mappings.
         * 
         * @return builder
         * 
         */
        public Builder subnetMappings(@Nullable Output<List<NgfwSubnetMappingArgs>> subnetMappings) {
            $.subnetMappings = subnetMappings;
            return this;
        }

        /**
         * @param subnetMappings Subnet mappings.
         * 
         * @return builder
         * 
         */
        public Builder subnetMappings(List<NgfwSubnetMappingArgs> subnetMappings) {
            return subnetMappings(Output.of(subnetMappings));
        }

        /**
         * @param subnetMappings Subnet mappings.
         * 
         * @return builder
         * 
         */
        public Builder subnetMappings(NgfwSubnetMappingArgs... subnetMappings) {
            return subnetMappings(List.of(subnetMappings));
        }

        /**
         * @param tags The tags.
         * 
         * @return builder
         * 
         */
        public Builder tags(@Nullable Output<Map<String,String>> tags) {
            $.tags = tags;
            return this;
        }

        /**
         * @param tags The tags.
         * 
         * @return builder
         * 
         */
        public Builder tags(Map<String,String> tags) {
            return tags(Output.of(tags));
        }

        /**
         * @param updateToken The update token.
         * 
         * @return builder
         * 
         */
        public Builder updateToken(@Nullable Output<String> updateToken) {
            $.updateToken = updateToken;
            return this;
        }

        /**
         * @param updateToken The update token.
         * 
         * @return builder
         * 
         */
        public Builder updateToken(String updateToken) {
            return updateToken(Output.of(updateToken));
        }

        /**
         * @param vpcId The vpc id.
         * 
         * @return builder
         * 
         */
        public Builder vpcId(@Nullable Output<String> vpcId) {
            $.vpcId = vpcId;
            return this;
        }

        /**
         * @param vpcId The vpc id.
         * 
         * @return builder
         * 
         */
        public Builder vpcId(String vpcId) {
            return vpcId(Output.of(vpcId));
        }

        public NgfwState build() {
            return $;
        }
    }

}
