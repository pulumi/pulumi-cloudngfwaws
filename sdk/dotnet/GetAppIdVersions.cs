// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws
{
    public static class GetAppIdVersions
    {
        /// <summary>
        /// Data source get a list of AppId versions.
        /// 
        /// 
        /// ## Admin Permission Type
        /// 
        /// * `Rulestack`
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
        ///     var example = CloudNgfwAws.GetAppIdVersions.Invoke();
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetAppIdVersionsResult> InvokeAsync(GetAppIdVersionsArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAppIdVersionsResult>("cloudngfwaws:index/getAppIdVersions:getAppIdVersions", args ?? new GetAppIdVersionsArgs(), options.WithDefaults());

        /// <summary>
        /// Data source get a list of AppId versions.
        /// 
        /// 
        /// ## Admin Permission Type
        /// 
        /// * `Rulestack`
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
        ///     var example = CloudNgfwAws.GetAppIdVersions.Invoke();
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetAppIdVersionsResult> Invoke(GetAppIdVersionsInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAppIdVersionsResult>("cloudngfwaws:index/getAppIdVersions:getAppIdVersions", args ?? new GetAppIdVersionsInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// Data source get a list of AppId versions.
        /// 
        /// 
        /// ## Admin Permission Type
        /// 
        /// * `Rulestack`
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
        ///     var example = CloudNgfwAws.GetAppIdVersions.Invoke();
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetAppIdVersionsResult> Invoke(GetAppIdVersionsInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetAppIdVersionsResult>("cloudngfwaws:index/getAppIdVersions:getAppIdVersions", args ?? new GetAppIdVersionsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAppIdVersionsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Max number of results. Defaults to `100`.
        /// </summary>
        [Input("maxResults")]
        public int? MaxResults { get; set; }

        /// <summary>
        /// Pagination token.
        /// </summary>
        [Input("token")]
        public string? Token { get; set; }

        public GetAppIdVersionsArgs()
        {
        }
        public static new GetAppIdVersionsArgs Empty => new GetAppIdVersionsArgs();
    }

    public sealed class GetAppIdVersionsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Max number of results. Defaults to `100`.
        /// </summary>
        [Input("maxResults")]
        public Input<int>? MaxResults { get; set; }

        /// <summary>
        /// Pagination token.
        /// </summary>
        [Input("token")]
        public Input<string>? Token { get; set; }

        public GetAppIdVersionsInvokeArgs()
        {
        }
        public static new GetAppIdVersionsInvokeArgs Empty => new GetAppIdVersionsInvokeArgs();
    }


    [OutputType]
    public sealed class GetAppIdVersionsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Max number of results. Defaults to `100`.
        /// </summary>
        public readonly int? MaxResults;
        /// <summary>
        /// Token for the next page of results.
        /// </summary>
        public readonly string NextToken;
        /// <summary>
        /// Pagination token.
        /// </summary>
        public readonly string? Token;
        /// <summary>
        /// List of AppId versions.
        /// </summary>
        public readonly ImmutableArray<string> Versions;

        [OutputConstructor]
        private GetAppIdVersionsResult(
            string id,

            int? maxResults,

            string nextToken,

            string? token,

            ImmutableArray<string> versions)
        {
            Id = id;
            MaxResults = maxResults;
            NextToken = nextToken;
            Token = token;
            Versions = versions;
        }
    }
}
