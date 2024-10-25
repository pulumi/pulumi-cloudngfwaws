// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetAppIdVersionResult {
    /**
     * @return List of applications.
     * 
     */
    private List<String> applications;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return Max results. Defaults to `100`.
     * 
     */
    private @Nullable Integer maxResults;
    /**
     * @return Token for the next page of results.
     * 
     */
    private String nextToken;
    /**
     * @return Pagination token.
     * 
     */
    private @Nullable String token;
    /**
     * @return The AppId version.
     * 
     */
    private String version;

    private GetAppIdVersionResult() {}
    /**
     * @return List of applications.
     * 
     */
    public List<String> applications() {
        return this.applications;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Max results. Defaults to `100`.
     * 
     */
    public Optional<Integer> maxResults() {
        return Optional.ofNullable(this.maxResults);
    }
    /**
     * @return Token for the next page of results.
     * 
     */
    public String nextToken() {
        return this.nextToken;
    }
    /**
     * @return Pagination token.
     * 
     */
    public Optional<String> token() {
        return Optional.ofNullable(this.token);
    }
    /**
     * @return The AppId version.
     * 
     */
    public String version() {
        return this.version;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetAppIdVersionResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<String> applications;
        private String id;
        private @Nullable Integer maxResults;
        private String nextToken;
        private @Nullable String token;
        private String version;
        public Builder() {}
        public Builder(GetAppIdVersionResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.applications = defaults.applications;
    	      this.id = defaults.id;
    	      this.maxResults = defaults.maxResults;
    	      this.nextToken = defaults.nextToken;
    	      this.token = defaults.token;
    	      this.version = defaults.version;
        }

        @CustomType.Setter
        public Builder applications(List<String> applications) {
            if (applications == null) {
              throw new MissingRequiredPropertyException("GetAppIdVersionResult", "applications");
            }
            this.applications = applications;
            return this;
        }
        public Builder applications(String... applications) {
            return applications(List.of(applications));
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetAppIdVersionResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder maxResults(@Nullable Integer maxResults) {

            this.maxResults = maxResults;
            return this;
        }
        @CustomType.Setter
        public Builder nextToken(String nextToken) {
            if (nextToken == null) {
              throw new MissingRequiredPropertyException("GetAppIdVersionResult", "nextToken");
            }
            this.nextToken = nextToken;
            return this;
        }
        @CustomType.Setter
        public Builder token(@Nullable String token) {

            this.token = token;
            return this;
        }
        @CustomType.Setter
        public Builder version(String version) {
            if (version == null) {
              throw new MissingRequiredPropertyException("GetAppIdVersionResult", "version");
            }
            this.version = version;
            return this;
        }
        public GetAppIdVersionResult build() {
            final var _resultValue = new GetAppIdVersionResult();
            _resultValue.applications = applications;
            _resultValue.id = id;
            _resultValue.maxResults = maxResults;
            _resultValue.nextToken = nextToken;
            _resultValue.token = token;
            _resultValue.version = version;
            return _resultValue;
        }
    }
}
