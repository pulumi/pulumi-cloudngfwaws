// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws.outputs;

import com.pulumi.cloudngfwaws.outputs.GetAccountsAccountDetail;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetAccountsResult {
    /**
     * @return List of account details.
     * 
     */
    private List<GetAccountsAccountDetail> accountDetails;
    /**
     * @return List of account ids.
     * 
     */
    private List<String> accountIds;
    /**
     * @return Flag to include account details while listing accounts. Defaults to `false`.
     * 
     */
    private @Nullable Boolean describe;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;

    private GetAccountsResult() {}
    /**
     * @return List of account details.
     * 
     */
    public List<GetAccountsAccountDetail> accountDetails() {
        return this.accountDetails;
    }
    /**
     * @return List of account ids.
     * 
     */
    public List<String> accountIds() {
        return this.accountIds;
    }
    /**
     * @return Flag to include account details while listing accounts. Defaults to `false`.
     * 
     */
    public Optional<Boolean> describe() {
        return Optional.ofNullable(this.describe);
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetAccountsResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<GetAccountsAccountDetail> accountDetails;
        private List<String> accountIds;
        private @Nullable Boolean describe;
        private String id;
        public Builder() {}
        public Builder(GetAccountsResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.accountDetails = defaults.accountDetails;
    	      this.accountIds = defaults.accountIds;
    	      this.describe = defaults.describe;
    	      this.id = defaults.id;
        }

        @CustomType.Setter
        public Builder accountDetails(List<GetAccountsAccountDetail> accountDetails) {
            if (accountDetails == null) {
              throw new MissingRequiredPropertyException("GetAccountsResult", "accountDetails");
            }
            this.accountDetails = accountDetails;
            return this;
        }
        public Builder accountDetails(GetAccountsAccountDetail... accountDetails) {
            return accountDetails(List.of(accountDetails));
        }
        @CustomType.Setter
        public Builder accountIds(List<String> accountIds) {
            if (accountIds == null) {
              throw new MissingRequiredPropertyException("GetAccountsResult", "accountIds");
            }
            this.accountIds = accountIds;
            return this;
        }
        public Builder accountIds(String... accountIds) {
            return accountIds(List.of(accountIds));
        }
        @CustomType.Setter
        public Builder describe(@Nullable Boolean describe) {

            this.describe = describe;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetAccountsResult", "id");
            }
            this.id = id;
            return this;
        }
        public GetAccountsResult build() {
            final var _resultValue = new GetAccountsResult();
            _resultValue.accountDetails = accountDetails;
            _resultValue.accountIds = accountIds;
            _resultValue.describe = describe;
            _resultValue.id = id;
            return _resultValue;
        }
    }
}
