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
public final class GetPredefinedUrlCategoriesResult {
    /**
     * @return List of predefined URL categories.
     * 
     */
    private List<String> categories;
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
     * @return Next pagination token.
     * 
     */
    private String nextToken;
    /**
     * @return Pagination token.
     * 
     */
    private @Nullable String token;

    private GetPredefinedUrlCategoriesResult() {}
    /**
     * @return List of predefined URL categories.
     * 
     */
    public List<String> categories() {
        return this.categories;
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
     * @return Next pagination token.
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

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetPredefinedUrlCategoriesResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<String> categories;
        private String id;
        private @Nullable Integer maxResults;
        private String nextToken;
        private @Nullable String token;
        public Builder() {}
        public Builder(GetPredefinedUrlCategoriesResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.categories = defaults.categories;
    	      this.id = defaults.id;
    	      this.maxResults = defaults.maxResults;
    	      this.nextToken = defaults.nextToken;
    	      this.token = defaults.token;
        }

        @CustomType.Setter
        public Builder categories(List<String> categories) {
            if (categories == null) {
              throw new MissingRequiredPropertyException("GetPredefinedUrlCategoriesResult", "categories");
            }
            this.categories = categories;
            return this;
        }
        public Builder categories(String... categories) {
            return categories(List.of(categories));
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetPredefinedUrlCategoriesResult", "id");
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
              throw new MissingRequiredPropertyException("GetPredefinedUrlCategoriesResult", "nextToken");
            }
            this.nextToken = nextToken;
            return this;
        }
        @CustomType.Setter
        public Builder token(@Nullable String token) {

            this.token = token;
            return this;
        }
        public GetPredefinedUrlCategoriesResult build() {
            final var _resultValue = new GetPredefinedUrlCategoriesResult();
            _resultValue.categories = categories;
            _resultValue.id = id;
            _resultValue.maxResults = maxResults;
            _resultValue.nextToken = nextToken;
            _resultValue.token = token;
            return _resultValue;
        }
    }
}
