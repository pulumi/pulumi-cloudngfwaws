// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws.Inputs
{

    public sealed class GetAccountsAccountDetailInputArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The account id.
        /// </summary>
        [Input("accountId", required: true)]
        public Input<string> AccountId { get; set; } = null!;

        /// <summary>
        /// External Id of the onboarded account
        /// </summary>
        [Input("externalId", required: true)]
        public Input<string> ExternalId { get; set; } = null!;

        /// <summary>
        /// Onboarding status of the account.
        /// </summary>
        [Input("onboardingStatus", required: true)]
        public Input<string> OnboardingStatus { get; set; } = null!;

        public GetAccountsAccountDetailInputArgs()
        {
        }
        public static new GetAccountsAccountDetailInputArgs Empty => new GetAccountsAccountDetailInputArgs();
    }
}
