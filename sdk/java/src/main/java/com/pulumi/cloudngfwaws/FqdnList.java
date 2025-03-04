// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws;

import com.pulumi.cloudngfwaws.FqdnListArgs;
import com.pulumi.cloudngfwaws.Utilities;
import com.pulumi.cloudngfwaws.inputs.FqdnListState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Resource for fqdn list manipulation.
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
 * import com.pulumi.cloudngfwaws.FqdnList;
 * import com.pulumi.cloudngfwaws.FqdnListArgs;
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
 *         var example = new FqdnList("example", FqdnListArgs.builder()
 *             .rulestack(r.name())
 *             .name("tf-fqdn-list")
 *             .description("Also configured by Terraform")
 *             .fqdnLists(            
 *                 "example.com",
 *                 "foobar.org")
 *             .auditComment("initial config")
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
 * import name is &lt;scope&gt;:&lt;rulestack&gt;:&lt;fqdn_list_name&gt;
 * 
 * ```sh
 * $ pulumi import cloudngfwaws:index/fqdnList:FqdnList example Local:terraform-rulestack:tf-fqdn-list
 * ```
 * 
 */
@ResourceType(type="cloudngfwaws:index/fqdnList:FqdnList")
public class FqdnList extends com.pulumi.resources.CustomResource {
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
     * The description.
     * 
     */
    @Export(name="description", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> description;

    /**
     * @return The description.
     * 
     */
    public Output<Optional<String>> description() {
        return Codegen.optional(this.description);
    }
    /**
     * The fqdn list.
     * 
     */
    @Export(name="fqdnLists", refs={List.class,String.class}, tree="[0,1]")
    private Output<List<String>> fqdnLists;

    /**
     * @return The fqdn list.
     * 
     */
    public Output<List<String>> fqdnLists() {
        return this.fqdnLists;
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
     * The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     * 
     */
    @Export(name="scope", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> scope;

    /**
     * @return The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     * 
     */
    public Output<Optional<String>> scope() {
        return Codegen.optional(this.scope);
    }
    /**
     * The update token.
     * 
     */
    @Export(name="updateToken", refs={String.class}, tree="[0]")
    private Output<String> updateToken;

    /**
     * @return The update token.
     * 
     */
    public Output<String> updateToken() {
        return this.updateToken;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public FqdnList(java.lang.String name) {
        this(name, FqdnListArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public FqdnList(java.lang.String name, FqdnListArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public FqdnList(java.lang.String name, FqdnListArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("cloudngfwaws:index/fqdnList:FqdnList", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private FqdnList(java.lang.String name, Output<java.lang.String> id, @Nullable FqdnListState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("cloudngfwaws:index/fqdnList:FqdnList", name, state, makeResourceOptions(options, id), false);
    }

    private static FqdnListArgs makeArgs(FqdnListArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? FqdnListArgs.Empty : args;
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
    public static FqdnList get(java.lang.String name, Output<java.lang.String> id, @Nullable FqdnListState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new FqdnList(name, id, state, options);
    }
}
