// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.CloudNgfwAws.Inputs
{

    public sealed class NgfwStatusAttachmentGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The endpoint id.
        /// </summary>
        [Input("endpointId")]
        public Input<string>? EndpointId { get; set; }

        /// <summary>
        /// The reject reason.
        /// </summary>
        [Input("rejectedReason")]
        public Input<string>? RejectedReason { get; set; }

        /// <summary>
        /// The attachment status.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// The subnet id.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        public NgfwStatusAttachmentGetArgs()
        {
        }
        public static new NgfwStatusAttachmentGetArgs Empty => new NgfwStatusAttachmentGetArgs();
    }
}
