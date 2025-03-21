// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cloudngfwaws.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class CommitRulestackState extends com.pulumi.resources.ResourceArgs {

    public static final CommitRulestackState Empty = new CommitRulestackState();

    /**
     * Commit error messages.
     * 
     */
    @Import(name="commitErrors")
    private @Nullable Output<List<String>> commitErrors;

    /**
     * @return Commit error messages.
     * 
     */
    public Optional<Output<List<String>>> commitErrors() {
        return Optional.ofNullable(this.commitErrors);
    }

    /**
     * The commit status.
     * 
     */
    @Import(name="commitStatus")
    private @Nullable Output<String> commitStatus;

    /**
     * @return The commit status.
     * 
     */
    public Optional<Output<String>> commitStatus() {
        return Optional.ofNullable(this.commitStatus);
    }

    /**
     * The rulestack.
     * 
     */
    @Import(name="rulestack")
    private @Nullable Output<String> rulestack;

    /**
     * @return The rulestack.
     * 
     */
    public Optional<Output<String>> rulestack() {
        return Optional.ofNullable(this.rulestack);
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

    /**
     * The rulestack state. This can only be the default value. Defaults to `Running`.
     * 
     */
    @Import(name="state")
    private @Nullable Output<String> state;

    /**
     * @return The rulestack state. This can only be the default value. Defaults to `Running`.
     * 
     */
    public Optional<Output<String>> state() {
        return Optional.ofNullable(this.state);
    }

    /**
     * Validation error messages.
     * 
     */
    @Import(name="validationErrors")
    private @Nullable Output<List<String>> validationErrors;

    /**
     * @return Validation error messages.
     * 
     */
    public Optional<Output<List<String>>> validationErrors() {
        return Optional.ofNullable(this.validationErrors);
    }

    /**
     * The validation status.
     * 
     */
    @Import(name="validationStatus")
    private @Nullable Output<String> validationStatus;

    /**
     * @return The validation status.
     * 
     */
    public Optional<Output<String>> validationStatus() {
        return Optional.ofNullable(this.validationStatus);
    }

    private CommitRulestackState() {}

    private CommitRulestackState(CommitRulestackState $) {
        this.commitErrors = $.commitErrors;
        this.commitStatus = $.commitStatus;
        this.rulestack = $.rulestack;
        this.scope = $.scope;
        this.state = $.state;
        this.validationErrors = $.validationErrors;
        this.validationStatus = $.validationStatus;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(CommitRulestackState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private CommitRulestackState $;

        public Builder() {
            $ = new CommitRulestackState();
        }

        public Builder(CommitRulestackState defaults) {
            $ = new CommitRulestackState(Objects.requireNonNull(defaults));
        }

        /**
         * @param commitErrors Commit error messages.
         * 
         * @return builder
         * 
         */
        public Builder commitErrors(@Nullable Output<List<String>> commitErrors) {
            $.commitErrors = commitErrors;
            return this;
        }

        /**
         * @param commitErrors Commit error messages.
         * 
         * @return builder
         * 
         */
        public Builder commitErrors(List<String> commitErrors) {
            return commitErrors(Output.of(commitErrors));
        }

        /**
         * @param commitErrors Commit error messages.
         * 
         * @return builder
         * 
         */
        public Builder commitErrors(String... commitErrors) {
            return commitErrors(List.of(commitErrors));
        }

        /**
         * @param commitStatus The commit status.
         * 
         * @return builder
         * 
         */
        public Builder commitStatus(@Nullable Output<String> commitStatus) {
            $.commitStatus = commitStatus;
            return this;
        }

        /**
         * @param commitStatus The commit status.
         * 
         * @return builder
         * 
         */
        public Builder commitStatus(String commitStatus) {
            return commitStatus(Output.of(commitStatus));
        }

        /**
         * @param rulestack The rulestack.
         * 
         * @return builder
         * 
         */
        public Builder rulestack(@Nullable Output<String> rulestack) {
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

        /**
         * @param state The rulestack state. This can only be the default value. Defaults to `Running`.
         * 
         * @return builder
         * 
         */
        public Builder state(@Nullable Output<String> state) {
            $.state = state;
            return this;
        }

        /**
         * @param state The rulestack state. This can only be the default value. Defaults to `Running`.
         * 
         * @return builder
         * 
         */
        public Builder state(String state) {
            return state(Output.of(state));
        }

        /**
         * @param validationErrors Validation error messages.
         * 
         * @return builder
         * 
         */
        public Builder validationErrors(@Nullable Output<List<String>> validationErrors) {
            $.validationErrors = validationErrors;
            return this;
        }

        /**
         * @param validationErrors Validation error messages.
         * 
         * @return builder
         * 
         */
        public Builder validationErrors(List<String> validationErrors) {
            return validationErrors(Output.of(validationErrors));
        }

        /**
         * @param validationErrors Validation error messages.
         * 
         * @return builder
         * 
         */
        public Builder validationErrors(String... validationErrors) {
            return validationErrors(List.of(validationErrors));
        }

        /**
         * @param validationStatus The validation status.
         * 
         * @return builder
         * 
         */
        public Builder validationStatus(@Nullable Output<String> validationStatus) {
            $.validationStatus = validationStatus;
            return this;
        }

        /**
         * @param validationStatus The validation status.
         * 
         * @return builder
         * 
         */
        public Builder validationStatus(String validationStatus) {
            return validationStatus(Output.of(validationStatus));
        }

        public CommitRulestackState build() {
            return $;
        }
    }

}
