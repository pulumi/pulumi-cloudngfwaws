// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Resource for rulestack manipulation.
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
 * const example = new cloudngfwaws.Rulestack("example", {
 *     name: "terraform-rulestack",
 *     scope: "Local",
 *     accountId: "123456789",
 *     description: "Made by Pulumi",
 *     profileConfig: {
 *         antiSpyware: "BestPractice",
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * import name is <scope>:<rulestack>
 *
 * ```sh
 * $ pulumi import cloudngfwaws:index/rulestack:Rulestack example Local:terraform-rulestack
 * ```
 */
export class Rulestack extends pulumi.CustomResource {
    /**
     * Get an existing Rulestack resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RulestackState, opts?: pulumi.CustomResourceOptions): Rulestack {
        return new Rulestack(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudngfwaws:index/rulestack:Rulestack';

    /**
     * Returns true if the given object is an instance of Rulestack.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Rulestack {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Rulestack.__pulumiType;
    }

    /**
     * Account group.
     */
    public readonly accountGroup!: pulumi.Output<string | undefined>;
    /**
     * The account ID.
     */
    public readonly accountId!: pulumi.Output<string | undefined>;
    /**
     * The description.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Lookup x forwarded for.
     */
    public readonly lookupXForwardedFor!: pulumi.Output<string>;
    /**
     * Minimum App-ID version number.
     */
    public readonly minimumAppIdVersion!: pulumi.Output<string>;
    /**
     * The name.
     */
    public readonly name!: pulumi.Output<string>;
    public readonly profileConfig!: pulumi.Output<outputs.RulestackProfileConfig>;
    /**
     * The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     */
    public readonly scope!: pulumi.Output<string | undefined>;
    /**
     * The rulestack state.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * The tags.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Rulestack resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RulestackArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RulestackArgs | RulestackState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RulestackState | undefined;
            resourceInputs["accountGroup"] = state ? state.accountGroup : undefined;
            resourceInputs["accountId"] = state ? state.accountId : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["lookupXForwardedFor"] = state ? state.lookupXForwardedFor : undefined;
            resourceInputs["minimumAppIdVersion"] = state ? state.minimumAppIdVersion : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["profileConfig"] = state ? state.profileConfig : undefined;
            resourceInputs["scope"] = state ? state.scope : undefined;
            resourceInputs["state"] = state ? state.state : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as RulestackArgs | undefined;
            if ((!args || args.profileConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'profileConfig'");
            }
            resourceInputs["accountGroup"] = args ? args.accountGroup : undefined;
            resourceInputs["accountId"] = args ? args.accountId : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["lookupXForwardedFor"] = args ? args.lookupXForwardedFor : undefined;
            resourceInputs["minimumAppIdVersion"] = args ? args.minimumAppIdVersion : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["profileConfig"] = args ? args.profileConfig : undefined;
            resourceInputs["scope"] = args ? args.scope : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["state"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Rulestack.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Rulestack resources.
 */
export interface RulestackState {
    /**
     * Account group.
     */
    accountGroup?: pulumi.Input<string>;
    /**
     * The account ID.
     */
    accountId?: pulumi.Input<string>;
    /**
     * The description.
     */
    description?: pulumi.Input<string>;
    /**
     * Lookup x forwarded for.
     */
    lookupXForwardedFor?: pulumi.Input<string>;
    /**
     * Minimum App-ID version number.
     */
    minimumAppIdVersion?: pulumi.Input<string>;
    /**
     * The name.
     */
    name?: pulumi.Input<string>;
    profileConfig?: pulumi.Input<inputs.RulestackProfileConfig>;
    /**
     * The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     */
    scope?: pulumi.Input<string>;
    /**
     * The rulestack state.
     */
    state?: pulumi.Input<string>;
    /**
     * The tags.
     */
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a Rulestack resource.
 */
export interface RulestackArgs {
    /**
     * Account group.
     */
    accountGroup?: pulumi.Input<string>;
    /**
     * The account ID.
     */
    accountId?: pulumi.Input<string>;
    /**
     * The description.
     */
    description?: pulumi.Input<string>;
    /**
     * Lookup x forwarded for.
     */
    lookupXForwardedFor?: pulumi.Input<string>;
    /**
     * Minimum App-ID version number.
     */
    minimumAppIdVersion?: pulumi.Input<string>;
    /**
     * The name.
     */
    name?: pulumi.Input<string>;
    profileConfig: pulumi.Input<inputs.RulestackProfileConfig>;
    /**
     * The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     */
    scope?: pulumi.Input<string>;
    /**
     * The tags.
     */
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
