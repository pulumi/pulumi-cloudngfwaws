// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws.Inputs
{

    public sealed class SecurityRuleSourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("cidrs")]
        private InputList<string>? _cidrs;

        /// <summary>
        /// List of CIDRs.
        /// </summary>
        public InputList<string> Cidrs
        {
            get => _cidrs ?? (_cidrs = new InputList<string>());
            set => _cidrs = value;
        }

        [Input("countries")]
        private InputList<string>? _countries;

        /// <summary>
        /// List of countries.
        /// </summary>
        public InputList<string> Countries
        {
            get => _countries ?? (_countries = new InputList<string>());
            set => _countries = value;
        }

        [Input("feeds")]
        private InputList<string>? _feeds;

        /// <summary>
        /// List of feeds.
        /// </summary>
        public InputList<string> Feeds
        {
            get => _feeds ?? (_feeds = new InputList<string>());
            set => _feeds = value;
        }

        [Input("prefixLists")]
        private InputList<string>? _prefixLists;

        /// <summary>
        /// List of prefix list.
        /// </summary>
        public InputList<string> PrefixLists
        {
            get => _prefixLists ?? (_prefixLists = new InputList<string>());
            set => _prefixLists = value;
        }

        public SecurityRuleSourceArgs()
        {
        }
        public static new SecurityRuleSourceArgs Empty => new SecurityRuleSourceArgs();
    }
}
