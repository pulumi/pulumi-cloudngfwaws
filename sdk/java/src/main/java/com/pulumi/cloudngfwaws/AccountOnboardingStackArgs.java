// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class AccountOnboardingStackArgs extends com.pulumi.resources.ResourceArgs {

    public static final AccountOnboardingStackArgs Empty = new AccountOnboardingStackArgs();

    /**
     * The account IDs
     * 
     */
    @Import(name="accountId", required=true)
    private Output<String> accountId;

    /**
     * @return The account IDs
     * 
     */
    public Output<String> accountId() {
        return this.accountId;
    }

    /**
     * Audit Log Group Name
     * 
     */
    @Import(name="auditlogGroup")
    private @Nullable Output<String> auditlogGroup;

    /**
     * @return Audit Log Group Name
     * 
     */
    public Optional<Output<String>> auditlogGroup() {
        return Optional.ofNullable(this.auditlogGroup);
    }

    /**
     * Role name to run the account onboarding CFT in each account to be onboarded.
     * 
     */
    @Import(name="cftRoleName", required=true)
    private Output<String> cftRoleName;

    /**
     * @return Role name to run the account onboarding CFT in each account to be onboarded.
     * 
     */
    public Output<String> cftRoleName() {
        return this.cftRoleName;
    }

    /**
     * Cloudwatch Log Group
     * 
     */
    @Import(name="cloudwatchLogGroup")
    private @Nullable Output<String> cloudwatchLogGroup;

    /**
     * @return Cloudwatch Log Group
     * 
     */
    public Optional<Output<String>> cloudwatchLogGroup() {
        return Optional.ofNullable(this.cloudwatchLogGroup);
    }

    /**
     * Cloudwatch Namespace
     * 
     */
    @Import(name="cloudwatchNamespace")
    private @Nullable Output<String> cloudwatchNamespace;

    /**
     * @return Cloudwatch Namespace
     * 
     */
    public Optional<Output<String>> cloudwatchNamespace() {
        return Optional.ofNullable(this.cloudwatchNamespace);
    }

    /**
     * The CloudNGFW can decrypt inbound and outbound traffic by providing a
     * 					  certificate stored in secret Manager.
     * 		 			  The role allows the service to access a certificate configured in the rulestack.
     * 		 			  Only certificated tagged with PaloAltoCloudNGFW can be accessed
     * 
     */
    @Import(name="decryptionCert")
    private @Nullable Output<String> decryptionCert;

    /**
     * @return The CloudNGFW can decrypt inbound and outbound traffic by providing a
     * 					  certificate stored in secret Manager.
     * 		 			  The role allows the service to access a certificate configured in the rulestack.
     * 		 			  Only certificated tagged with PaloAltoCloudNGFW can be accessed
     * 
     */
    public Optional<Output<String>> decryptionCert() {
        return Optional.ofNullable(this.decryptionCert);
    }

    /**
     * Controls whether cloud NGFW will create firewall endpoints automatitically in customer subnets
     * 
     */
    @Import(name="endpointMode")
    private @Nullable Output<String> endpointMode;

    /**
     * @return Controls whether cloud NGFW will create firewall endpoints automatitically in customer subnets
     * 
     */
    public Optional<Output<String>> endpointMode() {
        return Optional.ofNullable(this.endpointMode);
    }

    /**
     * External Id of the onboarded account
     * 
     */
    @Import(name="externalId", required=true)
    private Output<String> externalId;

    /**
     * @return External Id of the onboarded account
     * 
     */
    public Output<String> externalId() {
        return this.externalId;
    }

    /**
     * Kinesis Firehose for logging
     * 
     */
    @Import(name="kinesisFirehose")
    private @Nullable Output<String> kinesisFirehose;

    /**
     * @return Kinesis Firehose for logging
     * 
     */
    public Optional<Output<String>> kinesisFirehose() {
        return Optional.ofNullable(this.kinesisFirehose);
    }

    /**
     * Role name to run the account onboarding CFT in each account to be onboarded.
     * 
     */
    @Import(name="onboardingCft", required=true)
    private Output<String> onboardingCft;

    /**
     * @return Role name to run the account onboarding CFT in each account to be onboarded.
     * 
     */
    public Output<String> onboardingCft() {
        return this.onboardingCft;
    }

    /**
     * S3 Bucket Name for Logging. Logging roles provide access to create log contents in this bucket.
     * 
     */
    @Import(name="s3Bucket")
    private @Nullable Output<String> s3Bucket;

    /**
     * @return S3 Bucket Name for Logging. Logging roles provide access to create log contents in this bucket.
     * 
     */
    public Optional<Output<String>> s3Bucket() {
        return Optional.ofNullable(this.s3Bucket);
    }

    /**
     * SNS topic ARN to publish the role ARNs
     * 
     */
    @Import(name="snsTopicArn", required=true)
    private Output<String> snsTopicArn;

    /**
     * @return SNS topic ARN to publish the role ARNs
     * 
     */
    public Output<String> snsTopicArn() {
        return this.snsTopicArn;
    }

    /**
     * ID of the account onboarding CFT stack
     * 
     */
    @Import(name="stackId")
    private @Nullable Output<String> stackId;

    /**
     * @return ID of the account onboarding CFT stack
     * 
     */
    public Optional<Output<String>> stackId() {
        return Optional.ofNullable(this.stackId);
    }

    /**
     * Status of the account onboarding CFT stack.
     * 
     */
    @Import(name="stackStatus")
    private @Nullable Output<String> stackStatus;

    /**
     * @return Status of the account onboarding CFT stack.
     * 
     */
    public Optional<Output<String>> stackStatus() {
        return Optional.ofNullable(this.stackStatus);
    }

    /**
     * PANW Cloud NGFW trusted account Id
     * 
     */
    @Import(name="trustedAccount", required=true)
    private Output<String> trustedAccount;

    /**
     * @return PANW Cloud NGFW trusted account Id
     * 
     */
    public Output<String> trustedAccount() {
        return this.trustedAccount;
    }

    private AccountOnboardingStackArgs() {}

    private AccountOnboardingStackArgs(AccountOnboardingStackArgs $) {
        this.accountId = $.accountId;
        this.auditlogGroup = $.auditlogGroup;
        this.cftRoleName = $.cftRoleName;
        this.cloudwatchLogGroup = $.cloudwatchLogGroup;
        this.cloudwatchNamespace = $.cloudwatchNamespace;
        this.decryptionCert = $.decryptionCert;
        this.endpointMode = $.endpointMode;
        this.externalId = $.externalId;
        this.kinesisFirehose = $.kinesisFirehose;
        this.onboardingCft = $.onboardingCft;
        this.s3Bucket = $.s3Bucket;
        this.snsTopicArn = $.snsTopicArn;
        this.stackId = $.stackId;
        this.stackStatus = $.stackStatus;
        this.trustedAccount = $.trustedAccount;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(AccountOnboardingStackArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private AccountOnboardingStackArgs $;

        public Builder() {
            $ = new AccountOnboardingStackArgs();
        }

        public Builder(AccountOnboardingStackArgs defaults) {
            $ = new AccountOnboardingStackArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param accountId The account IDs
         * 
         * @return builder
         * 
         */
        public Builder accountId(Output<String> accountId) {
            $.accountId = accountId;
            return this;
        }

        /**
         * @param accountId The account IDs
         * 
         * @return builder
         * 
         */
        public Builder accountId(String accountId) {
            return accountId(Output.of(accountId));
        }

        /**
         * @param auditlogGroup Audit Log Group Name
         * 
         * @return builder
         * 
         */
        public Builder auditlogGroup(@Nullable Output<String> auditlogGroup) {
            $.auditlogGroup = auditlogGroup;
            return this;
        }

        /**
         * @param auditlogGroup Audit Log Group Name
         * 
         * @return builder
         * 
         */
        public Builder auditlogGroup(String auditlogGroup) {
            return auditlogGroup(Output.of(auditlogGroup));
        }

        /**
         * @param cftRoleName Role name to run the account onboarding CFT in each account to be onboarded.
         * 
         * @return builder
         * 
         */
        public Builder cftRoleName(Output<String> cftRoleName) {
            $.cftRoleName = cftRoleName;
            return this;
        }

        /**
         * @param cftRoleName Role name to run the account onboarding CFT in each account to be onboarded.
         * 
         * @return builder
         * 
         */
        public Builder cftRoleName(String cftRoleName) {
            return cftRoleName(Output.of(cftRoleName));
        }

        /**
         * @param cloudwatchLogGroup Cloudwatch Log Group
         * 
         * @return builder
         * 
         */
        public Builder cloudwatchLogGroup(@Nullable Output<String> cloudwatchLogGroup) {
            $.cloudwatchLogGroup = cloudwatchLogGroup;
            return this;
        }

        /**
         * @param cloudwatchLogGroup Cloudwatch Log Group
         * 
         * @return builder
         * 
         */
        public Builder cloudwatchLogGroup(String cloudwatchLogGroup) {
            return cloudwatchLogGroup(Output.of(cloudwatchLogGroup));
        }

        /**
         * @param cloudwatchNamespace Cloudwatch Namespace
         * 
         * @return builder
         * 
         */
        public Builder cloudwatchNamespace(@Nullable Output<String> cloudwatchNamespace) {
            $.cloudwatchNamespace = cloudwatchNamespace;
            return this;
        }

        /**
         * @param cloudwatchNamespace Cloudwatch Namespace
         * 
         * @return builder
         * 
         */
        public Builder cloudwatchNamespace(String cloudwatchNamespace) {
            return cloudwatchNamespace(Output.of(cloudwatchNamespace));
        }

        /**
         * @param decryptionCert The CloudNGFW can decrypt inbound and outbound traffic by providing a
         * 					  certificate stored in secret Manager.
         * 		 			  The role allows the service to access a certificate configured in the rulestack.
         * 		 			  Only certificated tagged with PaloAltoCloudNGFW can be accessed
         * 
         * @return builder
         * 
         */
        public Builder decryptionCert(@Nullable Output<String> decryptionCert) {
            $.decryptionCert = decryptionCert;
            return this;
        }

        /**
         * @param decryptionCert The CloudNGFW can decrypt inbound and outbound traffic by providing a
         * 					  certificate stored in secret Manager.
         * 		 			  The role allows the service to access a certificate configured in the rulestack.
         * 		 			  Only certificated tagged with PaloAltoCloudNGFW can be accessed
         * 
         * @return builder
         * 
         */
        public Builder decryptionCert(String decryptionCert) {
            return decryptionCert(Output.of(decryptionCert));
        }

        /**
         * @param endpointMode Controls whether cloud NGFW will create firewall endpoints automatitically in customer subnets
         * 
         * @return builder
         * 
         */
        public Builder endpointMode(@Nullable Output<String> endpointMode) {
            $.endpointMode = endpointMode;
            return this;
        }

        /**
         * @param endpointMode Controls whether cloud NGFW will create firewall endpoints automatitically in customer subnets
         * 
         * @return builder
         * 
         */
        public Builder endpointMode(String endpointMode) {
            return endpointMode(Output.of(endpointMode));
        }

        /**
         * @param externalId External Id of the onboarded account
         * 
         * @return builder
         * 
         */
        public Builder externalId(Output<String> externalId) {
            $.externalId = externalId;
            return this;
        }

        /**
         * @param externalId External Id of the onboarded account
         * 
         * @return builder
         * 
         */
        public Builder externalId(String externalId) {
            return externalId(Output.of(externalId));
        }

        /**
         * @param kinesisFirehose Kinesis Firehose for logging
         * 
         * @return builder
         * 
         */
        public Builder kinesisFirehose(@Nullable Output<String> kinesisFirehose) {
            $.kinesisFirehose = kinesisFirehose;
            return this;
        }

        /**
         * @param kinesisFirehose Kinesis Firehose for logging
         * 
         * @return builder
         * 
         */
        public Builder kinesisFirehose(String kinesisFirehose) {
            return kinesisFirehose(Output.of(kinesisFirehose));
        }

        /**
         * @param onboardingCft Role name to run the account onboarding CFT in each account to be onboarded.
         * 
         * @return builder
         * 
         */
        public Builder onboardingCft(Output<String> onboardingCft) {
            $.onboardingCft = onboardingCft;
            return this;
        }

        /**
         * @param onboardingCft Role name to run the account onboarding CFT in each account to be onboarded.
         * 
         * @return builder
         * 
         */
        public Builder onboardingCft(String onboardingCft) {
            return onboardingCft(Output.of(onboardingCft));
        }

        /**
         * @param s3Bucket S3 Bucket Name for Logging. Logging roles provide access to create log contents in this bucket.
         * 
         * @return builder
         * 
         */
        public Builder s3Bucket(@Nullable Output<String> s3Bucket) {
            $.s3Bucket = s3Bucket;
            return this;
        }

        /**
         * @param s3Bucket S3 Bucket Name for Logging. Logging roles provide access to create log contents in this bucket.
         * 
         * @return builder
         * 
         */
        public Builder s3Bucket(String s3Bucket) {
            return s3Bucket(Output.of(s3Bucket));
        }

        /**
         * @param snsTopicArn SNS topic ARN to publish the role ARNs
         * 
         * @return builder
         * 
         */
        public Builder snsTopicArn(Output<String> snsTopicArn) {
            $.snsTopicArn = snsTopicArn;
            return this;
        }

        /**
         * @param snsTopicArn SNS topic ARN to publish the role ARNs
         * 
         * @return builder
         * 
         */
        public Builder snsTopicArn(String snsTopicArn) {
            return snsTopicArn(Output.of(snsTopicArn));
        }

        /**
         * @param stackId ID of the account onboarding CFT stack
         * 
         * @return builder
         * 
         */
        public Builder stackId(@Nullable Output<String> stackId) {
            $.stackId = stackId;
            return this;
        }

        /**
         * @param stackId ID of the account onboarding CFT stack
         * 
         * @return builder
         * 
         */
        public Builder stackId(String stackId) {
            return stackId(Output.of(stackId));
        }

        /**
         * @param stackStatus Status of the account onboarding CFT stack.
         * 
         * @return builder
         * 
         */
        public Builder stackStatus(@Nullable Output<String> stackStatus) {
            $.stackStatus = stackStatus;
            return this;
        }

        /**
         * @param stackStatus Status of the account onboarding CFT stack.
         * 
         * @return builder
         * 
         */
        public Builder stackStatus(String stackStatus) {
            return stackStatus(Output.of(stackStatus));
        }

        /**
         * @param trustedAccount PANW Cloud NGFW trusted account Id
         * 
         * @return builder
         * 
         */
        public Builder trustedAccount(Output<String> trustedAccount) {
            $.trustedAccount = trustedAccount;
            return this;
        }

        /**
         * @param trustedAccount PANW Cloud NGFW trusted account Id
         * 
         * @return builder
         * 
         */
        public Builder trustedAccount(String trustedAccount) {
            return trustedAccount(Output.of(trustedAccount));
        }

        public AccountOnboardingStackArgs build() {
            if ($.accountId == null) {
                throw new MissingRequiredPropertyException("AccountOnboardingStackArgs", "accountId");
            }
            if ($.cftRoleName == null) {
                throw new MissingRequiredPropertyException("AccountOnboardingStackArgs", "cftRoleName");
            }
            if ($.externalId == null) {
                throw new MissingRequiredPropertyException("AccountOnboardingStackArgs", "externalId");
            }
            if ($.onboardingCft == null) {
                throw new MissingRequiredPropertyException("AccountOnboardingStackArgs", "onboardingCft");
            }
            if ($.snsTopicArn == null) {
                throw new MissingRequiredPropertyException("AccountOnboardingStackArgs", "snsTopicArn");
            }
            if ($.trustedAccount == null) {
                throw new MissingRequiredPropertyException("AccountOnboardingStackArgs", "trustedAccount");
            }
            return $;
        }
    }

}
