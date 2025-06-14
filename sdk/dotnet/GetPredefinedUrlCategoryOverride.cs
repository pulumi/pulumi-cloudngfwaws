// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws
{
    public static class GetPredefinedUrlCategoryOverride
    {
        /// <summary>
        /// Data source for retrieving a predefined URL category override.
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
        ///     var example = CloudNgfwAws.GetPredefinedUrlCategoryOverride.Invoke(new()
        ///     {
        ///         Rulestack = r.Name,
        ///         Name = "foobar",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetPredefinedUrlCategoryOverrideResult> InvokeAsync(GetPredefinedUrlCategoryOverrideArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPredefinedUrlCategoryOverrideResult>("cloudngfwaws:index/getPredefinedUrlCategoryOverride:getPredefinedUrlCategoryOverride", args ?? new GetPredefinedUrlCategoryOverrideArgs(), options.WithDefaults());

        /// <summary>
        /// Data source for retrieving a predefined URL category override.
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
        ///     var example = CloudNgfwAws.GetPredefinedUrlCategoryOverride.Invoke(new()
        ///     {
        ///         Rulestack = r.Name,
        ///         Name = "foobar",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetPredefinedUrlCategoryOverrideResult> Invoke(GetPredefinedUrlCategoryOverrideInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPredefinedUrlCategoryOverrideResult>("cloudngfwaws:index/getPredefinedUrlCategoryOverride:getPredefinedUrlCategoryOverride", args ?? new GetPredefinedUrlCategoryOverrideInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// Data source for retrieving a predefined URL category override.
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
        ///     var example = CloudNgfwAws.GetPredefinedUrlCategoryOverride.Invoke(new()
        ///     {
        ///         Rulestack = r.Name,
        ///         Name = "foobar",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetPredefinedUrlCategoryOverrideResult> Invoke(GetPredefinedUrlCategoryOverrideInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetPredefinedUrlCategoryOverrideResult>("cloudngfwaws:index/getPredefinedUrlCategoryOverride:getPredefinedUrlCategoryOverride", args ?? new GetPredefinedUrlCategoryOverrideInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPredefinedUrlCategoryOverrideArgs : global::Pulumi.InvokeArgs
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

        public GetPredefinedUrlCategoryOverrideArgs()
        {
        }
        public static new GetPredefinedUrlCategoryOverrideArgs Empty => new GetPredefinedUrlCategoryOverrideArgs();
    }

    public sealed class GetPredefinedUrlCategoryOverrideInvokeArgs : global::Pulumi.InvokeArgs
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

        public GetPredefinedUrlCategoryOverrideInvokeArgs()
        {
        }
        public static new GetPredefinedUrlCategoryOverrideInvokeArgs Empty => new GetPredefinedUrlCategoryOverrideInvokeArgs();
    }


    [OutputType]
    public sealed class GetPredefinedUrlCategoryOverrideResult
    {
        /// <summary>
        /// The action to take. Valid values are `none`, `allow`, `alert`, or `block`.
        /// </summary>
        public readonly string Action;
        /// <summary>
        /// The audit comment.
        /// </summary>
        public readonly string AuditComment;
        /// <summary>
        /// Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
        /// </summary>
        public readonly string? ConfigType;
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
        /// Update token.
        /// </summary>
        public readonly string UpdateToken;

        [OutputConstructor]
        private GetPredefinedUrlCategoryOverrideResult(
            string action,

            string auditComment,

            string? configType,

            string id,

            string name,

            string rulestack,

            string updateToken)
        {
            Action = action;
            AuditComment = auditComment;
            ConfigType = configType;
            Id = id;
            Name = name;
            Rulestack = rulestack;
            UpdateToken = updateToken;
        }
    }
}
