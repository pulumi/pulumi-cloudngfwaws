// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws;

import com.pulumi.cloudngfwaws.ProviderArgs;
import com.pulumi.cloudngfwaws.Utilities;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * The provider type for the cloudngfwaws package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 * 
 */
@ResourceType(type="pulumi:providers:cloudngfwaws")
public class Provider extends com.pulumi.resources.ProviderResource {
    /**
     * (Used for the initial `sts assume role`) AWS access key. Environment variable: `CLOUDNGFWAWS_ACCESS_KEY`. JSON conf file
     * variable: `access-key`.
     * 
     */
    @Export(name="accessKey", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> accessKey;

    /**
     * @return (Used for the initial `sts assume role`) AWS access key. Environment variable: `CLOUDNGFWAWS_ACCESS_KEY`. JSON conf file
     * variable: `access-key`.
     * 
     */
    public Output<Optional<String>> accessKey() {
        return Codegen.optional(this.accessKey);
    }
    /**
     * The ARN allowing account admin permissions. Environment variable: `CLOUDNGFWAWS_ACCT_ADMIN_ARN`. JSON conf file
     * variable: `account-admin-arn`.
     * 
     */
    @Export(name="accountAdminArn", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> accountAdminArn;

    /**
     * @return The ARN allowing account admin permissions. Environment variable: `CLOUDNGFWAWS_ACCT_ADMIN_ARN`. JSON conf file
     * variable: `account-admin-arn`.
     * 
     */
    public Output<Optional<String>> accountAdminArn() {
        return Codegen.optional(this.accountAdminArn);
    }
    /**
     * The ARN allowing firewall, rulestack, and global rulestack admin permissions. Global rulestack admin permissions can be
     * enabled only if the AWS account is onboarded by AWS Firewall Manager. Use &#39;lfa_arn&#39; and &#39;lra_arn&#39; if you want to enable
     * only firewall and rulestack admin permissions. Environment variable: `CLOUDNGFWAWS_ARN`. JSON conf file variable: `arn`.
     * 
     */
    @Export(name="arn", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> arn;

    /**
     * @return The ARN allowing firewall, rulestack, and global rulestack admin permissions. Global rulestack admin permissions can be
     * enabled only if the AWS account is onboarded by AWS Firewall Manager. Use &#39;lfa_arn&#39; and &#39;lra_arn&#39; if you want to enable
     * only firewall and rulestack admin permissions. Environment variable: `CLOUDNGFWAWS_ARN`. JSON conf file variable: `arn`.
     * 
     */
    public Output<Optional<String>> arn() {
        return Codegen.optional(this.arn);
    }
    /**
     * The ARN allowing global rulestack admin permissions. Global rulestack admin permissions can be enabled only if the AWS
     * account is onboarded by AWS Firewall Manager. &#39;gra_arn&#39; is preferentially used over the `arn` param if both are
     * specified. Environment variable: `CLOUDNGFWAWS_GRA_ARN`. JSON conf file variable: `gra-arn`.
     * 
     */
    @Export(name="graArn", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> graArn;

    /**
     * @return The ARN allowing global rulestack admin permissions. Global rulestack admin permissions can be enabled only if the AWS
     * account is onboarded by AWS Firewall Manager. &#39;gra_arn&#39; is preferentially used over the `arn` param if both are
     * specified. Environment variable: `CLOUDNGFWAWS_GRA_ARN`. JSON conf file variable: `gra-arn`.
     * 
     */
    public Output<Optional<String>> graArn() {
        return Codegen.optional(this.graArn);
    }
    /**
     * The hostname of the API (default: `api.us-east-1.aws.cloudngfw.paloaltonetworks.com`). Environment variable:
     * `CLOUDNGFWAWS_HOST`. JSON conf file variable: `host`.
     * 
     */
    @Export(name="host", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> host;

    /**
     * @return The hostname of the API (default: `api.us-east-1.aws.cloudngfw.paloaltonetworks.com`). Environment variable:
     * `CLOUDNGFWAWS_HOST`. JSON conf file variable: `host`.
     * 
     */
    public Output<Optional<String>> host() {
        return Codegen.optional(this.host);
    }
    /**
     * Retrieve provider configuration from this JSON file.
     * 
     */
    @Export(name="jsonConfigFile", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> jsonConfigFile;

    /**
     * @return Retrieve provider configuration from this JSON file.
     * 
     */
    public Output<Optional<String>> jsonConfigFile() {
        return Codegen.optional(this.jsonConfigFile);
    }
    /**
     * The ARN allowing firewall admin permissions. This is preferentially used over the `arn` param if both are specified.
     * Environment variable: `CLOUDNGFWAWS_LFA_ARN`. JSON conf file variable: `lfa-arn`.
     * 
     */
    @Export(name="lfaArn", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> lfaArn;

    /**
     * @return The ARN allowing firewall admin permissions. This is preferentially used over the `arn` param if both are specified.
     * Environment variable: `CLOUDNGFWAWS_LFA_ARN`. JSON conf file variable: `lfa-arn`.
     * 
     */
    public Output<Optional<String>> lfaArn() {
        return Codegen.optional(this.lfaArn);
    }
    /**
     * The ARN allowing rulestack admin permissions. This is preferentially used over the `arn` param if both are specified.
     * Environment variable: `CLOUDNGFWAWS_LRA_ARN`. JSON conf file variable: `lra-arn`.
     * 
     */
    @Export(name="lraArn", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> lraArn;

    /**
     * @return The ARN allowing rulestack admin permissions. This is preferentially used over the `arn` param if both are specified.
     * Environment variable: `CLOUDNGFWAWS_LRA_ARN`. JSON conf file variable: `lra-arn`.
     * 
     */
    public Output<Optional<String>> lraArn() {
        return Codegen.optional(this.lraArn);
    }
    /**
     * AWS management plane region. Environment variable: `CLOUDNGFWAWS_MP_REGION`. JSON conf file variable: `mp_region`.
     * 
     */
    @Export(name="mpRegion", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> mpRegion;

    /**
     * @return AWS management plane region. Environment variable: `CLOUDNGFWAWS_MP_REGION`. JSON conf file variable: `mp_region`.
     * 
     */
    public Output<Optional<String>> mpRegion() {
        return Codegen.optional(this.mpRegion);
    }
    /**
     * AWS management plane MP region host Environment variable: `CLOUDNGFWAWS_MP_REGION_HOST`. JSON conf file variable:
     * `mp_region_host`.
     * 
     */
    @Export(name="mpRegionHost", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> mpRegionHost;

    /**
     * @return AWS management plane MP region host Environment variable: `CLOUDNGFWAWS_MP_REGION_HOST`. JSON conf file variable:
     * `mp_region_host`.
     * 
     */
    public Output<Optional<String>> mpRegionHost() {
        return Codegen.optional(this.mpRegionHost);
    }
    /**
     * (Used for the initial `sts assume role`) AWS PROFILE. Environment variable: `CLOUDNGFWAWS_PROFILE`. JSON conf file
     * variable: `profile`.
     * 
     */
    @Export(name="profile", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> profile;

    /**
     * @return (Used for the initial `sts assume role`) AWS PROFILE. Environment variable: `CLOUDNGFWAWS_PROFILE`. JSON conf file
     * variable: `profile`.
     * 
     */
    public Output<Optional<String>> profile() {
        return Codegen.optional(this.profile);
    }
    /**
     * The protocol (defaults to `https`). Environment variable: `CLOUDNGFWAWS_PROTOCOL`. JSON conf file variable: `protocol`.
     * Valid values are `https` or `http`.
     * 
     */
    @Export(name="protocol", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> protocol;

    /**
     * @return The protocol (defaults to `https`). Environment variable: `CLOUDNGFWAWS_PROTOCOL`. JSON conf file variable: `protocol`.
     * Valid values are `https` or `http`.
     * 
     */
    public Output<Optional<String>> protocol() {
        return Codegen.optional(this.protocol);
    }
    /**
     * AWS region. Environment variable: `CLOUDNGFWAWS_REGION`. JSON conf file variable: `region`.
     * 
     */
    @Export(name="region", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> region;

    /**
     * @return AWS region. Environment variable: `CLOUDNGFWAWS_REGION`. JSON conf file variable: `region`.
     * 
     */
    public Output<Optional<String>> region() {
        return Codegen.optional(this.region);
    }
    /**
     * (Used for the initial `sts assume role`) AWS secret key. Environment variable: `CLOUDNGFWAWS_SECRET_KEY`. JSON conf file
     * variable: `secret-key`.
     * 
     */
    @Export(name="secretKey", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> secretKey;

    /**
     * @return (Used for the initial `sts assume role`) AWS secret key. Environment variable: `CLOUDNGFWAWS_SECRET_KEY`. JSON conf file
     * variable: `secret-key`.
     * 
     */
    public Output<Optional<String>> secretKey() {
        return Codegen.optional(this.secretKey);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Provider(java.lang.String name) {
        this(name, ProviderArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Provider(java.lang.String name, @Nullable ProviderArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Provider(java.lang.String name, @Nullable ProviderArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("cloudngfwaws", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private static ProviderArgs makeArgs(@Nullable ProviderArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? ProviderArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<java.lang.String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

}
