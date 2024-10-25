// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetPrefixListPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetPrefixListPlainArgs Empty = new GetPrefixListPlainArgs();

    /**
     * Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
     * 
     */
    @Import(name="configType")
    private @Nullable String configType;

    /**
     * @return Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
     * 
     */
    public Optional<String> configType() {
        return Optional.ofNullable(this.configType);
    }

    /**
     * The name.
     * 
     */
    @Import(name="name", required=true)
    private String name;

    /**
     * @return The name.
     * 
     */
    public String name() {
        return this.name;
    }

    /**
     * The rulestack.
     * 
     */
    @Import(name="rulestack", required=true)
    private String rulestack;

    /**
     * @return The rulestack.
     * 
     */
    public String rulestack() {
        return this.rulestack;
    }

    /**
     * The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     * 
     */
    @Import(name="scope")
    private @Nullable String scope;

    /**
     * @return The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     * 
     */
    public Optional<String> scope() {
        return Optional.ofNullable(this.scope);
    }

    private GetPrefixListPlainArgs() {}

    private GetPrefixListPlainArgs(GetPrefixListPlainArgs $) {
        this.configType = $.configType;
        this.name = $.name;
        this.rulestack = $.rulestack;
        this.scope = $.scope;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetPrefixListPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetPrefixListPlainArgs $;

        public Builder() {
            $ = new GetPrefixListPlainArgs();
        }

        public Builder(GetPrefixListPlainArgs defaults) {
            $ = new GetPrefixListPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param configType Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
         * 
         * @return builder
         * 
         */
        public Builder configType(@Nullable String configType) {
            $.configType = configType;
            return this;
        }

        /**
         * @param name The name.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            $.name = name;
            return this;
        }

        /**
         * @param rulestack The rulestack.
         * 
         * @return builder
         * 
         */
        public Builder rulestack(String rulestack) {
            $.rulestack = rulestack;
            return this;
        }

        /**
         * @param scope The rulestack&#39;s scope. A local rulestack will require that you&#39;ve retrieved a LRA JWT. A global rulestack will require that you&#39;ve retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
         * 
         * @return builder
         * 
         */
        public Builder scope(@Nullable String scope) {
            $.scope = scope;
            return this;
        }

        public GetPrefixListPlainArgs build() {
            if ($.name == null) {
                throw new MissingRequiredPropertyException("GetPrefixListPlainArgs", "name");
            }
            if ($.rulestack == null) {
                throw new MissingRequiredPropertyException("GetPrefixListPlainArgs", "rulestack");
            }
            return $;
        }
    }

}
