// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Resource for Account Onboarding.
 *
 * ## Admin Permission Type
 *
 * * `Rulestack` (for `scope="Local"`)
 * * `Global Rulestack` (for `scope="Global"`)
 */
export class AccountOnboarding extends pulumi.CustomResource {
    /**
     * Get an existing AccountOnboarding resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountOnboardingState, opts?: pulumi.CustomResourceOptions): AccountOnboarding {
        return new AccountOnboarding(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudngfwaws:index/accountOnboarding:AccountOnboarding';

    /**
     * Returns true if the given object is an instance of AccountOnboarding.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AccountOnboarding {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AccountOnboarding.__pulumiType;
    }

    /**
     * The account IDs
     */
    public readonly accountId!: pulumi.Output<string>;
    /**
     * Onboarding status of the account
     */
    public readonly onboardingStatus!: pulumi.Output<string>;

    /**
     * Create a AccountOnboarding resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AccountOnboardingArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AccountOnboardingArgs | AccountOnboardingState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AccountOnboardingState | undefined;
            resourceInputs["accountId"] = state ? state.accountId : undefined;
            resourceInputs["onboardingStatus"] = state ? state.onboardingStatus : undefined;
        } else {
            const args = argsOrState as AccountOnboardingArgs | undefined;
            if ((!args || args.accountId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accountId'");
            }
            resourceInputs["accountId"] = args ? args.accountId : undefined;
            resourceInputs["onboardingStatus"] = args ? args.onboardingStatus : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AccountOnboarding.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AccountOnboarding resources.
 */
export interface AccountOnboardingState {
    /**
     * The account IDs
     */
    accountId?: pulumi.Input<string>;
    /**
     * Onboarding status of the account
     */
    onboardingStatus?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AccountOnboarding resource.
 */
export interface AccountOnboardingArgs {
    /**
     * The account IDs
     */
    accountId: pulumi.Input<string>;
    /**
     * Onboarding status of the account
     */
    onboardingStatus?: pulumi.Input<string>;
}
