// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Resource for committing the rulestack config.
 *
 * !> **NOTE:** This resource should be placed in a separate plan as the plan that configures the rulestack and its contents.  If you do not, you will have perpetual configuration drift and will need to run your plan twice so the commit is performed.  Placing instances of this resource with instances of NGFW resources (such as `cloudngfwaws.Ngfw`) is fine.
 *
 * ## Admin Permission Type
 *
 * * `Rulestack` (for `scope="Local"`)
 * * `Global Rulestack` (for `scope="Global"`)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudngfwaws from "@pulumi/cloudngfwaws";
 *
 * const example = new cloudngfwaws.CommitRulestack("example", {rulestack: "my-rulestack"});
 * ```
 */
export class CommitRulestack extends pulumi.CustomResource {
    /**
     * Get an existing CommitRulestack resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CommitRulestackState, opts?: pulumi.CustomResourceOptions): CommitRulestack {
        return new CommitRulestack(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudngfwaws:index/commitRulestack:CommitRulestack';

    /**
     * Returns true if the given object is an instance of CommitRulestack.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CommitRulestack {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CommitRulestack.__pulumiType;
    }

    /**
     * Commit error messages.
     */
    public /*out*/ readonly commitErrors!: pulumi.Output<string[]>;
    /**
     * The commit status.
     */
    public /*out*/ readonly commitStatus!: pulumi.Output<string>;
    /**
     * The rulestack.
     */
    public readonly rulestack!: pulumi.Output<string>;
    /**
     * The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     */
    public readonly scope!: pulumi.Output<string | undefined>;
    /**
     * The rulestack state. This can only be the default value. Defaults to `Running`.
     */
    public readonly state!: pulumi.Output<string | undefined>;
    /**
     * Validation error messages.
     */
    public /*out*/ readonly validationErrors!: pulumi.Output<string[]>;
    /**
     * The validation status.
     */
    public /*out*/ readonly validationStatus!: pulumi.Output<string>;

    /**
     * Create a CommitRulestack resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CommitRulestackArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CommitRulestackArgs | CommitRulestackState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CommitRulestackState | undefined;
            resourceInputs["commitErrors"] = state ? state.commitErrors : undefined;
            resourceInputs["commitStatus"] = state ? state.commitStatus : undefined;
            resourceInputs["rulestack"] = state ? state.rulestack : undefined;
            resourceInputs["scope"] = state ? state.scope : undefined;
            resourceInputs["state"] = state ? state.state : undefined;
            resourceInputs["validationErrors"] = state ? state.validationErrors : undefined;
            resourceInputs["validationStatus"] = state ? state.validationStatus : undefined;
        } else {
            const args = argsOrState as CommitRulestackArgs | undefined;
            if ((!args || args.rulestack === undefined) && !opts.urn) {
                throw new Error("Missing required property 'rulestack'");
            }
            resourceInputs["rulestack"] = args ? args.rulestack : undefined;
            resourceInputs["scope"] = args ? args.scope : undefined;
            resourceInputs["state"] = args ? args.state : undefined;
            resourceInputs["commitErrors"] = undefined /*out*/;
            resourceInputs["commitStatus"] = undefined /*out*/;
            resourceInputs["validationErrors"] = undefined /*out*/;
            resourceInputs["validationStatus"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CommitRulestack.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CommitRulestack resources.
 */
export interface CommitRulestackState {
    /**
     * Commit error messages.
     */
    commitErrors?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The commit status.
     */
    commitStatus?: pulumi.Input<string>;
    /**
     * The rulestack.
     */
    rulestack?: pulumi.Input<string>;
    /**
     * The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     */
    scope?: pulumi.Input<string>;
    /**
     * The rulestack state. This can only be the default value. Defaults to `Running`.
     */
    state?: pulumi.Input<string>;
    /**
     * Validation error messages.
     */
    validationErrors?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The validation status.
     */
    validationStatus?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CommitRulestack resource.
 */
export interface CommitRulestackArgs {
    /**
     * The rulestack.
     */
    rulestack: pulumi.Input<string>;
    /**
     * The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     */
    scope?: pulumi.Input<string>;
    /**
     * The rulestack state. This can only be the default value. Defaults to `Running`.
     */
    state?: pulumi.Input<string>;
}
