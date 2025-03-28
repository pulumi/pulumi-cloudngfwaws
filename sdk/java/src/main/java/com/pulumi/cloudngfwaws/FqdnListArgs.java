// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class FqdnListArgs extends com.pulumi.resources.ResourceArgs {

    public static final FqdnListArgs Empty = new FqdnListArgs();

    /**
     * The audit comment.
     * 
     */
    @Import(name="auditComment")
    private @Nullable Output<String> auditComment;

    /**
     * @return The audit comment.
     * 
     */
    public Optional<Output<String>> auditComment() {
        return Optional.ofNullable(this.auditComment);
    }

    /**
     * The description.
     * 
     */
    @Import(name="description")
    private @Nullable Output<String> description;

    /**
     * @return The description.
     * 
     */
    public Optional<Output<String>> description() {
        return Optional.ofNullable(this.description);
    }

    /**
     * The fqdn list.
     * 
     */
    @Import(name="fqdnLists", required=true)
    private Output<List<String>> fqdnLists;

    /**
     * @return The fqdn list.
     * 
     */
    public Output<List<String>> fqdnLists() {
        return this.fqdnLists;
    }

    /**
     * The name.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
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

    private FqdnListArgs() {}

    private FqdnListArgs(FqdnListArgs $) {
        this.auditComment = $.auditComment;
        this.description = $.description;
        this.fqdnLists = $.fqdnLists;
        this.name = $.name;
        this.rulestack = $.rulestack;
        this.scope = $.scope;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(FqdnListArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private FqdnListArgs $;

        public Builder() {
            $ = new FqdnListArgs();
        }

        public Builder(FqdnListArgs defaults) {
            $ = new FqdnListArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param auditComment The audit comment.
         * 
         * @return builder
         * 
         */
        public Builder auditComment(@Nullable Output<String> auditComment) {
            $.auditComment = auditComment;
            return this;
        }

        /**
         * @param auditComment The audit comment.
         * 
         * @return builder
         * 
         */
        public Builder auditComment(String auditComment) {
            return auditComment(Output.of(auditComment));
        }

        /**
         * @param description The description.
         * 
         * @return builder
         * 
         */
        public Builder description(@Nullable Output<String> description) {
            $.description = description;
            return this;
        }

        /**
         * @param description The description.
         * 
         * @return builder
         * 
         */
        public Builder description(String description) {
            return description(Output.of(description));
        }

        /**
         * @param fqdnLists The fqdn list.
         * 
         * @return builder
         * 
         */
        public Builder fqdnLists(Output<List<String>> fqdnLists) {
            $.fqdnLists = fqdnLists;
            return this;
        }

        /**
         * @param fqdnLists The fqdn list.
         * 
         * @return builder
         * 
         */
        public Builder fqdnLists(List<String> fqdnLists) {
            return fqdnLists(Output.of(fqdnLists));
        }

        /**
         * @param fqdnLists The fqdn list.
         * 
         * @return builder
         * 
         */
        public Builder fqdnLists(String... fqdnLists) {
            return fqdnLists(List.of(fqdnLists));
        }

        /**
         * @param name The name.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
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

        public FqdnListArgs build() {
            if ($.fqdnLists == null) {
                throw new MissingRequiredPropertyException("FqdnListArgs", "fqdnLists");
            }
            if ($.rulestack == null) {
                throw new MissingRequiredPropertyException("FqdnListArgs", "rulestack");
            }
            return $;
        }
    }

}
