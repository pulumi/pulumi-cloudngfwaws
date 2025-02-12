// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws;

import com.pulumi.cloudngfwaws.PredefinedUrlCategoryOverrideArgs;
import com.pulumi.cloudngfwaws.Utilities;
import com.pulumi.cloudngfwaws.inputs.PredefinedUrlCategoryOverrideState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Resource for predefined URL category override management.
 * 
 * ## Admin Permission Type
 * 
 * * `Rulestack` (for `scope=&#34;Local&#34;`)
 * * `Global Rulestack` (for `scope=&#34;Global&#34;`)
 * 
 * ## Example Usage
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.cloudngfwaws.Rulestack;
 * import com.pulumi.cloudngfwaws.RulestackArgs;
 * import com.pulumi.cloudngfwaws.inputs.RulestackProfileConfigArgs;
 * import com.pulumi.cloudngfwaws.PredefinedUrlCategoryOverride;
 * import com.pulumi.cloudngfwaws.PredefinedUrlCategoryOverrideArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var r = new Rulestack("r", RulestackArgs.builder()
 *             .name("terraform-rulestack")
 *             .scope("Local")
 *             .accountId("123456789")
 *             .description("Made by Pulumi")
 *             .profileConfig(RulestackProfileConfigArgs.builder()
 *                 .antiSpyware("BestPractice")
 *                 .build())
 *             .build());
 * 
 *         var example = new PredefinedUrlCategoryOverride("example", PredefinedUrlCategoryOverrideArgs.builder()
 *             .rulestack(r.name())
 *             .name("foobar")
 *             .action("block")
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ## Import
 * 
 * import name is &lt;rulestack&gt;:&lt;predefined_url_category_override_name&gt;
 * 
 * ```sh
 * $ pulumi import cloudngfwaws:index/predefinedUrlCategoryOverride:PredefinedUrlCategoryOverride example terraform-rulestack:foobar
 * ```
 * 
 */
@ResourceType(type="cloudngfwaws:index/predefinedUrlCategoryOverride:PredefinedUrlCategoryOverride")
public class PredefinedUrlCategoryOverride extends com.pulumi.resources.CustomResource {
    /**
     * The action to take. Valid values are `none`, `allow`, `alert`, or `block`. Defaults to `none`.
     * 
     */
    @Export(name="action", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> action;

    /**
     * @return The action to take. Valid values are `none`, `allow`, `alert`, or `block`. Defaults to `none`.
     * 
     */
    public Output<Optional<String>> action() {
        return Codegen.optional(this.action);
    }
    /**
     * The audit comment.
     * 
     */
    @Export(name="auditComment", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> auditComment;

    /**
     * @return The audit comment.
     * 
     */
    public Output<Optional<String>> auditComment() {
        return Codegen.optional(this.auditComment);
    }
    /**
     * The name.
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return The name.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * The rulestack.
     * 
     */
    @Export(name="rulestack", refs={String.class}, tree="[0]")
    private Output<String> rulestack;

    /**
     * @return The rulestack.
     * 
     */
    public Output<String> rulestack() {
        return this.rulestack;
    }
    /**
     * Update token.
     * 
     */
    @Export(name="updateToken", refs={String.class}, tree="[0]")
    private Output<String> updateToken;

    /**
     * @return Update token.
     * 
     */
    public Output<String> updateToken() {
        return this.updateToken;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public PredefinedUrlCategoryOverride(java.lang.String name) {
        this(name, PredefinedUrlCategoryOverrideArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public PredefinedUrlCategoryOverride(java.lang.String name, PredefinedUrlCategoryOverrideArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public PredefinedUrlCategoryOverride(java.lang.String name, PredefinedUrlCategoryOverrideArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("cloudngfwaws:index/predefinedUrlCategoryOverride:PredefinedUrlCategoryOverride", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private PredefinedUrlCategoryOverride(java.lang.String name, Output<java.lang.String> id, @Nullable PredefinedUrlCategoryOverrideState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("cloudngfwaws:index/predefinedUrlCategoryOverride:PredefinedUrlCategoryOverride", name, state, makeResourceOptions(options, id), false);
    }

    private static PredefinedUrlCategoryOverrideArgs makeArgs(PredefinedUrlCategoryOverrideArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? PredefinedUrlCategoryOverrideArgs.Empty : args;
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
    public static PredefinedUrlCategoryOverride get(java.lang.String name, Output<java.lang.String> id, @Nullable PredefinedUrlCategoryOverrideState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new PredefinedUrlCategoryOverride(name, id, state, options);
    }
}
