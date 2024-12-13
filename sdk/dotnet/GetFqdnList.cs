// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws
{
    public static class GetFqdnList
    {
        /// <summary>
        /// Data source for retrieving fqdn list information.
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
        ///     var example = CloudNgfwAws.GetFqdnList.Invoke(new()
        ///     {
        ///         Rulestack = r.Name,
        ///         Name = "foobar",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetFqdnListResult> InvokeAsync(GetFqdnListArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetFqdnListResult>("cloudngfwaws:index/getFqdnList:getFqdnList", args ?? new GetFqdnListArgs(), options.WithDefaults());

        /// <summary>
        /// Data source for retrieving fqdn list information.
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
        ///     var example = CloudNgfwAws.GetFqdnList.Invoke(new()
        ///     {
        ///         Rulestack = r.Name,
        ///         Name = "foobar",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetFqdnListResult> Invoke(GetFqdnListInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetFqdnListResult>("cloudngfwaws:index/getFqdnList:getFqdnList", args ?? new GetFqdnListInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// Data source for retrieving fqdn list information.
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
        ///     var example = CloudNgfwAws.GetFqdnList.Invoke(new()
        ///     {
        ///         Rulestack = r.Name,
        ///         Name = "foobar",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetFqdnListResult> Invoke(GetFqdnListInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetFqdnListResult>("cloudngfwaws:index/getFqdnList:getFqdnList", args ?? new GetFqdnListInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetFqdnListArgs : global::Pulumi.InvokeArgs
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

        public GetFqdnListArgs()
        {
        }
        public static new GetFqdnListArgs Empty => new GetFqdnListArgs();
    }

    public sealed class GetFqdnListInvokeArgs : global::Pulumi.InvokeArgs
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

        public GetFqdnListInvokeArgs()
        {
        }
        public static new GetFqdnListInvokeArgs Empty => new GetFqdnListInvokeArgs();
    }


    [OutputType]
    public sealed class GetFqdnListResult
    {
        /// <summary>
        /// The audit comment.
        /// </summary>
        public readonly string AuditComment;
        /// <summary>
        /// Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
        /// </summary>
        public readonly string? ConfigType;
        /// <summary>
        /// The description.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The fqdn list.
        /// </summary>
        public readonly ImmutableArray<string> FqdnLists;
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
        /// The update token.
        /// </summary>
        public readonly string UpdateToken;

        [OutputConstructor]
        private GetFqdnListResult(
            string auditComment,

            string? configType,

            string description,

            ImmutableArray<string> fqdnLists,

            string id,

            string name,

            string rulestack,

            string? scope,

            string updateToken)
        {
            AuditComment = auditComment;
            ConfigType = configType;
            Description = description;
            FqdnLists = fqdnLists;
            Id = id;
            Name = name;
            Rulestack = rulestack;
            Scope = scope;
            UpdateToken = updateToken;
        }
    }
}
