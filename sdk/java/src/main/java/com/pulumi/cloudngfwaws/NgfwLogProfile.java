// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws;

import com.pulumi.cloudngfwaws.NgfwLogProfileArgs;
import com.pulumi.cloudngfwaws.Utilities;
import com.pulumi.cloudngfwaws.inputs.NgfwLogProfileState;
import com.pulumi.cloudngfwaws.outputs.NgfwLogProfileLogDestination;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Resource for NGFW log profile manipulation.
 * 
 * ## Admin Permission Type
 * 
 * * `Firewall`
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
 * import com.pulumi.aws.vpc;
 * import com.pulumi.aws.vpcArgs;
 * import com.pulumi.aws.subnet;
 * import com.pulumi.aws.subnetArgs;
 * import com.pulumi.cloudngfwaws.Ngfw;
 * import com.pulumi.cloudngfwaws.NgfwArgs;
 * import com.pulumi.cloudngfwaws.inputs.NgfwSubnetMappingArgs;
 * import com.pulumi.cloudngfwaws.NgfwLogProfile;
 * import com.pulumi.cloudngfwaws.NgfwLogProfileArgs;
 * import com.pulumi.cloudngfwaws.inputs.NgfwLogProfileLogDestinationArgs;
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
 *         var exampleVpc = new Vpc("exampleVpc", VpcArgs.builder()
 *             .cidrBlock("172.16.0.0/16")
 *             .tags(Map.of("name", "tf-example"))
 *             .build());
 * 
 *         var subnet1 = new Subnet("subnet1", SubnetArgs.builder()
 *             .vpcId(myVpc.id())
 *             .cidrBlock("172.16.10.0/24")
 *             .availabilityZone("us-west-2a")
 *             .tags(Map.of("name", "tf-example"))
 *             .build());
 * 
 *         var subnet2 = new Subnet("subnet2", SubnetArgs.builder()
 *             .vpcId(myVpc.id())
 *             .cidrBlock("172.16.20.0/24")
 *             .availabilityZone("us-west-2b")
 *             .tags(Map.of("name", "tf-example"))
 *             .build());
 * 
 *         var x = new Ngfw("x", NgfwArgs.builder()
 *             .name("example-instance")
 *             .vpcId(exampleVpc.id())
 *             .accountId("12345678")
 *             .description("Example description")
 *             .endpointMode("ServiceManaged")
 *             .subnetMappings(            
 *                 NgfwSubnetMappingArgs.builder()
 *                     .subnetId(subnet1.id())
 *                     .build(),
 *                 NgfwSubnetMappingArgs.builder()
 *                     .subnetId(subnet2.id())
 *                     .build())
 *             .rulestack("example-rulestack")
 *             .tags(Map.of("Foo", "bar"))
 *             .build());
 * 
 *         var example = new NgfwLogProfile("example", NgfwLogProfileArgs.builder()
 *             .ngfw(x.name())
 *             .accountId(x.accountId())
 *             .logDestinations(            
 *                 NgfwLogProfileLogDestinationArgs.builder()
 *                     .destinationType("S3")
 *                     .destination("my-s3-bucket")
 *                     .logType("TRAFFIC")
 *                     .build(),
 *                 NgfwLogProfileLogDestinationArgs.builder()
 *                     .destinationType("CloudWatchLogs")
 *                     .destination("panw-log-group")
 *                     .logType("THREAT")
 *                     .build())
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
 * import name is &lt;account_id&gt;:&lt;ngfw&gt;
 * 
 * ```sh
 * $ pulumi import cloudngfwaws:index/ngfwLogProfile:NgfwLogProfile example 12345678:example-instance
 * ```
 * 
 */
@ResourceType(type="cloudngfwaws:index/ngfwLogProfile:NgfwLogProfile")
public class NgfwLogProfile extends com.pulumi.resources.CustomResource {
    /**
     * The unique ID of the account.
     * 
     */
    @Export(name="accountId", refs={String.class}, tree="[0]")
    private Output<String> accountId;

    /**
     * @return The unique ID of the account.
     * 
     */
    public Output<String> accountId() {
        return this.accountId;
    }
    /**
     * Enable advanced threat logging.
     * 
     */
    @Export(name="advancedThreatLog", refs={Boolean.class}, tree="[0]")
    private Output</* @Nullable */ Boolean> advancedThreatLog;

    /**
     * @return Enable advanced threat logging.
     * 
     */
    public Output<Optional<Boolean>> advancedThreatLog() {
        return Codegen.optional(this.advancedThreatLog);
    }
    /**
     * The CloudWatch metric namespace.
     * 
     */
    @Export(name="cloudWatchMetricNamespace", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> cloudWatchMetricNamespace;

    /**
     * @return The CloudWatch metric namespace.
     * 
     */
    public Output<Optional<String>> cloudWatchMetricNamespace() {
        return Codegen.optional(this.cloudWatchMetricNamespace);
    }
    /**
     * Cloudwatch metric fields.
     * 
     */
    @Export(name="cloudwatchMetricFields", refs={List.class,String.class}, tree="[0,1]")
    private Output</* @Nullable */ List<String>> cloudwatchMetricFields;

    /**
     * @return Cloudwatch metric fields.
     * 
     */
    public Output<Optional<List<String>>> cloudwatchMetricFields() {
        return Codegen.optional(this.cloudwatchMetricFields);
    }
    /**
     * List of log destinations.
     * 
     */
    @Export(name="logDestinations", refs={List.class,NgfwLogProfileLogDestination.class}, tree="[0,1]")
    private Output<List<NgfwLogProfileLogDestination>> logDestinations;

    /**
     * @return List of log destinations.
     * 
     */
    public Output<List<NgfwLogProfileLogDestination>> logDestinations() {
        return this.logDestinations;
    }
    /**
     * The name of the NGFW.
     * 
     */
    @Export(name="ngfw", refs={String.class}, tree="[0]")
    private Output<String> ngfw;

    /**
     * @return The name of the NGFW.
     * 
     */
    public Output<String> ngfw() {
        return this.ngfw;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public NgfwLogProfile(java.lang.String name) {
        this(name, NgfwLogProfileArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public NgfwLogProfile(java.lang.String name, NgfwLogProfileArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public NgfwLogProfile(java.lang.String name, NgfwLogProfileArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("cloudngfwaws:index/ngfwLogProfile:NgfwLogProfile", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private NgfwLogProfile(java.lang.String name, Output<java.lang.String> id, @Nullable NgfwLogProfileState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("cloudngfwaws:index/ngfwLogProfile:NgfwLogProfile", name, state, makeResourceOptions(options, id), false);
    }

    private static NgfwLogProfileArgs makeArgs(NgfwLogProfileArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? NgfwLogProfileArgs.Empty : args;
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
    public static NgfwLogProfile get(java.lang.String name, Output<java.lang.String> id, @Nullable NgfwLogProfileState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new NgfwLogProfile(name, id, state, options);
    }
}
