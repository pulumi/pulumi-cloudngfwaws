// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws.Outputs
{

    [OutputType]
    public sealed class GetSecurityRuleCategoryResult
    {
        /// <summary>
        /// List of feeds.
        /// </summary>
        public readonly ImmutableArray<string> Feeds;
        /// <summary>
        /// List of URL category names.
        /// </summary>
        public readonly ImmutableArray<string> UrlCategoryNames;

        [OutputConstructor]
        private GetSecurityRuleCategoryResult(
            ImmutableArray<string> feeds,

            ImmutableArray<string> urlCategoryNames)
        {
            Feeds = feeds;
            UrlCategoryNames = urlCategoryNames;
        }
    }
}
