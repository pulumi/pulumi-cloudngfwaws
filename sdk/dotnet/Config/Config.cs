// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Pulumi.CloudNgfwAws
{
    public static class Config
    {
        [global::System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "IDE1006", Justification = 
        "Double underscore prefix used to avoid conflicts with variable names.")]
        private sealed class __Value<T>
        {
            private readonly Func<T> _getter;
            private T _value = default!;
            private bool _set;

            public __Value(Func<T> getter)
            {
                _getter = getter;
            }

            public T Get() => _set ? _value : _getter();

            public void Set(T value)
            {
                _value = value;
                _set = true;
            }
        }

        private static readonly global::Pulumi.Config __config = new global::Pulumi.Config("cloudngfwaws");

        private static readonly __Value<string?> _accessKey = new __Value<string?>(() => __config.Get("accessKey"));
        /// <summary>
        /// (Used for the initial `sts assume role`) AWS access key. Environment variable: `CLOUDNGFWAWS_ACCESS_KEY`. JSON conf file
        /// variable: `access-key`.
        /// </summary>
        public static string? AccessKey
        {
            get => _accessKey.Get();
            set => _accessKey.Set(value);
        }

        private static readonly __Value<string?> _accountAdminArn = new __Value<string?>(() => __config.Get("accountAdminArn"));
        /// <summary>
        /// The ARN allowing account admin permissions. Environment variable: `CLOUDNGFWAWS_ACCT_ADMIN_ARN`. JSON conf file
        /// variable: `account-admin-arn`.
        /// </summary>
        public static string? AccountAdminArn
        {
            get => _accountAdminArn.Get();
            set => _accountAdminArn.Set(value);
        }

        private static readonly __Value<string?> _arn = new __Value<string?>(() => __config.Get("arn"));
        /// <summary>
        /// The ARN allowing firewall, rulestack, and global rulestack admin permissions. Global rulestack admin permissions can be
        /// enabled only if the AWS account is onboarded by AWS Firewall Manager. Use 'lfa_arn' and 'lra_arn' if you want to enable
        /// only firewall and rulestack admin permissions. Environment variable: `CLOUDNGFWAWS_ARN`. JSON conf file variable: `arn`.
        /// </summary>
        public static string? Arn
        {
            get => _arn.Get();
            set => _arn.Set(value);
        }

        private static readonly __Value<string?> _graArn = new __Value<string?>(() => __config.Get("graArn"));
        /// <summary>
        /// The ARN allowing global rulestack admin permissions. Global rulestack admin permissions can be enabled only if the AWS
        /// account is onboarded by AWS Firewall Manager. 'gra_arn' is preferentially used over the `arn` param if both are
        /// specified. Environment variable: `CLOUDNGFWAWS_GRA_ARN`. JSON conf file variable: `gra-arn`.
        /// </summary>
        public static string? GraArn
        {
            get => _graArn.Get();
            set => _graArn.Set(value);
        }

        private static readonly __Value<ImmutableDictionary<string, string>?> _headers = new __Value<ImmutableDictionary<string, string>?>(() => __config.GetObject<ImmutableDictionary<string, string>>("headers"));
        /// <summary>
        /// Additional HTTP headers to send with API calls. Environment variable: `CLOUDNGFWAWS_HEADERS`. JSON conf file variable:
        /// `headers`.
        /// </summary>
        public static ImmutableDictionary<string, string>? Headers
        {
            get => _headers.Get();
            set => _headers.Set(value);
        }

        private static readonly __Value<string?> _host = new __Value<string?>(() => __config.Get("host"));
        /// <summary>
        /// The hostname of the API (default: `api.us-east-1.aws.cloudngfw.paloaltonetworks.com`). Environment variable:
        /// `CLOUDNGFWAWS_HOST`. JSON conf file variable: `host`.
        /// </summary>
        public static string? Host
        {
            get => _host.Get();
            set => _host.Set(value);
        }

        private static readonly __Value<string?> _jsonConfigFile = new __Value<string?>(() => __config.Get("jsonConfigFile"));
        /// <summary>
        /// Retrieve provider configuration from this JSON file.
        /// </summary>
        public static string? JsonConfigFile
        {
            get => _jsonConfigFile.Get();
            set => _jsonConfigFile.Set(value);
        }

        private static readonly __Value<string?> _lfaArn = new __Value<string?>(() => __config.Get("lfaArn"));
        /// <summary>
        /// The ARN allowing firewall admin permissions. This is preferentially used over the `arn` param if both are specified.
        /// Environment variable: `CLOUDNGFWAWS_LFA_ARN`. JSON conf file variable: `lfa-arn`.
        /// </summary>
        public static string? LfaArn
        {
            get => _lfaArn.Get();
            set => _lfaArn.Set(value);
        }

        private static readonly __Value<ImmutableArray<string>> _loggings = new __Value<ImmutableArray<string>>(() => __config.GetObject<ImmutableArray<string>>("loggings"));
        /// <summary>
        /// The logging options for the provider. Environment variable: `CLOUDNGFWAWS_LOGGING`. JSON conf file variable: `logging`.
        /// </summary>
        public static ImmutableArray<string> Loggings
        {
            get => _loggings.Get();
            set => _loggings.Set(value);
        }

        private static readonly __Value<string?> _lraArn = new __Value<string?>(() => __config.Get("lraArn"));
        /// <summary>
        /// The ARN allowing rulestack admin permissions. This is preferentially used over the `arn` param if both are specified.
        /// Environment variable: `CLOUDNGFWAWS_LRA_ARN`. JSON conf file variable: `lra-arn`.
        /// </summary>
        public static string? LraArn
        {
            get => _lraArn.Get();
            set => _lraArn.Set(value);
        }

        private static readonly __Value<string?> _mpRegion = new __Value<string?>(() => __config.Get("mpRegion"));
        /// <summary>
        /// AWS management plane region. Environment variable: `CLOUDNGFWAWS_MP_REGION`. JSON conf file variable: `mp_region`.
        /// </summary>
        public static string? MpRegion
        {
            get => _mpRegion.Get();
            set => _mpRegion.Set(value);
        }

        private static readonly __Value<string?> _mpRegionHost = new __Value<string?>(() => __config.Get("mpRegionHost"));
        /// <summary>
        /// AWS management plane MP region host Environment variable: `CLOUDNGFWAWS_MP_REGION_HOST`. JSON conf file variable:
        /// `mp_region_host`.
        /// </summary>
        public static string? MpRegionHost
        {
            get => _mpRegionHost.Get();
            set => _mpRegionHost.Set(value);
        }

        private static readonly __Value<string?> _profile = new __Value<string?>(() => __config.Get("profile"));
        /// <summary>
        /// (Used for the initial `sts assume role`) AWS PROFILE. Environment variable: `CLOUDNGFWAWS_PROFILE`. JSON conf file
        /// variable: `profile`.
        /// </summary>
        public static string? Profile
        {
            get => _profile.Get();
            set => _profile.Set(value);
        }

        private static readonly __Value<string?> _protocol = new __Value<string?>(() => __config.Get("protocol"));
        /// <summary>
        /// The protocol (defaults to `https`). Environment variable: `CLOUDNGFWAWS_PROTOCOL`. JSON conf file variable: `protocol`.
        /// Valid values are `https` or `http`.
        /// </summary>
        public static string? Protocol
        {
            get => _protocol.Get();
            set => _protocol.Set(value);
        }

        private static readonly __Value<string?> _region = new __Value<string?>(() => __config.Get("region"));
        /// <summary>
        /// AWS region. Environment variable: `CLOUDNGFWAWS_REGION`. JSON conf file variable: `region`.
        /// </summary>
        public static string? Region
        {
            get => _region.Get();
            set => _region.Set(value);
        }

        private static readonly __Value<int?> _resourceTimeout = new __Value<int?>(() => __config.GetInt32("resourceTimeout"));
        public static int? ResourceTimeout
        {
            get => _resourceTimeout.Get();
            set => _resourceTimeout.Set(value);
        }

        private static readonly __Value<string?> _secretKey = new __Value<string?>(() => __config.Get("secretKey"));
        /// <summary>
        /// (Used for the initial `sts assume role`) AWS secret key. Environment variable: `CLOUDNGFWAWS_SECRET_KEY`. JSON conf file
        /// variable: `secret-key`.
        /// </summary>
        public static string? SecretKey
        {
            get => _secretKey.Get();
            set => _secretKey.Set(value);
        }

        private static readonly __Value<bool?> _skipVerifyCertificate = new __Value<bool?>(() => __config.GetBoolean("skipVerifyCertificate"));
        /// <summary>
        /// Skip verifying the SSL certificate. Environment variable: `CLOUDNGFWAWS_SKIP_VERIFY_CERTIFICATE`. JSON conf file
        /// variable: `skip-verify-certificate`.
        /// </summary>
        public static bool? SkipVerifyCertificate
        {
            get => _skipVerifyCertificate.Get();
            set => _skipVerifyCertificate.Set(value);
        }

        private static readonly __Value<bool?> _syncMode = new __Value<bool?>(() => __config.GetBoolean("syncMode"));
        /// <summary>
        /// Enable synchronous mode while creating resources Environment variable: `CLOUDNGFWAWS_SYNC_MODE`. JSON conf file
        /// variable: `sync_mode`.
        /// </summary>
        public static bool? SyncMode
        {
            get => _syncMode.Get();
            set => _syncMode.Set(value);
        }

        private static readonly __Value<int?> _timeout = new __Value<int?>(() => __config.GetInt32("timeout"));
        /// <summary>
        /// The timeout for any single API call (default: `30`). Environment variable: `CLOUDNGFWAWS_TIMEOUT`. JSON conf file
        /// variable: `timeout`.
        /// </summary>
        public static int? Timeout
        {
            get => _timeout.Get();
            set => _timeout.Set(value);
        }

    }
}
