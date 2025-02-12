// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws.outputs;

import com.pulumi.cloudngfwaws.outputs.GetRulestackProfileConfig;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetRulestackResult {
    /**
     * @return Account group.
     * 
     */
    private String accountGroup;
    /**
     * @return The account ID.
     * 
     */
    private String accountId;
    /**
     * @return Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
     * 
     */
    private @Nullable String configType;
    /**
     * @return The description.
     * 
     */
    private String description;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return Lookup x forwarded for.
     * 
     */
    private String lookupXForwardedFor;
    /**
     * @return Minimum App-ID version number.
     * 
     */
    private String minimumAppIdVersion;
    /**
     * @return The name.
     * 
     */
    private String name;
    private List<GetRulestackProfileConfig> profileConfigs;
    /**
     * @return The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     * 
     */
    private @Nullable String scope;
    /**
     * @return The rulestack state.
     * 
     */
    private String state;
    /**
     * @return The tags.
     * 
     */
    private Map<String,String> tags;

    private GetRulestackResult() {}
    /**
     * @return Account group.
     * 
     */
    public String accountGroup() {
        return this.accountGroup;
    }
    /**
     * @return The account ID.
     * 
     */
    public String accountId() {
        return this.accountId;
    }
    /**
     * @return Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
     * 
     */
    public Optional<String> configType() {
        return Optional.ofNullable(this.configType);
    }
    /**
     * @return The description.
     * 
     */
    public String description() {
        return this.description;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Lookup x forwarded for.
     * 
     */
    public String lookupXForwardedFor() {
        return this.lookupXForwardedFor;
    }
    /**
     * @return Minimum App-ID version number.
     * 
     */
    public String minimumAppIdVersion() {
        return this.minimumAppIdVersion;
    }
    /**
     * @return The name.
     * 
     */
    public String name() {
        return this.name;
    }
    public List<GetRulestackProfileConfig> profileConfigs() {
        return this.profileConfigs;
    }
    /**
     * @return The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     * 
     */
    public Optional<String> scope() {
        return Optional.ofNullable(this.scope);
    }
    /**
     * @return The rulestack state.
     * 
     */
    public String state() {
        return this.state;
    }
    /**
     * @return The tags.
     * 
     */
    public Map<String,String> tags() {
        return this.tags;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetRulestackResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String accountGroup;
        private String accountId;
        private @Nullable String configType;
        private String description;
        private String id;
        private String lookupXForwardedFor;
        private String minimumAppIdVersion;
        private String name;
        private List<GetRulestackProfileConfig> profileConfigs;
        private @Nullable String scope;
        private String state;
        private Map<String,String> tags;
        public Builder() {}
        public Builder(GetRulestackResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.accountGroup = defaults.accountGroup;
    	      this.accountId = defaults.accountId;
    	      this.configType = defaults.configType;
    	      this.description = defaults.description;
    	      this.id = defaults.id;
    	      this.lookupXForwardedFor = defaults.lookupXForwardedFor;
    	      this.minimumAppIdVersion = defaults.minimumAppIdVersion;
    	      this.name = defaults.name;
    	      this.profileConfigs = defaults.profileConfigs;
    	      this.scope = defaults.scope;
    	      this.state = defaults.state;
    	      this.tags = defaults.tags;
        }

        @CustomType.Setter
        public Builder accountGroup(String accountGroup) {
            if (accountGroup == null) {
              throw new MissingRequiredPropertyException("GetRulestackResult", "accountGroup");
            }
            this.accountGroup = accountGroup;
            return this;
        }
        @CustomType.Setter
        public Builder accountId(String accountId) {
            if (accountId == null) {
              throw new MissingRequiredPropertyException("GetRulestackResult", "accountId");
            }
            this.accountId = accountId;
            return this;
        }
        @CustomType.Setter
        public Builder configType(@Nullable String configType) {

            this.configType = configType;
            return this;
        }
        @CustomType.Setter
        public Builder description(String description) {
            if (description == null) {
              throw new MissingRequiredPropertyException("GetRulestackResult", "description");
            }
            this.description = description;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetRulestackResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder lookupXForwardedFor(String lookupXForwardedFor) {
            if (lookupXForwardedFor == null) {
              throw new MissingRequiredPropertyException("GetRulestackResult", "lookupXForwardedFor");
            }
            this.lookupXForwardedFor = lookupXForwardedFor;
            return this;
        }
        @CustomType.Setter
        public Builder minimumAppIdVersion(String minimumAppIdVersion) {
            if (minimumAppIdVersion == null) {
              throw new MissingRequiredPropertyException("GetRulestackResult", "minimumAppIdVersion");
            }
            this.minimumAppIdVersion = minimumAppIdVersion;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetRulestackResult", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder profileConfigs(List<GetRulestackProfileConfig> profileConfigs) {
            if (profileConfigs == null) {
              throw new MissingRequiredPropertyException("GetRulestackResult", "profileConfigs");
            }
            this.profileConfigs = profileConfigs;
            return this;
        }
        public Builder profileConfigs(GetRulestackProfileConfig... profileConfigs) {
            return profileConfigs(List.of(profileConfigs));
        }
        @CustomType.Setter
        public Builder scope(@Nullable String scope) {

            this.scope = scope;
            return this;
        }
        @CustomType.Setter
        public Builder state(String state) {
            if (state == null) {
              throw new MissingRequiredPropertyException("GetRulestackResult", "state");
            }
            this.state = state;
            return this;
        }
        @CustomType.Setter
        public Builder tags(Map<String,String> tags) {
            if (tags == null) {
              throw new MissingRequiredPropertyException("GetRulestackResult", "tags");
            }
            this.tags = tags;
            return this;
        }
        public GetRulestackResult build() {
            final var _resultValue = new GetRulestackResult();
            _resultValue.accountGroup = accountGroup;
            _resultValue.accountId = accountId;
            _resultValue.configType = configType;
            _resultValue.description = description;
            _resultValue.id = id;
            _resultValue.lookupXForwardedFor = lookupXForwardedFor;
            _resultValue.minimumAppIdVersion = minimumAppIdVersion;
            _resultValue.name = name;
            _resultValue.profileConfigs = profileConfigs;
            _resultValue.scope = scope;
            _resultValue.state = state;
            _resultValue.tags = tags;
            return _resultValue;
        }
    }
}
