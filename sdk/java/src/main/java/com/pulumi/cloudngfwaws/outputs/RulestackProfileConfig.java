// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class RulestackProfileConfig {
    /**
     * @return Anti-spyware profile setting. Defaults to `BestPractice`.
     * 
     */
    private @Nullable String antiSpyware;
    /**
     * @return Anti-virus profile setting. Defaults to `BestPractice`.
     * 
     */
    private @Nullable String antiVirus;
    /**
     * @return File blocking profile setting. Defaults to `BestPractice`.
     * 
     */
    private @Nullable String fileBlocking;
    /**
     * @return Outbound trust certificate.
     * 
     */
    private @Nullable String outboundTrustCertificate;
    /**
     * @return Outbound untrust certificate.
     * 
     */
    private @Nullable String outboundUntrustCertificate;
    /**
     * @return URL filtering profile setting. Defaults to `None`.
     * 
     */
    private @Nullable String urlFiltering;
    /**
     * @return Vulnerability profile setting. Defaults to `BestPractice`.
     * 
     */
    private @Nullable String vulnerability;

    private RulestackProfileConfig() {}
    /**
     * @return Anti-spyware profile setting. Defaults to `BestPractice`.
     * 
     */
    public Optional<String> antiSpyware() {
        return Optional.ofNullable(this.antiSpyware);
    }
    /**
     * @return Anti-virus profile setting. Defaults to `BestPractice`.
     * 
     */
    public Optional<String> antiVirus() {
        return Optional.ofNullable(this.antiVirus);
    }
    /**
     * @return File blocking profile setting. Defaults to `BestPractice`.
     * 
     */
    public Optional<String> fileBlocking() {
        return Optional.ofNullable(this.fileBlocking);
    }
    /**
     * @return Outbound trust certificate.
     * 
     */
    public Optional<String> outboundTrustCertificate() {
        return Optional.ofNullable(this.outboundTrustCertificate);
    }
    /**
     * @return Outbound untrust certificate.
     * 
     */
    public Optional<String> outboundUntrustCertificate() {
        return Optional.ofNullable(this.outboundUntrustCertificate);
    }
    /**
     * @return URL filtering profile setting. Defaults to `None`.
     * 
     */
    public Optional<String> urlFiltering() {
        return Optional.ofNullable(this.urlFiltering);
    }
    /**
     * @return Vulnerability profile setting. Defaults to `BestPractice`.
     * 
     */
    public Optional<String> vulnerability() {
        return Optional.ofNullable(this.vulnerability);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(RulestackProfileConfig defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable String antiSpyware;
        private @Nullable String antiVirus;
        private @Nullable String fileBlocking;
        private @Nullable String outboundTrustCertificate;
        private @Nullable String outboundUntrustCertificate;
        private @Nullable String urlFiltering;
        private @Nullable String vulnerability;
        public Builder() {}
        public Builder(RulestackProfileConfig defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.antiSpyware = defaults.antiSpyware;
    	      this.antiVirus = defaults.antiVirus;
    	      this.fileBlocking = defaults.fileBlocking;
    	      this.outboundTrustCertificate = defaults.outboundTrustCertificate;
    	      this.outboundUntrustCertificate = defaults.outboundUntrustCertificate;
    	      this.urlFiltering = defaults.urlFiltering;
    	      this.vulnerability = defaults.vulnerability;
        }

        @CustomType.Setter
        public Builder antiSpyware(@Nullable String antiSpyware) {

            this.antiSpyware = antiSpyware;
            return this;
        }
        @CustomType.Setter
        public Builder antiVirus(@Nullable String antiVirus) {

            this.antiVirus = antiVirus;
            return this;
        }
        @CustomType.Setter
        public Builder fileBlocking(@Nullable String fileBlocking) {

            this.fileBlocking = fileBlocking;
            return this;
        }
        @CustomType.Setter
        public Builder outboundTrustCertificate(@Nullable String outboundTrustCertificate) {

            this.outboundTrustCertificate = outboundTrustCertificate;
            return this;
        }
        @CustomType.Setter
        public Builder outboundUntrustCertificate(@Nullable String outboundUntrustCertificate) {

            this.outboundUntrustCertificate = outboundUntrustCertificate;
            return this;
        }
        @CustomType.Setter
        public Builder urlFiltering(@Nullable String urlFiltering) {

            this.urlFiltering = urlFiltering;
            return this;
        }
        @CustomType.Setter
        public Builder vulnerability(@Nullable String vulnerability) {

            this.vulnerability = vulnerability;
            return this;
        }
        public RulestackProfileConfig build() {
            final var _resultValue = new RulestackProfileConfig();
            _resultValue.antiSpyware = antiSpyware;
            _resultValue.antiVirus = antiVirus;
            _resultValue.fileBlocking = fileBlocking;
            _resultValue.outboundTrustCertificate = outboundTrustCertificate;
            _resultValue.outboundUntrustCertificate = outboundUntrustCertificate;
            _resultValue.urlFiltering = urlFiltering;
            _resultValue.vulnerability = vulnerability;
            return _resultValue;
        }
    }
}
