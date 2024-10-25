// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Resource for certificate manipulation.
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
 * const r = new cloudngfwaws.Rulestack("r", {
 *     name: "terraform-rulestack",
 *     scope: "Local",
 *     accountId: "123456789",
 *     description: "Made by Pulumi",
 *     profileConfig: {
 *         antiSpyware: "BestPractice",
 *     },
 * });
 * const example = new cloudngfwaws.Certificate("example", {
 *     rulestack: r.name,
 *     name: "tf-cert",
 *     description: "Also configured by Terraform",
 *     selfSigned: true,
 *     auditComment: "initial config",
 * });
 * ```
 *
 * ## Import
 *
 * import name is <scope>:<rulestack>:<certificate_name>
 *
 * ```sh
 * $ pulumi import cloudngfwaws:index/certificate:Certificate example Local:terraform-rulestack:tf-cert
 * ```
 */
export class Certificate extends pulumi.CustomResource {
    /**
     * Get an existing Certificate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertificateState, opts?: pulumi.CustomResourceOptions): Certificate {
        return new Certificate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cloudngfwaws:index/certificate:Certificate';

    /**
     * Returns true if the given object is an instance of Certificate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Certificate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Certificate.__pulumiType;
    }

    /**
     * The audit comment.
     */
    public readonly auditComment!: pulumi.Output<string | undefined>;
    /**
     * The description.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The rulestack.
     */
    public readonly rulestack!: pulumi.Output<string>;
    /**
     * The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     */
    public readonly scope!: pulumi.Output<string | undefined>;
    /**
     * Set to true if certificate is self-signed.
     */
    public readonly selfSigned!: pulumi.Output<boolean | undefined>;
    /**
     * The certificate signer ARN.
     */
    public readonly signerArn!: pulumi.Output<string | undefined>;
    /**
     * The update token.
     */
    public /*out*/ readonly updateToken!: pulumi.Output<string>;

    /**
     * Create a Certificate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CertificateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CertificateArgs | CertificateState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CertificateState | undefined;
            resourceInputs["auditComment"] = state ? state.auditComment : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["rulestack"] = state ? state.rulestack : undefined;
            resourceInputs["scope"] = state ? state.scope : undefined;
            resourceInputs["selfSigned"] = state ? state.selfSigned : undefined;
            resourceInputs["signerArn"] = state ? state.signerArn : undefined;
            resourceInputs["updateToken"] = state ? state.updateToken : undefined;
        } else {
            const args = argsOrState as CertificateArgs | undefined;
            if ((!args || args.rulestack === undefined) && !opts.urn) {
                throw new Error("Missing required property 'rulestack'");
            }
            resourceInputs["auditComment"] = args ? args.auditComment : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["rulestack"] = args ? args.rulestack : undefined;
            resourceInputs["scope"] = args ? args.scope : undefined;
            resourceInputs["selfSigned"] = args ? args.selfSigned : undefined;
            resourceInputs["signerArn"] = args ? args.signerArn : undefined;
            resourceInputs["updateToken"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Certificate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Certificate resources.
 */
export interface CertificateState {
    /**
     * The audit comment.
     */
    auditComment?: pulumi.Input<string>;
    /**
     * The description.
     */
    description?: pulumi.Input<string>;
    /**
     * The name.
     */
    name?: pulumi.Input<string>;
    /**
     * The rulestack.
     */
    rulestack?: pulumi.Input<string>;
    /**
     * The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     */
    scope?: pulumi.Input<string>;
    /**
     * Set to true if certificate is self-signed.
     */
    selfSigned?: pulumi.Input<boolean>;
    /**
     * The certificate signer ARN.
     */
    signerArn?: pulumi.Input<string>;
    /**
     * The update token.
     */
    updateToken?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Certificate resource.
 */
export interface CertificateArgs {
    /**
     * The audit comment.
     */
    auditComment?: pulumi.Input<string>;
    /**
     * The description.
     */
    description?: pulumi.Input<string>;
    /**
     * The name.
     */
    name?: pulumi.Input<string>;
    /**
     * The rulestack.
     */
    rulestack: pulumi.Input<string>;
    /**
     * The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
     */
    scope?: pulumi.Input<string>;
    /**
     * Set to true if certificate is self-signed.
     */
    selfSigned?: pulumi.Input<boolean>;
    /**
     * The certificate signer ARN.
     */
    signerArn?: pulumi.Input<string>;
}
