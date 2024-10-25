// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetCertificateResult {
    /**
     * @return The audit comment.
     * 
     */
    private String auditComment;
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
     * @return The name.
     * 
     */
    private String name;
    /**
     * @return The rulestack.
     * 
     */
    private String rulestack;
    /**
     * @return The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     * 
     */
    private @Nullable String scope;
    /**
     * @return Set to true if certificate is self-signed.
     * 
     */
    private Boolean selfSigned;
    /**
     * @return The certificate signer ARN.
     * 
     */
    private String signerArn;
    /**
     * @return The update token.
     * 
     */
    private String updateToken;

    private GetCertificateResult() {}
    /**
     * @return The audit comment.
     * 
     */
    public String auditComment() {
        return this.auditComment;
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
     * @return The name.
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return The rulestack.
     * 
     */
    public String rulestack() {
        return this.rulestack;
    }
    /**
     * @return The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     * 
     */
    public Optional<String> scope() {
        return Optional.ofNullable(this.scope);
    }
    /**
     * @return Set to true if certificate is self-signed.
     * 
     */
    public Boolean selfSigned() {
        return this.selfSigned;
    }
    /**
     * @return The certificate signer ARN.
     * 
     */
    public String signerArn() {
        return this.signerArn;
    }
    /**
     * @return The update token.
     * 
     */
    public String updateToken() {
        return this.updateToken;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetCertificateResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String auditComment;
        private @Nullable String configType;
        private String description;
        private String id;
        private String name;
        private String rulestack;
        private @Nullable String scope;
        private Boolean selfSigned;
        private String signerArn;
        private String updateToken;
        public Builder() {}
        public Builder(GetCertificateResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.auditComment = defaults.auditComment;
    	      this.configType = defaults.configType;
    	      this.description = defaults.description;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.rulestack = defaults.rulestack;
    	      this.scope = defaults.scope;
    	      this.selfSigned = defaults.selfSigned;
    	      this.signerArn = defaults.signerArn;
    	      this.updateToken = defaults.updateToken;
        }

        @CustomType.Setter
        public Builder auditComment(String auditComment) {
            if (auditComment == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "auditComment");
            }
            this.auditComment = auditComment;
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
              throw new MissingRequiredPropertyException("GetCertificateResult", "description");
            }
            this.description = description;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder rulestack(String rulestack) {
            if (rulestack == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "rulestack");
            }
            this.rulestack = rulestack;
            return this;
        }
        @CustomType.Setter
        public Builder scope(@Nullable String scope) {

            this.scope = scope;
            return this;
        }
        @CustomType.Setter
        public Builder selfSigned(Boolean selfSigned) {
            if (selfSigned == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "selfSigned");
            }
            this.selfSigned = selfSigned;
            return this;
        }
        @CustomType.Setter
        public Builder signerArn(String signerArn) {
            if (signerArn == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "signerArn");
            }
            this.signerArn = signerArn;
            return this;
        }
        @CustomType.Setter
        public Builder updateToken(String updateToken) {
            if (updateToken == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "updateToken");
            }
            this.updateToken = updateToken;
            return this;
        }
        public GetCertificateResult build() {
            final var _resultValue = new GetCertificateResult();
            _resultValue.auditComment = auditComment;
            _resultValue.configType = configType;
            _resultValue.description = description;
            _resultValue.id = id;
            _resultValue.name = name;
            _resultValue.rulestack = rulestack;
            _resultValue.scope = scope;
            _resultValue.selfSigned = selfSigned;
            _resultValue.signerArn = signerArn;
            _resultValue.updateToken = updateToken;
            return _resultValue;
        }
    }
}
