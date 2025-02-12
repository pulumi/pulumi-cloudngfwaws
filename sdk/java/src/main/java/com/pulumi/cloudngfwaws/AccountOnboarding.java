// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws;

import com.pulumi.cloudngfwaws.AccountOnboardingArgs;
import com.pulumi.cloudngfwaws.Utilities;
import com.pulumi.cloudngfwaws.inputs.AccountOnboardingState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import javax.annotation.Nullable;

/**
 * Resource for Account Onboarding.
 * 
 * ## Admin Permission Type
 * 
 * * `Rulestack` (for `scope=&#34;Local&#34;`)
 * * `Global Rulestack` (for `scope=&#34;Global&#34;`)
 * 
 */
@ResourceType(type="cloudngfwaws:index/accountOnboarding:AccountOnboarding")
public class AccountOnboarding extends com.pulumi.resources.CustomResource {
    /**
     * The account IDs
     * 
     */
    @Export(name="accountId", refs={String.class}, tree="[0]")
    private Output<String> accountId;

    /**
     * @return The account IDs
     * 
     */
    public Output<String> accountId() {
        return this.accountId;
    }
    /**
     * Onboarding status of the account
     * 
     */
    @Export(name="onboardingStatus", refs={String.class}, tree="[0]")
    private Output<String> onboardingStatus;

    /**
     * @return Onboarding status of the account
     * 
     */
    public Output<String> onboardingStatus() {
        return this.onboardingStatus;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public AccountOnboarding(java.lang.String name) {
        this(name, AccountOnboardingArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public AccountOnboarding(java.lang.String name, AccountOnboardingArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public AccountOnboarding(java.lang.String name, AccountOnboardingArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("cloudngfwaws:index/accountOnboarding:AccountOnboarding", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private AccountOnboarding(java.lang.String name, Output<java.lang.String> id, @Nullable AccountOnboardingState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("cloudngfwaws:index/accountOnboarding:AccountOnboarding", name, state, makeResourceOptions(options, id), false);
    }

    private static AccountOnboardingArgs makeArgs(AccountOnboardingArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? AccountOnboardingArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<java.lang.String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .pluginDownloadURL("github://api.github.com/pulumi/pulumi-cloudngfwaws")
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static AccountOnboarding get(java.lang.String name, Output<java.lang.String> id, @Nullable AccountOnboardingState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new AccountOnboarding(name, id, state, options);
    }
}
