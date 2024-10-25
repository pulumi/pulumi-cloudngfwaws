// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class AccountArgs extends com.pulumi.resources.ResourceArgs {

    public static final AccountArgs Empty = new AccountArgs();

    /**
     * The account ID
     * 
     */
    @Import(name="accountId")
    private @Nullable Output<String> accountId;

    /**
     * @return The account ID
     * 
     */
    public Optional<Output<String>> accountId() {
        return Optional.ofNullable(this.accountId);
    }

    /**
     * The CFT URL.
     * 
     */
    @Import(name="cftUrl")
    private @Nullable Output<String> cftUrl;

    /**
     * @return The CFT URL.
     * 
     */
    public Optional<Output<String>> cftUrl() {
        return Optional.ofNullable(this.cftUrl);
    }

    /**
     * The external ID of the account
     * 
     */
    @Import(name="externalId")
    private @Nullable Output<String> externalId;

    /**
     * @return The external ID of the account
     * 
     */
    public Optional<Output<String>> externalId() {
        return Optional.ofNullable(this.externalId);
    }

    /**
     * The Account onboarding status
     * 
     */
    @Import(name="onboardingStatus")
    private @Nullable Output<String> onboardingStatus;

    /**
     * @return The Account onboarding status
     * 
     */
    public Optional<Output<String>> onboardingStatus() {
        return Optional.ofNullable(this.onboardingStatus);
    }

    /**
     * Origin of account onboarding
     * 
     */
    @Import(name="origin")
    private @Nullable Output<String> origin;

    /**
     * @return Origin of account onboarding
     * 
     */
    public Optional<Output<String>> origin() {
        return Optional.ofNullable(this.origin);
    }

    /**
     * The account ID of cloud NGFW service
     * 
     */
    @Import(name="serviceAccountId")
    private @Nullable Output<String> serviceAccountId;

    /**
     * @return The account ID of cloud NGFW service
     * 
     */
    public Optional<Output<String>> serviceAccountId() {
        return Optional.ofNullable(this.serviceAccountId);
    }

    /**
     * The SNS topic ARN
     * 
     */
    @Import(name="snsTopicArn")
    private @Nullable Output<String> snsTopicArn;

    /**
     * @return The SNS topic ARN
     * 
     */
    public Optional<Output<String>> snsTopicArn() {
        return Optional.ofNullable(this.snsTopicArn);
    }

    /**
     * The trusted account ID
     * 
     */
    @Import(name="trustedAccount")
    private @Nullable Output<String> trustedAccount;

    /**
     * @return The trusted account ID
     * 
     */
    public Optional<Output<String>> trustedAccount() {
        return Optional.ofNullable(this.trustedAccount);
    }

    private AccountArgs() {}

    private AccountArgs(AccountArgs $) {
        this.accountId = $.accountId;
        this.cftUrl = $.cftUrl;
        this.externalId = $.externalId;
        this.onboardingStatus = $.onboardingStatus;
        this.origin = $.origin;
        this.serviceAccountId = $.serviceAccountId;
        this.snsTopicArn = $.snsTopicArn;
        this.trustedAccount = $.trustedAccount;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(AccountArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private AccountArgs $;

        public Builder() {
            $ = new AccountArgs();
        }

        public Builder(AccountArgs defaults) {
            $ = new AccountArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param accountId The account ID
         * 
         * @return builder
         * 
         */
        public Builder accountId(@Nullable Output<String> accountId) {
            $.accountId = accountId;
            return this;
        }

        /**
         * @param accountId The account ID
         * 
         * @return builder
         * 
         */
        public Builder accountId(String accountId) {
            return accountId(Output.of(accountId));
        }

        /**
         * @param cftUrl The CFT URL.
         * 
         * @return builder
         * 
         */
        public Builder cftUrl(@Nullable Output<String> cftUrl) {
            $.cftUrl = cftUrl;
            return this;
        }

        /**
         * @param cftUrl The CFT URL.
         * 
         * @return builder
         * 
         */
        public Builder cftUrl(String cftUrl) {
            return cftUrl(Output.of(cftUrl));
        }

        /**
         * @param externalId The external ID of the account
         * 
         * @return builder
         * 
         */
        public Builder externalId(@Nullable Output<String> externalId) {
            $.externalId = externalId;
            return this;
        }

        /**
         * @param externalId The external ID of the account
         * 
         * @return builder
         * 
         */
        public Builder externalId(String externalId) {
            return externalId(Output.of(externalId));
        }

        /**
         * @param onboardingStatus The Account onboarding status
         * 
         * @return builder
         * 
         */
        public Builder onboardingStatus(@Nullable Output<String> onboardingStatus) {
            $.onboardingStatus = onboardingStatus;
            return this;
        }

        /**
         * @param onboardingStatus The Account onboarding status
         * 
         * @return builder
         * 
         */
        public Builder onboardingStatus(String onboardingStatus) {
            return onboardingStatus(Output.of(onboardingStatus));
        }

        /**
         * @param origin Origin of account onboarding
         * 
         * @return builder
         * 
         */
        public Builder origin(@Nullable Output<String> origin) {
            $.origin = origin;
            return this;
        }

        /**
         * @param origin Origin of account onboarding
         * 
         * @return builder
         * 
         */
        public Builder origin(String origin) {
            return origin(Output.of(origin));
        }

        /**
         * @param serviceAccountId The account ID of cloud NGFW service
         * 
         * @return builder
         * 
         */
        public Builder serviceAccountId(@Nullable Output<String> serviceAccountId) {
            $.serviceAccountId = serviceAccountId;
            return this;
        }

        /**
         * @param serviceAccountId The account ID of cloud NGFW service
         * 
         * @return builder
         * 
         */
        public Builder serviceAccountId(String serviceAccountId) {
            return serviceAccountId(Output.of(serviceAccountId));
        }

        /**
         * @param snsTopicArn The SNS topic ARN
         * 
         * @return builder
         * 
         */
        public Builder snsTopicArn(@Nullable Output<String> snsTopicArn) {
            $.snsTopicArn = snsTopicArn;
            return this;
        }

        /**
         * @param snsTopicArn The SNS topic ARN
         * 
         * @return builder
         * 
         */
        public Builder snsTopicArn(String snsTopicArn) {
            return snsTopicArn(Output.of(snsTopicArn));
        }

        /**
         * @param trustedAccount The trusted account ID
         * 
         * @return builder
         * 
         */
        public Builder trustedAccount(@Nullable Output<String> trustedAccount) {
            $.trustedAccount = trustedAccount;
            return this;
        }

        /**
         * @param trustedAccount The trusted account ID
         * 
         * @return builder
         * 
         */
        public Builder trustedAccount(String trustedAccount) {
            return trustedAccount(Output.of(trustedAccount));
        }

        public AccountArgs build() {
            return $;
        }
    }

}
