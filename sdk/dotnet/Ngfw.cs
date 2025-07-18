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
    ///     var rs = new CloudNgfwAws.CommitRulestack("rs", new()
    ///     {
    ///         Rulestack = "my-rulestack",
    ///     });
    /// 
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
    ///     var example = new CloudNgfwAws.Ngfw("example", new()
    ///     {
    ///         Name = "example-instance",
    ///         VpcId = exampleVpc.Id,
    ///         AccountId = "12345678",
    ///         Description = "Example description",
    ///         LinkId = "Link-81e80ccc-357a-4e4e-8325-1ed1d830cba5",
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
    ///         Rulestack = rs.Rulestack,
    ///         Tags = 
    ///         {
    ///             { "Foo", "bar" },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// import name is &lt;account_id&gt;:&lt;name&gt;
    /// 
    /// ```sh
    /// $ pulumi import cloudngfwaws:index/ngfw:Ngfw example 12345678:example-instance
    /// ```
    /// </summary>
    [CloudNgfwAwsResourceType("cloudngfwaws:index/ngfw:Ngfw")]
    public partial class Ngfw : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The account ID. This field is mandatory if using multiple accounts.
        /// </summary>
        [Output("accountId")]
        public Output<string?> AccountId { get; private set; } = null!;

        /// <summary>
        /// App-ID version number.
        /// </summary>
        [Output("appIdVersion")]
        public Output<string> AppIdVersion { get; private set; } = null!;

        /// <summary>
        /// Automatic App-ID upgrade version number. Defaults to `true`.
        /// </summary>
        [Output("automaticUpgradeAppIdVersion")]
        public Output<bool?> AutomaticUpgradeAppIdVersion { get; private set; } = null!;

        /// <summary>
        /// The description.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
        /// </summary>
        [Output("endpointMode")]
        public Output<string> EndpointMode { get; private set; } = null!;

        /// <summary>
        /// The endpoint service name.
        /// </summary>
        [Output("endpointServiceName")]
        public Output<string> EndpointServiceName { get; private set; } = null!;

        /// <summary>
        /// The Id of the NGFW.
        /// </summary>
        [Output("firewallId")]
        public Output<string> FirewallId { get; private set; } = null!;

        /// <summary>
        /// The global rulestack for this NGFW.
        /// </summary>
        [Output("globalRulestack")]
        public Output<string?> GlobalRulestack { get; private set; } = null!;

        /// <summary>
        /// A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
        /// </summary>
        [Output("linkId")]
        public Output<string> LinkId { get; private set; } = null!;

        /// <summary>
        /// The link status.
        /// </summary>
        [Output("linkStatus")]
        public Output<string> LinkStatus { get; private set; } = null!;

        /// <summary>
        /// Share NGFW with Multiple VPCs. This feature can be enabled only if the endpoint_mode is CustomerManaged.
        /// </summary>
        [Output("multiVpc")]
        public Output<bool> MultiVpc { get; private set; } = null!;

        /// <summary>
        /// The NGFW name.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The rulestack for this NGFW.
        /// </summary>
        [Output("rulestack")]
        public Output<string?> Rulestack { get; private set; } = null!;

        [Output("statuses")]
        public Output<ImmutableArray<Outputs.NgfwStatus>> Statuses { get; private set; } = null!;

        /// <summary>
        /// Subnet mappings.
        /// </summary>
        [Output("subnetMappings")]
        public Output<ImmutableArray<Outputs.NgfwSubnetMapping>> SubnetMappings { get; private set; } = null!;

        /// <summary>
        /// The tags.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        /// <summary>
        /// The update token.
        /// </summary>
        [Output("updateToken")]
        public Output<string> UpdateToken { get; private set; } = null!;

        /// <summary>
        /// The vpc id.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a Ngfw resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Ngfw(string name, NgfwArgs args, CustomResourceOptions? options = null)
            : base("cloudngfwaws:index/ngfw:Ngfw", name, args ?? new NgfwArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Ngfw(string name, Input<string> id, NgfwState? state = null, CustomResourceOptions? options = null)
            : base("cloudngfwaws:index/ngfw:Ngfw", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Ngfw resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Ngfw Get(string name, Input<string> id, NgfwState? state = null, CustomResourceOptions? options = null)
        {
            return new Ngfw(name, id, state, options);
        }
    }

    public sealed class NgfwArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The account ID. This field is mandatory if using multiple accounts.
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// App-ID version number.
        /// </summary>
        [Input("appIdVersion")]
        public Input<string>? AppIdVersion { get; set; }

        /// <summary>
        /// Automatic App-ID upgrade version number. Defaults to `true`.
        /// </summary>
        [Input("automaticUpgradeAppIdVersion")]
        public Input<bool>? AutomaticUpgradeAppIdVersion { get; set; }

        /// <summary>
        /// The description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
        /// </summary>
        [Input("endpointMode", required: true)]
        public Input<string> EndpointMode { get; set; } = null!;

        /// <summary>
        /// The global rulestack for this NGFW.
        /// </summary>
        [Input("globalRulestack")]
        public Input<string>? GlobalRulestack { get; set; }

        /// <summary>
        /// A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
        /// </summary>
        [Input("linkId")]
        public Input<string>? LinkId { get; set; }

        /// <summary>
        /// Share NGFW with Multiple VPCs. This feature can be enabled only if the endpoint_mode is CustomerManaged.
        /// </summary>
        [Input("multiVpc")]
        public Input<bool>? MultiVpc { get; set; }

        /// <summary>
        /// The NGFW name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The rulestack for this NGFW.
        /// </summary>
        [Input("rulestack")]
        public Input<string>? Rulestack { get; set; }

        [Input("subnetMappings", required: true)]
        private InputList<Inputs.NgfwSubnetMappingArgs>? _subnetMappings;

        /// <summary>
        /// Subnet mappings.
        /// </summary>
        public InputList<Inputs.NgfwSubnetMappingArgs> SubnetMappings
        {
            get => _subnetMappings ?? (_subnetMappings = new InputList<Inputs.NgfwSubnetMappingArgs>());
            set => _subnetMappings = value;
        }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// The tags.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The vpc id.
        /// </summary>
        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public NgfwArgs()
        {
        }
        public static new NgfwArgs Empty => new NgfwArgs();
    }

    public sealed class NgfwState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The account ID. This field is mandatory if using multiple accounts.
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// App-ID version number.
        /// </summary>
        [Input("appIdVersion")]
        public Input<string>? AppIdVersion { get; set; }

        /// <summary>
        /// Automatic App-ID upgrade version number. Defaults to `true`.
        /// </summary>
        [Input("automaticUpgradeAppIdVersion")]
        public Input<bool>? AutomaticUpgradeAppIdVersion { get; set; }

        /// <summary>
        /// The description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
        /// </summary>
        [Input("endpointMode")]
        public Input<string>? EndpointMode { get; set; }

        /// <summary>
        /// The endpoint service name.
        /// </summary>
        [Input("endpointServiceName")]
        public Input<string>? EndpointServiceName { get; set; }

        /// <summary>
        /// The Id of the NGFW.
        /// </summary>
        [Input("firewallId")]
        public Input<string>? FirewallId { get; set; }

        /// <summary>
        /// The global rulestack for this NGFW.
        /// </summary>
        [Input("globalRulestack")]
        public Input<string>? GlobalRulestack { get; set; }

        /// <summary>
        /// A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
        /// </summary>
        [Input("linkId")]
        public Input<string>? LinkId { get; set; }

        /// <summary>
        /// The link status.
        /// </summary>
        [Input("linkStatus")]
        public Input<string>? LinkStatus { get; set; }

        /// <summary>
        /// Share NGFW with Multiple VPCs. This feature can be enabled only if the endpoint_mode is CustomerManaged.
        /// </summary>
        [Input("multiVpc")]
        public Input<bool>? MultiVpc { get; set; }

        /// <summary>
        /// The NGFW name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The rulestack for this NGFW.
        /// </summary>
        [Input("rulestack")]
        public Input<string>? Rulestack { get; set; }

        [Input("statuses")]
        private InputList<Inputs.NgfwStatusGetArgs>? _statuses;
        public InputList<Inputs.NgfwStatusGetArgs> Statuses
        {
            get => _statuses ?? (_statuses = new InputList<Inputs.NgfwStatusGetArgs>());
            set => _statuses = value;
        }

        [Input("subnetMappings")]
        private InputList<Inputs.NgfwSubnetMappingGetArgs>? _subnetMappings;

        /// <summary>
        /// Subnet mappings.
        /// </summary>
        public InputList<Inputs.NgfwSubnetMappingGetArgs> SubnetMappings
        {
            get => _subnetMappings ?? (_subnetMappings = new InputList<Inputs.NgfwSubnetMappingGetArgs>());
            set => _subnetMappings = value;
        }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// The tags.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The update token.
        /// </summary>
        [Input("updateToken")]
        public Input<string>? UpdateToken { get; set; }

        /// <summary>
        /// The vpc id.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public NgfwState()
        {
        }
        public static new NgfwState Empty => new NgfwState();
    }
}
