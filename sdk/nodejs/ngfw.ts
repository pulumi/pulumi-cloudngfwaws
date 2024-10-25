// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as cloudngfwaws from "@pulumi/cloudngfwaws";
 *
 * const rs = new cloudngfwaws.CommitRulestack("rs", {rulestack: "my-rulestack"});
 * const exampleVpc = new aws.index.Vpc("example", {
 *     cidrBlock: "172.16.0.0/16",
 *     tags: {
 *         name: "tf-example",
 *     },
 * });
 * const subnet1 = new aws.index.Subnet("subnet1", {
 *     vpcId: myVpc.id,
 *     cidrBlock: "172.16.10.0/24",
 *     availabilityZone: "us-west-2a",
 *     tags: {
 *         name: "tf-example",
 *     },
 * });
 * const subnet2 = new aws.index.Subnet("subnet2", {
 *     vpcId: myVpc.id,
 *     cidrBlock: "172.16.20.0/24",
 *     availabilityZone: "us-west-2b",
 *     tags: {
 *         name: "tf-example",
 *     },
 * });
 * const example = new cloudngfwaws.Ngfw("example", {
 *     name: "example-instance",
 *     vpcId: exampleVpc.id,
 *     accountId: "12345678",
 *     description: "Example description",
 *     linkId: "Link-81e80ccc-357a-4e4e-8325-1ed1d830cba5",
 *     endpointMode: "ServiceManaged",
 *     subnetMappings: [
 *         {
 *             subnetId: subnet1.id,
 *         },
 *         {
 *             subnetId: subnet2.id,
 *         },
 *     ],
 *     rulestack: rs.rulestack,
 *     tags: {
 *         Foo: "bar",
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * import name is <account_id>:<name>
 *
 * ```sh
 * $ pulumi import cloudngfwaws:index/ngfw:Ngfw example 12345678:example-instance
 * ```
 */
export class Ngfw extends pulumi.CustomResource {
    /**
     * Get an existing Ngfw resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NgfwState, opts?: pulumi.CustomResourceOptions): Ngfw {
        return new Ngfw(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudngfwaws:index/ngfw:Ngfw';

    /**
     * Returns true if the given object is an instance of Ngfw.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Ngfw {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Ngfw.__pulumiType;
    }

    /**
     * The account ID. This field is mandatory if using multiple accounts.
     */
    public readonly accountId!: pulumi.Output<string | undefined>;
    /**
     * App-ID version number.
     */
    public readonly appIdVersion!: pulumi.Output<string>;
    /**
     * Automatic App-ID upgrade version number. Defaults to `true`.
     */
    public readonly automaticUpgradeAppIdVersion!: pulumi.Output<boolean | undefined>;
    /**
     * The description.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
     */
    public readonly endpointMode!: pulumi.Output<string>;
    /**
     * The endpoint service name.
     */
    public /*out*/ readonly endpointServiceName!: pulumi.Output<string>;
    /**
     * The Id of the NGFW.
     */
    public /*out*/ readonly firewallId!: pulumi.Output<string>;
    /**
     * The global rulestack for this NGFW.
     */
    public readonly globalRulestack!: pulumi.Output<string | undefined>;
    /**
     * A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
     */
    public readonly linkId!: pulumi.Output<string>;
    /**
     * The link status.
     */
    public /*out*/ readonly linkStatus!: pulumi.Output<string>;
    /**
     * Share NGFW with Multiple VPCs. This feature can be enabled only if the endpointMode is CustomerManaged.
     */
    public readonly multiVpc!: pulumi.Output<boolean>;
    /**
     * The NGFW name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The rulestack for this NGFW.
     */
    public readonly rulestack!: pulumi.Output<string | undefined>;
    public /*out*/ readonly statuses!: pulumi.Output<outputs.NgfwStatus[]>;
    /**
     * Subnet mappings.
     */
    public readonly subnetMappings!: pulumi.Output<outputs.NgfwSubnetMapping[]>;
    /**
     * The tags.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The update token.
     */
    public /*out*/ readonly updateToken!: pulumi.Output<string>;
    /**
     * The vpc id.
     */
    public readonly vpcId!: pulumi.Output<string>;

    /**
     * Create a Ngfw resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NgfwArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NgfwArgs | NgfwState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NgfwState | undefined;
            resourceInputs["accountId"] = state ? state.accountId : undefined;
            resourceInputs["appIdVersion"] = state ? state.appIdVersion : undefined;
            resourceInputs["automaticUpgradeAppIdVersion"] = state ? state.automaticUpgradeAppIdVersion : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["endpointMode"] = state ? state.endpointMode : undefined;
            resourceInputs["endpointServiceName"] = state ? state.endpointServiceName : undefined;
            resourceInputs["firewallId"] = state ? state.firewallId : undefined;
            resourceInputs["globalRulestack"] = state ? state.globalRulestack : undefined;
            resourceInputs["linkId"] = state ? state.linkId : undefined;
            resourceInputs["linkStatus"] = state ? state.linkStatus : undefined;
            resourceInputs["multiVpc"] = state ? state.multiVpc : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["rulestack"] = state ? state.rulestack : undefined;
            resourceInputs["statuses"] = state ? state.statuses : undefined;
            resourceInputs["subnetMappings"] = state ? state.subnetMappings : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
            resourceInputs["updateToken"] = state ? state.updateToken : undefined;
            resourceInputs["vpcId"] = state ? state.vpcId : undefined;
        } else {
            const args = argsOrState as NgfwArgs | undefined;
            if ((!args || args.endpointMode === undefined) && !opts.urn) {
                throw new Error("Missing required property 'endpointMode'");
            }
            if ((!args || args.subnetMappings === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetMappings'");
            }
            if ((!args || args.vpcId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcId'");
            }
            resourceInputs["accountId"] = args ? args.accountId : undefined;
            resourceInputs["appIdVersion"] = args ? args.appIdVersion : undefined;
            resourceInputs["automaticUpgradeAppIdVersion"] = args ? args.automaticUpgradeAppIdVersion : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["endpointMode"] = args ? args.endpointMode : undefined;
            resourceInputs["globalRulestack"] = args ? args.globalRulestack : undefined;
            resourceInputs["linkId"] = args ? args.linkId : undefined;
            resourceInputs["multiVpc"] = args ? args.multiVpc : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["rulestack"] = args ? args.rulestack : undefined;
            resourceInputs["subnetMappings"] = args ? args.subnetMappings : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["vpcId"] = args ? args.vpcId : undefined;
            resourceInputs["endpointServiceName"] = undefined /*out*/;
            resourceInputs["firewallId"] = undefined /*out*/;
            resourceInputs["linkStatus"] = undefined /*out*/;
            resourceInputs["statuses"] = undefined /*out*/;
            resourceInputs["updateToken"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Ngfw.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Ngfw resources.
 */
export interface NgfwState {
    /**
     * The account ID. This field is mandatory if using multiple accounts.
     */
    accountId?: pulumi.Input<string>;
    /**
     * App-ID version number.
     */
    appIdVersion?: pulumi.Input<string>;
    /**
     * Automatic App-ID upgrade version number. Defaults to `true`.
     */
    automaticUpgradeAppIdVersion?: pulumi.Input<boolean>;
    /**
     * The description.
     */
    description?: pulumi.Input<string>;
    /**
     * Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
     */
    endpointMode?: pulumi.Input<string>;
    /**
     * The endpoint service name.
     */
    endpointServiceName?: pulumi.Input<string>;
    /**
     * The Id of the NGFW.
     */
    firewallId?: pulumi.Input<string>;
    /**
     * The global rulestack for this NGFW.
     */
    globalRulestack?: pulumi.Input<string>;
    /**
     * A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
     */
    linkId?: pulumi.Input<string>;
    /**
     * The link status.
     */
    linkStatus?: pulumi.Input<string>;
    /**
     * Share NGFW with Multiple VPCs. This feature can be enabled only if the endpointMode is CustomerManaged.
     */
    multiVpc?: pulumi.Input<boolean>;
    /**
     * The NGFW name.
     */
    name?: pulumi.Input<string>;
    /**
     * The rulestack for this NGFW.
     */
    rulestack?: pulumi.Input<string>;
    statuses?: pulumi.Input<pulumi.Input<inputs.NgfwStatus>[]>;
    /**
     * Subnet mappings.
     */
    subnetMappings?: pulumi.Input<pulumi.Input<inputs.NgfwSubnetMapping>[]>;
    /**
     * The tags.
     */
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The update token.
     */
    updateToken?: pulumi.Input<string>;
    /**
     * The vpc id.
     */
    vpcId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Ngfw resource.
 */
export interface NgfwArgs {
    /**
     * The account ID. This field is mandatory if using multiple accounts.
     */
    accountId?: pulumi.Input<string>;
    /**
     * App-ID version number.
     */
    appIdVersion?: pulumi.Input<string>;
    /**
     * Automatic App-ID upgrade version number. Defaults to `true`.
     */
    automaticUpgradeAppIdVersion?: pulumi.Input<boolean>;
    /**
     * The description.
     */
    description?: pulumi.Input<string>;
    /**
     * Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
     */
    endpointMode: pulumi.Input<string>;
    /**
     * The global rulestack for this NGFW.
     */
    globalRulestack?: pulumi.Input<string>;
    /**
     * A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
     */
    linkId?: pulumi.Input<string>;
    /**
     * Share NGFW with Multiple VPCs. This feature can be enabled only if the endpointMode is CustomerManaged.
     */
    multiVpc?: pulumi.Input<boolean>;
    /**
     * The NGFW name.
     */
    name?: pulumi.Input<string>;
    /**
     * The rulestack for this NGFW.
     */
    rulestack?: pulumi.Input<string>;
    /**
     * Subnet mappings.
     */
    subnetMappings: pulumi.Input<pulumi.Input<inputs.NgfwSubnetMapping>[]>;
    /**
     * The tags.
     */
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The vpc id.
     */
    vpcId: pulumi.Input<string>;
}
