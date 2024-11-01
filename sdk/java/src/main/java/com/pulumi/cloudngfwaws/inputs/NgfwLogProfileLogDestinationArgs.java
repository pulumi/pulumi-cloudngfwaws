// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class NgfwLogProfileLogDestinationArgs extends com.pulumi.resources.ResourceArgs {

    public static final NgfwLogProfileLogDestinationArgs Empty = new NgfwLogProfileLogDestinationArgs();

    /**
     * The log destination details.
     * 
     */
    @Import(name="destination")
    private @Nullable Output<String> destination;

    /**
     * @return The log destination details.
     * 
     */
    public Optional<Output<String>> destination() {
        return Optional.ofNullable(this.destination);
    }

    /**
     * The log destination type. Valid values are `S3`, `CloudWatchLogs`, or `KinesisDataFirehose`.
     * 
     */
    @Import(name="destinationType")
    private @Nullable Output<String> destinationType;

    /**
     * @return The log destination type. Valid values are `S3`, `CloudWatchLogs`, or `KinesisDataFirehose`.
     * 
     */
    public Optional<Output<String>> destinationType() {
        return Optional.ofNullable(this.destinationType);
    }

    /**
     * The type of logs. Valid values are `TRAFFIC`, `THREAT`, or `DECRYPTION`.
     * 
     */
    @Import(name="logType")
    private @Nullable Output<String> logType;

    /**
     * @return The type of logs. Valid values are `TRAFFIC`, `THREAT`, or `DECRYPTION`.
     * 
     */
    public Optional<Output<String>> logType() {
        return Optional.ofNullable(this.logType);
    }

    private NgfwLogProfileLogDestinationArgs() {}

    private NgfwLogProfileLogDestinationArgs(NgfwLogProfileLogDestinationArgs $) {
        this.destination = $.destination;
        this.destinationType = $.destinationType;
        this.logType = $.logType;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(NgfwLogProfileLogDestinationArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private NgfwLogProfileLogDestinationArgs $;

        public Builder() {
            $ = new NgfwLogProfileLogDestinationArgs();
        }

        public Builder(NgfwLogProfileLogDestinationArgs defaults) {
            $ = new NgfwLogProfileLogDestinationArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param destination The log destination details.
         * 
         * @return builder
         * 
         */
        public Builder destination(@Nullable Output<String> destination) {
            $.destination = destination;
            return this;
        }

        /**
         * @param destination The log destination details.
         * 
         * @return builder
         * 
         */
        public Builder destination(String destination) {
            return destination(Output.of(destination));
        }

        /**
         * @param destinationType The log destination type. Valid values are `S3`, `CloudWatchLogs`, or `KinesisDataFirehose`.
         * 
         * @return builder
         * 
         */
        public Builder destinationType(@Nullable Output<String> destinationType) {
            $.destinationType = destinationType;
            return this;
        }

        /**
         * @param destinationType The log destination type. Valid values are `S3`, `CloudWatchLogs`, or `KinesisDataFirehose`.
         * 
         * @return builder
         * 
         */
        public Builder destinationType(String destinationType) {
            return destinationType(Output.of(destinationType));
        }

        /**
         * @param logType The type of logs. Valid values are `TRAFFIC`, `THREAT`, or `DECRYPTION`.
         * 
         * @return builder
         * 
         */
        public Builder logType(@Nullable Output<String> logType) {
            $.logType = logType;
            return this;
        }

        /**
         * @param logType The type of logs. Valid values are `TRAFFIC`, `THREAT`, or `DECRYPTION`.
         * 
         * @return builder
         * 
         */
        public Builder logType(String logType) {
            return logType(Output.of(logType));
        }

        public NgfwLogProfileLogDestinationArgs build() {
            return $;
        }
    }

}
