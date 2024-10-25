// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetPredefinedUrlCategoryOverrideArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetPredefinedUrlCategoryOverrideArgs Empty = new GetPredefinedUrlCategoryOverrideArgs();

    /**
     * Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
     * 
     */
    @Import(name="configType")
    private @Nullable Output<String> configType;

    /**
     * @return Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
     * 
     */
    public Optional<Output<String>> configType() {
        return Optional.ofNullable(this.configType);
    }

    /**
     * The name.
     * 
     */
    @Import(name="name", required=true)
    private Output<String> name;

    /**
     * @return The name.
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    /**
     * The rulestack.
     * 
     */
    @Import(name="rulestack", required=true)
    private Output<String> rulestack;

    /**
     * @return The rulestack.
     * 
     */
    public Output<String> rulestack() {
        return this.rulestack;
    }

    private GetPredefinedUrlCategoryOverrideArgs() {}

    private GetPredefinedUrlCategoryOverrideArgs(GetPredefinedUrlCategoryOverrideArgs $) {
        this.configType = $.configType;
        this.name = $.name;
        this.rulestack = $.rulestack;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetPredefinedUrlCategoryOverrideArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetPredefinedUrlCategoryOverrideArgs $;

        public Builder() {
            $ = new GetPredefinedUrlCategoryOverrideArgs();
        }

        public Builder(GetPredefinedUrlCategoryOverrideArgs defaults) {
            $ = new GetPredefinedUrlCategoryOverrideArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param configType Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
         * 
         * @return builder
         * 
         */
        public Builder configType(@Nullable Output<String> configType) {
            $.configType = configType;
            return this;
        }

        /**
         * @param configType Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
         * 
         * @return builder
         * 
         */
        public Builder configType(String configType) {
            return configType(Output.of(configType));
        }

        /**
         * @param name The name.
         * 
         * @return builder
         * 
         */
        public Builder name(Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param rulestack The rulestack.
         * 
         * @return builder
         * 
         */
        public Builder rulestack(Output<String> rulestack) {
            $.rulestack = rulestack;
            return this;
        }

        /**
         * @param rulestack The rulestack.
         * 
         * @return builder
         * 
         */
        public Builder rulestack(String rulestack) {
            return rulestack(Output.of(rulestack));
        }

        public GetPredefinedUrlCategoryOverrideArgs build() {
            if ($.name == null) {
                throw new MissingRequiredPropertyException("GetPredefinedUrlCategoryOverrideArgs", "name");
            }
            if ($.rulestack == null) {
                throw new MissingRequiredPropertyException("GetPredefinedUrlCategoryOverrideArgs", "rulestack");
            }
            return $;
        }
    }

}
