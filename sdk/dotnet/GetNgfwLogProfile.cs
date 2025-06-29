// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws
{
    public static class GetNgfwLogProfile
    {
        /// <summary>
        /// Data source for retrieving log profile information.
        /// 
        /// 
        /// ## Admin Permission Type
        /// 
        /// * `Firewall`
        /// 
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using CloudNgfwAws = Pulumi.CloudNgfwAws;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = CloudNgfwAws.GetNgfwLogProfile.Invoke(new()
        ///     {
        ///         Ngfw = "example-instance",
        ///         AccountId = "123456789",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetNgfwLogProfileResult> InvokeAsync(GetNgfwLogProfileArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNgfwLogProfileResult>("cloudngfwaws:index/getNgfwLogProfile:getNgfwLogProfile", args ?? new GetNgfwLogProfileArgs(), options.WithDefaults());

        /// <summary>
        /// Data source for retrieving log profile information.
        /// 
        /// 
        /// ## Admin Permission Type
        /// 
        /// * `Firewall`
        /// 
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using CloudNgfwAws = Pulumi.CloudNgfwAws;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = CloudNgfwAws.GetNgfwLogProfile.Invoke(new()
        ///     {
        ///         Ngfw = "example-instance",
        ///         AccountId = "123456789",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetNgfwLogProfileResult> Invoke(GetNgfwLogProfileInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNgfwLogProfileResult>("cloudngfwaws:index/getNgfwLogProfile:getNgfwLogProfile", args ?? new GetNgfwLogProfileInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// Data source for retrieving log profile information.
        /// 
        /// 
        /// ## Admin Permission Type
        /// 
        /// * `Firewall`
        /// 
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using CloudNgfwAws = Pulumi.CloudNgfwAws;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = CloudNgfwAws.GetNgfwLogProfile.Invoke(new()
        ///     {
        ///         Ngfw = "example-instance",
        ///         AccountId = "123456789",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetNgfwLogProfileResult> Invoke(GetNgfwLogProfileInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetNgfwLogProfileResult>("cloudngfwaws:index/getNgfwLogProfile:getNgfwLogProfile", args ?? new GetNgfwLogProfileInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNgfwLogProfileArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique ID of the account.
        /// </summary>
        [Input("accountId", required: true)]
        public string AccountId { get; set; } = null!;

        /// <summary>
        /// The name of the NGFW.
        /// </summary>
        [Input("ngfw", required: true)]
        public string Ngfw { get; set; } = null!;

        public GetNgfwLogProfileArgs()
        {
        }
        public static new GetNgfwLogProfileArgs Empty => new GetNgfwLogProfileArgs();
    }

    public sealed class GetNgfwLogProfileInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique ID of the account.
        /// </summary>
        [Input("accountId", required: true)]
        public Input<string> AccountId { get; set; } = null!;

        /// <summary>
        /// The name of the NGFW.
        /// </summary>
        [Input("ngfw", required: true)]
        public Input<string> Ngfw { get; set; } = null!;

        public GetNgfwLogProfileInvokeArgs()
        {
        }
        public static new GetNgfwLogProfileInvokeArgs Empty => new GetNgfwLogProfileInvokeArgs();
    }


    [OutputType]
    public sealed class GetNgfwLogProfileResult
    {
        /// <summary>
        /// The unique ID of the account.
        /// </summary>
        public readonly string AccountId;
        /// <summary>
        /// Enable advanced threat logging.
        /// </summary>
        public readonly bool AdvancedThreatLog;
        /// <summary>
        /// The CloudWatch metric namespace.
        /// </summary>
        public readonly string CloudWatchMetricNamespace;
        /// <summary>
        /// Cloudwatch metric fields.
        /// </summary>
        public readonly ImmutableArray<string> CloudwatchMetricFields;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// List of log destinations.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNgfwLogProfileLogDestinationResult> LogDestinations;
        /// <summary>
        /// The name of the NGFW.
        /// </summary>
        public readonly string Ngfw;

        [OutputConstructor]
        private GetNgfwLogProfileResult(
            string accountId,

            bool advancedThreatLog,

            string cloudWatchMetricNamespace,

            ImmutableArray<string> cloudwatchMetricFields,

            string id,

            ImmutableArray<Outputs.GetNgfwLogProfileLogDestinationResult> logDestinations,

            string ngfw)
        {
            AccountId = accountId;
            AdvancedThreatLog = advancedThreatLog;
            CloudWatchMetricNamespace = cloudWatchMetricNamespace;
            CloudwatchMetricFields = cloudwatchMetricFields;
            Id = id;
            LogDestinations = logDestinations;
            Ngfw = ngfw;
        }
    }
}
