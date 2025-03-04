// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class RulestackProfileConfigArgs extends com.pulumi.resources.ResourceArgs {

    public static final RulestackProfileConfigArgs Empty = new RulestackProfileConfigArgs();

    /**
     * Anti-spyware profile setting. Defaults to `BestPractice`.
     * 
     */
    @Import(name="antiSpyware")
    private @Nullable Output<String> antiSpyware;

    /**
     * @return Anti-spyware profile setting. Defaults to `BestPractice`.
     * 
     */
    public Optional<Output<String>> antiSpyware() {
        return Optional.ofNullable(this.antiSpyware);
    }

    /**
     * Anti-virus profile setting. Defaults to `BestPractice`.
     * 
     */
    @Import(name="antiVirus")
    private @Nullable Output<String> antiVirus;

    /**
     * @return Anti-virus profile setting. Defaults to `BestPractice`.
     * 
     */
    public Optional<Output<String>> antiVirus() {
        return Optional.ofNullable(this.antiVirus);
    }

    /**
     * File blocking profile setting. Defaults to `BestPractice`.
     * 
     */
    @Import(name="fileBlocking")
    private @Nullable Output<String> fileBlocking;

    /**
     * @return File blocking profile setting. Defaults to `BestPractice`.
     * 
     */
    public Optional<Output<String>> fileBlocking() {
        return Optional.ofNullable(this.fileBlocking);
    }

    /**
     * Outbound trust certificate.
     * 
     */
    @Import(name="outboundTrustCertificate")
    private @Nullable Output<String> outboundTrustCertificate;

    /**
     * @return Outbound trust certificate.
     * 
     */
    public Optional<Output<String>> outboundTrustCertificate() {
        return Optional.ofNullable(this.outboundTrustCertificate);
    }

    /**
     * Outbound untrust certificate.
     * 
     */
    @Import(name="outboundUntrustCertificate")
    private @Nullable Output<String> outboundUntrustCertificate;

    /**
     * @return Outbound untrust certificate.
     * 
     */
    public Optional<Output<String>> outboundUntrustCertificate() {
        return Optional.ofNullable(this.outboundUntrustCertificate);
    }

    /**
     * URL filtering profile setting. Defaults to `None`.
     * 
     */
    @Import(name="urlFiltering")
    private @Nullable Output<String> urlFiltering;

    /**
     * @return URL filtering profile setting. Defaults to `None`.
     * 
     */
    public Optional<Output<String>> urlFiltering() {
        return Optional.ofNullable(this.urlFiltering);
    }

    /**
     * Vulnerability profile setting. Defaults to `BestPractice`.
     * 
     */
    @Import(name="vulnerability")
    private @Nullable Output<String> vulnerability;

    /**
     * @return Vulnerability profile setting. Defaults to `BestPractice`.
     * 
     */
    public Optional<Output<String>> vulnerability() {
        return Optional.ofNullable(this.vulnerability);
    }

    private RulestackProfileConfigArgs() {}

    private RulestackProfileConfigArgs(RulestackProfileConfigArgs $) {
        this.antiSpyware = $.antiSpyware;
        this.antiVirus = $.antiVirus;
        this.fileBlocking = $.fileBlocking;
        this.outboundTrustCertificate = $.outboundTrustCertificate;
        this.outboundUntrustCertificate = $.outboundUntrustCertificate;
        this.urlFiltering = $.urlFiltering;
        this.vulnerability = $.vulnerability;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(RulestackProfileConfigArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private RulestackProfileConfigArgs $;

        public Builder() {
            $ = new RulestackProfileConfigArgs();
        }

        public Builder(RulestackProfileConfigArgs defaults) {
            $ = new RulestackProfileConfigArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param antiSpyware Anti-spyware profile setting. Defaults to `BestPractice`.
         * 
         * @return builder
         * 
         */
        public Builder antiSpyware(@Nullable Output<String> antiSpyware) {
            $.antiSpyware = antiSpyware;
            return this;
        }

        /**
         * @param antiSpyware Anti-spyware profile setting. Defaults to `BestPractice`.
         * 
         * @return builder
         * 
         */
        public Builder antiSpyware(String antiSpyware) {
            return antiSpyware(Output.of(antiSpyware));
        }

        /**
         * @param antiVirus Anti-virus profile setting. Defaults to `BestPractice`.
         * 
         * @return builder
         * 
         */
        public Builder antiVirus(@Nullable Output<String> antiVirus) {
            $.antiVirus = antiVirus;
            return this;
        }

        /**
         * @param antiVirus Anti-virus profile setting. Defaults to `BestPractice`.
         * 
         * @return builder
         * 
         */
        public Builder antiVirus(String antiVirus) {
            return antiVirus(Output.of(antiVirus));
        }

        /**
         * @param fileBlocking File blocking profile setting. Defaults to `BestPractice`.
         * 
         * @return builder
         * 
         */
        public Builder fileBlocking(@Nullable Output<String> fileBlocking) {
            $.fileBlocking = fileBlocking;
            return this;
        }

        /**
         * @param fileBlocking File blocking profile setting. Defaults to `BestPractice`.
         * 
         * @return builder
         * 
         */
        public Builder fileBlocking(String fileBlocking) {
            return fileBlocking(Output.of(fileBlocking));
        }

        /**
         * @param outboundTrustCertificate Outbound trust certificate.
         * 
         * @return builder
         * 
         */
        public Builder outboundTrustCertificate(@Nullable Output<String> outboundTrustCertificate) {
            $.outboundTrustCertificate = outboundTrustCertificate;
            return this;
        }

        /**
         * @param outboundTrustCertificate Outbound trust certificate.
         * 
         * @return builder
         * 
         */
        public Builder outboundTrustCertificate(String outboundTrustCertificate) {
            return outboundTrustCertificate(Output.of(outboundTrustCertificate));
        }

        /**
         * @param outboundUntrustCertificate Outbound untrust certificate.
         * 
         * @return builder
         * 
         */
        public Builder outboundUntrustCertificate(@Nullable Output<String> outboundUntrustCertificate) {
            $.outboundUntrustCertificate = outboundUntrustCertificate;
            return this;
        }

        /**
         * @param outboundUntrustCertificate Outbound untrust certificate.
         * 
         * @return builder
         * 
         */
        public Builder outboundUntrustCertificate(String outboundUntrustCertificate) {
            return outboundUntrustCertificate(Output.of(outboundUntrustCertificate));
        }

        /**
         * @param urlFiltering URL filtering profile setting. Defaults to `None`.
         * 
         * @return builder
         * 
         */
        public Builder urlFiltering(@Nullable Output<String> urlFiltering) {
            $.urlFiltering = urlFiltering;
            return this;
        }

        /**
         * @param urlFiltering URL filtering profile setting. Defaults to `None`.
         * 
         * @return builder
         * 
         */
        public Builder urlFiltering(String urlFiltering) {
            return urlFiltering(Output.of(urlFiltering));
        }

        /**
         * @param vulnerability Vulnerability profile setting. Defaults to `BestPractice`.
         * 
         * @return builder
         * 
         */
        public Builder vulnerability(@Nullable Output<String> vulnerability) {
            $.vulnerability = vulnerability;
            return this;
        }

        /**
         * @param vulnerability Vulnerability profile setting. Defaults to `BestPractice`.
         * 
         * @return builder
         * 
         */
        public Builder vulnerability(String vulnerability) {
            return vulnerability(Output.of(vulnerability));
        }

        public RulestackProfileConfigArgs build() {
            return $;
        }
    }

}
