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


public final class GetRulestackArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetRulestackArgs Empty = new GetRulestackArgs();

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
     * The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     * 
     */
    @Import(name="scope")
    private @Nullable Output<String> scope;

    /**
     * @return The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     * 
     */
    public Optional<Output<String>> scope() {
        return Optional.ofNullable(this.scope);
    }

    private GetRulestackArgs() {}

    private GetRulestackArgs(GetRulestackArgs $) {
        this.configType = $.configType;
        this.name = $.name;
        this.scope = $.scope;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetRulestackArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetRulestackArgs $;

        public Builder() {
            $ = new GetRulestackArgs();
        }

        public Builder(GetRulestackArgs defaults) {
            $ = new GetRulestackArgs(Objects.requireNonNull(defaults));
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
         * @param scope The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
         * 
         * @return builder
         * 
         */
        public Builder scope(@Nullable Output<String> scope) {
            $.scope = scope;
            return this;
        }

        /**
         * @param scope The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
         * 
         * @return builder
         * 
         */
        public Builder scope(String scope) {
            return scope(Output.of(scope));
        }

        public GetRulestackArgs build() {
            if ($.name == null) {
                throw new MissingRequiredPropertyException("GetRulestackArgs", "name");
            }
            return $;
        }
    }

}
