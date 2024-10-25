// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Data source for retrieving the predefined URL categories.
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
 * const example = cloudngfwaws.getPredefinedUrlCategories({});
 * ```
 */
export function getPredefinedUrlCategories(args?: GetPredefinedUrlCategoriesArgs, opts?: pulumi.InvokeOptions): Promise<GetPredefinedUrlCategoriesResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("cloudngfwaws:index/getPredefinedUrlCategories:getPredefinedUrlCategories", {
        "maxResults": args.maxResults,
        "token": args.token,
    }, opts);
}

/**
 * A collection of arguments for invoking getPredefinedUrlCategories.
 */
export interface GetPredefinedUrlCategoriesArgs {
    /**
     * Max results. Defaults to `100`.
     */
    maxResults?: number;
    /**
     * Pagination token.
     */
    token?: string;
}

/**
 * A collection of values returned by getPredefinedUrlCategories.
 */
export interface GetPredefinedUrlCategoriesResult {
    /**
     * List of predefined URL categories.
     */
    readonly categories: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Max results. Defaults to `100`.
     */
    readonly maxResults?: number;
    /**
     * Next pagination token.
     */
    readonly nextToken: string;
    /**
     * Pagination token.
     */
    readonly token?: string;
}
/**
 * Data source for retrieving the predefined URL categories.
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
 * const example = cloudngfwaws.getPredefinedUrlCategories({});
 * ```
 */
export function getPredefinedUrlCategoriesOutput(args?: GetPredefinedUrlCategoriesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPredefinedUrlCategoriesResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("cloudngfwaws:index/getPredefinedUrlCategories:getPredefinedUrlCategories", {
        "maxResults": args.maxResults,
        "token": args.token,
    }, opts);
}

/**
 * A collection of arguments for invoking getPredefinedUrlCategories.
 */
export interface GetPredefinedUrlCategoriesOutputArgs {
    /**
     * Max results. Defaults to `100`.
     */
    maxResults?: pulumi.Input<number>;
    /**
     * Pagination token.
     */
    token?: pulumi.Input<string>;
}
