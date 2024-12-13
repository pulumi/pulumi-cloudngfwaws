// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws
{
    public static class GetIntelligentFeed
    {
        /// <summary>
        /// Data source for retrieving intelligent feed information.
        /// 
        /// 
        /// ## Admin Permission Type
        /// 
        /// * `Rulestack` (for `scope="Local"`)
        /// * `Global Rulestack` (for `scope="Global"`)
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
        ///     var r = new CloudNgfwAws.Rulestack("r", new()
        ///     {
        ///         Name = "my-rulestack",
        ///         Scope = "Local",
        ///         AccountId = "12345",
        ///         Description = "Made by Pulumi",
        ///         ProfileConfig = new CloudNgfwAws.Inputs.RulestackProfileConfigArgs
        ///         {
        ///             AntiSpyware = "BestPractice",
        ///         },
        ///     });
        /// 
        ///     var example = CloudNgfwAws.GetIntelligentFeed.Invoke(new()
        ///     {
        ///         Rulestack = r.Name,
        ///         Name = "foobar",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetIntelligentFeedResult> InvokeAsync(GetIntelligentFeedArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetIntelligentFeedResult>("cloudngfwaws:index/getIntelligentFeed:getIntelligentFeed", args ?? new GetIntelligentFeedArgs(), options.WithDefaults());

        /// <summary>
        /// Data source for retrieving intelligent feed information.
        /// 
        /// 
        /// ## Admin Permission Type
        /// 
        /// * `Rulestack` (for `scope="Local"`)
        /// * `Global Rulestack` (for `scope="Global"`)
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
        ///     var r = new CloudNgfwAws.Rulestack("r", new()
        ///     {
        ///         Name = "my-rulestack",
        ///         Scope = "Local",
        ///         AccountId = "12345",
        ///         Description = "Made by Pulumi",
        ///         ProfileConfig = new CloudNgfwAws.Inputs.RulestackProfileConfigArgs
        ///         {
        ///             AntiSpyware = "BestPractice",
        ///         },
        ///     });
        /// 
        ///     var example = CloudNgfwAws.GetIntelligentFeed.Invoke(new()
        ///     {
        ///         Rulestack = r.Name,
        ///         Name = "foobar",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetIntelligentFeedResult> Invoke(GetIntelligentFeedInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetIntelligentFeedResult>("cloudngfwaws:index/getIntelligentFeed:getIntelligentFeed", args ?? new GetIntelligentFeedInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// Data source for retrieving intelligent feed information.
        /// 
        /// 
        /// ## Admin Permission Type
        /// 
        /// * `Rulestack` (for `scope="Local"`)
        /// * `Global Rulestack` (for `scope="Global"`)
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
        ///     var r = new CloudNgfwAws.Rulestack("r", new()
        ///     {
        ///         Name = "my-rulestack",
        ///         Scope = "Local",
        ///         AccountId = "12345",
        ///         Description = "Made by Pulumi",
        ///         ProfileConfig = new CloudNgfwAws.Inputs.RulestackProfileConfigArgs
        ///         {
        ///             AntiSpyware = "BestPractice",
        ///         },
        ///     });
        /// 
        ///     var example = CloudNgfwAws.GetIntelligentFeed.Invoke(new()
        ///     {
        ///         Rulestack = r.Name,
        ///         Name = "foobar",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetIntelligentFeedResult> Invoke(GetIntelligentFeedInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetIntelligentFeedResult>("cloudngfwaws:index/getIntelligentFeed:getIntelligentFeed", args ?? new GetIntelligentFeedInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetIntelligentFeedArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
        /// </summary>
        [Input("configType")]
        public string? ConfigType { get; set; }

        /// <summary>
        /// The name.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The rulestack.
        /// </summary>
        [Input("rulestack", required: true)]
        public string Rulestack { get; set; } = null!;

        /// <summary>
        /// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        /// </summary>
        [Input("scope")]
        public string? Scope { get; set; }

        public GetIntelligentFeedArgs()
        {
        }
        public static new GetIntelligentFeedArgs Empty => new GetIntelligentFeedArgs();
    }

    public sealed class GetIntelligentFeedInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
        /// </summary>
        [Input("configType")]
        public Input<string>? ConfigType { get; set; }

        /// <summary>
        /// The name.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The rulestack.
        /// </summary>
        [Input("rulestack", required: true)]
        public Input<string> Rulestack { get; set; } = null!;

        /// <summary>
        /// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        /// </summary>
        [Input("scope")]
        public Input<string>? Scope { get; set; }

        public GetIntelligentFeedInvokeArgs()
        {
        }
        public static new GetIntelligentFeedInvokeArgs Empty => new GetIntelligentFeedInvokeArgs();
    }


    [OutputType]
    public sealed class GetIntelligentFeedResult
    {
        /// <summary>
        /// The audit comment.
        /// </summary>
        public readonly string AuditComment;
        /// <summary>
        /// The certificate profile.
        /// </summary>
        public readonly string Certificate;
        /// <summary>
        /// Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
        /// </summary>
        public readonly string? ConfigType;
        /// <summary>
        /// The description.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Update frequency. Valid values are `HOURLY` or `DAILY`.
        /// </summary>
        public readonly string Frequency;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The rulestack.
        /// </summary>
        public readonly string Rulestack;
        /// <summary>
        /// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
        /// </summary>
        public readonly string? Scope;
        /// <summary>
        /// The time to poll for updates if frequency is daily. The number must be between [0, 23] incluside.
        /// </summary>
        public readonly int Time;
        /// <summary>
        /// The intelligent feed type. Valid values are `IP_LIST` or `URL_LIST`.
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// The update token.
        /// </summary>
        public readonly string UpdateToken;
        /// <summary>
        /// The intelligent feed source.
        /// </summary>
        public readonly string Url;

        [OutputConstructor]
        private GetIntelligentFeedResult(
            string auditComment,

            string certificate,

            string? configType,

            string description,

            string frequency,

            string id,

            string name,

            string rulestack,

            string? scope,

            int time,

            string type,

            string updateToken,

            string url)
        {
            AuditComment = auditComment;
            Certificate = certificate;
            ConfigType = configType;
            Description = description;
            Frequency = frequency;
            Id = id;
            Name = name;
            Rulestack = rulestack;
            Scope = scope;
            Time = time;
            Type = type;
            UpdateToken = updateToken;
            Url = url;
        }
    }
}
