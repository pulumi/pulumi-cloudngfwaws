// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws
{
    /// <summary>
    /// Resource for NGFW log profile manipulation.
    /// 
    /// ## Admin Permission Type
    /// 
    /// * `Firewall`
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// using CloudNgfwAws = Pulumi.CloudNgfwAws;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleVpc = new Aws.Index.Vpc("example", new()
    ///     {
    ///         CidrBlock = "172.16.0.0/16",
    ///         Tags = 
    ///         {
    ///             { "name", "tf-example" },
    ///         },
    ///     });
    /// 
    ///     var subnet1 = new Aws.Index.Subnet("subnet1", new()
    ///     {
    ///         VpcId = myVpc.Id,
    ///         CidrBlock = "172.16.10.0/24",
    ///         AvailabilityZone = "us-west-2a",
    ///         Tags = 
    ///         {
    ///             { "name", "tf-example" },
    ///         },
    ///     });
    /// 
    ///     var subnet2 = new Aws.Index.Subnet("subnet2", new()
    ///     {
    ///         VpcId = myVpc.Id,
    ///         CidrBlock = "172.16.20.0/24",
    ///         AvailabilityZone = "us-west-2b",
    ///         Tags = 
    ///         {
    ///             { "name", "tf-example" },
    ///         },
    ///     });
    /// 
    ///     var x = new CloudNgfwAws.Ngfw("x", new()
    ///     {
    ///         Name = "example-instance",
    ///         VpcId = exampleVpc.Id,
    ///         AccountId = "12345678",
    ///         Description = "Example description",
    ///         EndpointMode = "ServiceManaged",
    ///         SubnetMappings = new[]
    ///         {
    ///             new CloudNgfwAws.Inputs.NgfwSubnetMappingArgs
    ///             {
    ///                 SubnetId = subnet1.Id,
    ///             },
    ///             new CloudNgfwAws.Inputs.NgfwSubnetMappingArgs
    ///             {
    ///                 SubnetId = subnet2.Id,
    ///             },
    ///         },
    ///         Rulestack = "example-rulestack",
    ///         Tags = 
    ///         {
    ///             { "Foo", "bar" },
    ///         },
    ///     });
    /// 
    ///     var example = new CloudNgfwAws.NgfwLogProfile("example", new()
    ///     {
    ///         Ngfw = x.Name,
    ///         AccountId = x.AccountId,
    ///         LogDestinations = new[]
    ///         {
    ///             new CloudNgfwAws.Inputs.NgfwLogProfileLogDestinationArgs
    ///             {
    ///                 DestinationType = "S3",
    ///                 Destination = "my-s3-bucket",
    ///                 LogType = "TRAFFIC",
    ///             },
    ///             new CloudNgfwAws.Inputs.NgfwLogProfileLogDestinationArgs
    ///             {
    ///                 DestinationType = "CloudWatchLogs",
    ///                 Destination = "panw-log-group",
    ///                 LogType = "THREAT",
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// import name is &lt;account_id&gt;:&lt;ngfw&gt;
    /// 
    /// ```sh
    /// $ pulumi import cloudngfwaws:index/ngfwLogProfile:NgfwLogProfile example 12345678:example-instance
    /// ```
    /// </summary>
    [CloudNgfwAwsResourceType("cloudngfwaws:index/ngfwLogProfile:NgfwLogProfile")]
    public partial class NgfwLogProfile : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The unique ID of the account.
        /// </summary>
        [Output("accountId")]
        public Output<string> AccountId { get; private set; } = null!;

        /// <summary>
        /// Enable advanced threat logging.
        /// </summary>
        [Output("advancedThreatLog")]
        public Output<bool?> AdvancedThreatLog { get; private set; } = null!;

        /// <summary>
        /// The CloudWatch metric namespace.
        /// </summary>
        [Output("cloudWatchMetricNamespace")]
        public Output<string?> CloudWatchMetricNamespace { get; private set; } = null!;

        /// <summary>
        /// Cloudwatch metric fields.
        /// </summary>
        [Output("cloudwatchMetricFields")]
        public Output<ImmutableArray<string>> CloudwatchMetricFields { get; private set; } = null!;

        /// <summary>
        /// List of log destinations.
        /// </summary>
        [Output("logDestinations")]
        public Output<ImmutableArray<Outputs.NgfwLogProfileLogDestination>> LogDestinations { get; private set; } = null!;

        /// <summary>
        /// The name of the NGFW.
        /// </summary>
        [Output("ngfw")]
        public Output<string> Ngfw { get; private set; } = null!;


        /// <summary>
        /// Create a NgfwLogProfile resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NgfwLogProfile(string name, NgfwLogProfileArgs args, CustomResourceOptions? options = null)
            : base("cloudngfwaws:index/ngfwLogProfile:NgfwLogProfile", name, args ?? new NgfwLogProfileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NgfwLogProfile(string name, Input<string> id, NgfwLogProfileState? state = null, CustomResourceOptions? options = null)
            : base("cloudngfwaws:index/ngfwLogProfile:NgfwLogProfile", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumi/pulumi-cloudngfwaws",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing NgfwLogProfile resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NgfwLogProfile Get(string name, Input<string> id, NgfwLogProfileState? state = null, CustomResourceOptions? options = null)
        {
            return new NgfwLogProfile(name, id, state, options);
        }
    }

    public sealed class NgfwLogProfileArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The unique ID of the account.
        /// </summary>
        [Input("accountId", required: true)]
        public Input<string> AccountId { get; set; } = null!;

        /// <summary>
        /// Enable advanced threat logging.
        /// </summary>
        [Input("advancedThreatLog")]
        public Input<bool>? AdvancedThreatLog { get; set; }

        /// <summary>
        /// The CloudWatch metric namespace.
        /// </summary>
        [Input("cloudWatchMetricNamespace")]
        public Input<string>? CloudWatchMetricNamespace { get; set; }

        [Input("cloudwatchMetricFields")]
        private InputList<string>? _cloudwatchMetricFields;

        /// <summary>
        /// Cloudwatch metric fields.
        /// </summary>
        public InputList<string> CloudwatchMetricFields
        {
            get => _cloudwatchMetricFields ?? (_cloudwatchMetricFields = new InputList<string>());
            set => _cloudwatchMetricFields = value;
        }

        [Input("logDestinations", required: true)]
        private InputList<Inputs.NgfwLogProfileLogDestinationArgs>? _logDestinations;

        /// <summary>
        /// List of log destinations.
        /// </summary>
        public InputList<Inputs.NgfwLogProfileLogDestinationArgs> LogDestinations
        {
            get => _logDestinations ?? (_logDestinations = new InputList<Inputs.NgfwLogProfileLogDestinationArgs>());
            set => _logDestinations = value;
        }

        /// <summary>
        /// The name of the NGFW.
        /// </summary>
        [Input("ngfw", required: true)]
        public Input<string> Ngfw { get; set; } = null!;

        public NgfwLogProfileArgs()
        {
        }
        public static new NgfwLogProfileArgs Empty => new NgfwLogProfileArgs();
    }

    public sealed class NgfwLogProfileState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The unique ID of the account.
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// Enable advanced threat logging.
        /// </summary>
        [Input("advancedThreatLog")]
        public Input<bool>? AdvancedThreatLog { get; set; }

        /// <summary>
        /// The CloudWatch metric namespace.
        /// </summary>
        [Input("cloudWatchMetricNamespace")]
        public Input<string>? CloudWatchMetricNamespace { get; set; }

        [Input("cloudwatchMetricFields")]
        private InputList<string>? _cloudwatchMetricFields;

        /// <summary>
        /// Cloudwatch metric fields.
        /// </summary>
        public InputList<string> CloudwatchMetricFields
        {
            get => _cloudwatchMetricFields ?? (_cloudwatchMetricFields = new InputList<string>());
            set => _cloudwatchMetricFields = value;
        }

        [Input("logDestinations")]
        private InputList<Inputs.NgfwLogProfileLogDestinationGetArgs>? _logDestinations;

        /// <summary>
        /// List of log destinations.
        /// </summary>
        public InputList<Inputs.NgfwLogProfileLogDestinationGetArgs> LogDestinations
        {
            get => _logDestinations ?? (_logDestinations = new InputList<Inputs.NgfwLogProfileLogDestinationGetArgs>());
            set => _logDestinations = value;
        }

        /// <summary>
        /// The name of the NGFW.
        /// </summary>
        [Input("ngfw")]
        public Input<string>? Ngfw { get; set; }

        public NgfwLogProfileState()
        {
        }
        public static new NgfwLogProfileState Empty => new NgfwLogProfileState();
    }
}
