// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws
{
    public static class GetCountry
    {
        /// <summary>
        /// Data source get a list of countries and their country codes.
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
        ///     var example = CloudNgfwAws.GetCountry.Invoke();
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetCountryResult> InvokeAsync(GetCountryArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCountryResult>("cloudngfwaws:index/getCountry:getCountry", args ?? new GetCountryArgs(), options.WithDefaults());

        /// <summary>
        /// Data source get a list of countries and their country codes.
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
        ///     var example = CloudNgfwAws.GetCountry.Invoke();
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetCountryResult> Invoke(GetCountryInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCountryResult>("cloudngfwaws:index/getCountry:getCountry", args ?? new GetCountryInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCountryArgs : global::Pulumi.InvokeArgs
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

        public GetCountryArgs()
        {
        }
        public static new GetCountryArgs Empty => new GetCountryArgs();
    }

    public sealed class GetCountryInvokeArgs : global::Pulumi.InvokeArgs
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

        public GetCountryInvokeArgs()
        {
        }
        public static new GetCountryInvokeArgs Empty => new GetCountryInvokeArgs();
    }


    [OutputType]
    public sealed class GetCountryResult
    {
        /// <summary>
        /// The country code (as the key) and description (as the value).
        /// </summary>
        public readonly ImmutableDictionary<string, string> Codes;
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

        [OutputConstructor]
        private GetCountryResult(
            ImmutableDictionary<string, string> codes,

            string id,

            int? maxResults,

            string nextToken,

            string? token)
        {
            Codes = codes;
            Id = id;
            MaxResults = maxResults;
            NextToken = nextToken;
            Token = token;
        }
    }
}
