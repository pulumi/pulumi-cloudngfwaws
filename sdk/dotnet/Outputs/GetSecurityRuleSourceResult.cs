// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws.Outputs
{

    [OutputType]
    public sealed class GetSecurityRuleSourceResult
    {
        /// <summary>
        /// List of CIDRs.
        /// </summary>
        public readonly ImmutableArray<string> Cidrs;
        /// <summary>
        /// List of countries.
        /// </summary>
        public readonly ImmutableArray<string> Countries;
        /// <summary>
        /// List of feeds.
        /// </summary>
        public readonly ImmutableArray<string> Feeds;
        /// <summary>
        /// List of prefix list.
        /// </summary>
        public readonly ImmutableArray<string> PrefixLists;

        [OutputConstructor]
        private GetSecurityRuleSourceResult(
            ImmutableArray<string> cidrs,

            ImmutableArray<string> countries,

            ImmutableArray<string> feeds,

            ImmutableArray<string> prefixLists)
        {
            Cidrs = cidrs;
            Countries = countries;
            Feeds = feeds;
            PrefixLists = prefixLists;
        }
    }
}
