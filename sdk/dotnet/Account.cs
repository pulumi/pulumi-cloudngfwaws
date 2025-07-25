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
    /// Resource for Account manipulation.
    /// 
    /// ## Admin Permission Type
    /// 
    /// * `Rulestack` (for `scope="Local"`)
    /// * `Global Rulestack` (for `scope="Global"`)
    /// </summary>
    [CloudNgfwAwsResourceType("cloudngfwaws:index/account:Account")]
    public partial class Account : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The account ID
        /// </summary>
        [Output("accountId")]
        public Output<string?> AccountId { get; private set; } = null!;

        /// <summary>
        /// The CFT URL.
        /// </summary>
        [Output("cftUrl")]
        public Output<string> CftUrl { get; private set; } = null!;

        /// <summary>
        /// The external ID of the account
        /// </summary>
        [Output("externalId")]
        public Output<string> ExternalId { get; private set; } = null!;

        /// <summary>
        /// The Account onboarding status
        /// </summary>
        [Output("onboardingStatus")]
        public Output<string> OnboardingStatus { get; private set; } = null!;

        /// <summary>
        /// Origin of account onboarding
        /// </summary>
        [Output("origin")]
        public Output<string> Origin { get; private set; } = null!;

        /// <summary>
        /// The account ID of cloud NGFW service
        /// </summary>
        [Output("serviceAccountId")]
        public Output<string> ServiceAccountId { get; private set; } = null!;

        /// <summary>
        /// The SNS topic ARN
        /// </summary>
        [Output("snsTopicArn")]
        public Output<string> SnsTopicArn { get; private set; } = null!;

        /// <summary>
        /// The trusted account ID
        /// </summary>
        [Output("trustedAccount")]
        public Output<string> TrustedAccount { get; private set; } = null!;

        /// <summary>
        /// The update token.
        /// </summary>
        [Output("updateToken")]
        public Output<string> UpdateToken { get; private set; } = null!;


        /// <summary>
        /// Create a Account resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Account(string name, AccountArgs? args = null, CustomResourceOptions? options = null)
            : base("cloudngfwaws:index/account:Account", name, args ?? new AccountArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Account(string name, Input<string> id, AccountState? state = null, CustomResourceOptions? options = null)
            : base("cloudngfwaws:index/account:Account", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Account resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Account Get(string name, Input<string> id, AccountState? state = null, CustomResourceOptions? options = null)
        {
            return new Account(name, id, state, options);
        }
    }

    public sealed class AccountArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The account ID
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// The CFT URL.
        /// </summary>
        [Input("cftUrl")]
        public Input<string>? CftUrl { get; set; }

        /// <summary>
        /// The external ID of the account
        /// </summary>
        [Input("externalId")]
        public Input<string>? ExternalId { get; set; }

        /// <summary>
        /// The Account onboarding status
        /// </summary>
        [Input("onboardingStatus")]
        public Input<string>? OnboardingStatus { get; set; }

        /// <summary>
        /// Origin of account onboarding
        /// </summary>
        [Input("origin")]
        public Input<string>? Origin { get; set; }

        /// <summary>
        /// The account ID of cloud NGFW service
        /// </summary>
        [Input("serviceAccountId")]
        public Input<string>? ServiceAccountId { get; set; }

        /// <summary>
        /// The SNS topic ARN
        /// </summary>
        [Input("snsTopicArn")]
        public Input<string>? SnsTopicArn { get; set; }

        /// <summary>
        /// The trusted account ID
        /// </summary>
        [Input("trustedAccount")]
        public Input<string>? TrustedAccount { get; set; }

        public AccountArgs()
        {
        }
        public static new AccountArgs Empty => new AccountArgs();
    }

    public sealed class AccountState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The account ID
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// The CFT URL.
        /// </summary>
        [Input("cftUrl")]
        public Input<string>? CftUrl { get; set; }

        /// <summary>
        /// The external ID of the account
        /// </summary>
        [Input("externalId")]
        public Input<string>? ExternalId { get; set; }

        /// <summary>
        /// The Account onboarding status
        /// </summary>
        [Input("onboardingStatus")]
        public Input<string>? OnboardingStatus { get; set; }

        /// <summary>
        /// Origin of account onboarding
        /// </summary>
        [Input("origin")]
        public Input<string>? Origin { get; set; }

        /// <summary>
        /// The account ID of cloud NGFW service
        /// </summary>
        [Input("serviceAccountId")]
        public Input<string>? ServiceAccountId { get; set; }

        /// <summary>
        /// The SNS topic ARN
        /// </summary>
        [Input("snsTopicArn")]
        public Input<string>? SnsTopicArn { get; set; }

        /// <summary>
        /// The trusted account ID
        /// </summary>
        [Input("trustedAccount")]
        public Input<string>? TrustedAccount { get; set; }

        /// <summary>
        /// The update token.
        /// </summary>
        [Input("updateToken")]
        public Input<string>? UpdateToken { get; set; }

        public AccountState()
        {
        }
        public static new AccountState Empty => new AccountState();
    }
}
