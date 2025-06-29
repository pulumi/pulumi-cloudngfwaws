// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudngfwaws

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-cloudngfwaws/sdk/go/cloudngfwaws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Data source for retrieving the predefined URL categories.
//
// ## Admin Permission Type
//
// * `Rulestack` (for `scope="Local"`)
// * `Global Rulestack` (for `scope="Global"`)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-cloudngfwaws/sdk/go/cloudngfwaws"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := cloudngfwaws.GetPredefinedUrlCategories(ctx, &cloudngfwaws.GetPredefinedUrlCategoriesArgs{}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetPredefinedUrlCategories(ctx *pulumi.Context, args *GetPredefinedUrlCategoriesArgs, opts ...pulumi.InvokeOption) (*GetPredefinedUrlCategoriesResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetPredefinedUrlCategoriesResult
	err := ctx.Invoke("cloudngfwaws:index/getPredefinedUrlCategories:getPredefinedUrlCategories", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPredefinedUrlCategories.
type GetPredefinedUrlCategoriesArgs struct {
	// Max results. Defaults to `100`.
	MaxResults *int `pulumi:"maxResults"`
	// Pagination token.
	Token *string `pulumi:"token"`
}

// A collection of values returned by getPredefinedUrlCategories.
type GetPredefinedUrlCategoriesResult struct {
	// List of predefined URL categories.
	Categories []string `pulumi:"categories"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Max results. Defaults to `100`.
	MaxResults *int `pulumi:"maxResults"`
	// Next pagination token.
	NextToken string `pulumi:"nextToken"`
	// Pagination token.
	Token *string `pulumi:"token"`
}

func GetPredefinedUrlCategoriesOutput(ctx *pulumi.Context, args GetPredefinedUrlCategoriesOutputArgs, opts ...pulumi.InvokeOption) GetPredefinedUrlCategoriesResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetPredefinedUrlCategoriesResultOutput, error) {
			args := v.(GetPredefinedUrlCategoriesArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("cloudngfwaws:index/getPredefinedUrlCategories:getPredefinedUrlCategories", args, GetPredefinedUrlCategoriesResultOutput{}, options).(GetPredefinedUrlCategoriesResultOutput), nil
		}).(GetPredefinedUrlCategoriesResultOutput)
}

// A collection of arguments for invoking getPredefinedUrlCategories.
type GetPredefinedUrlCategoriesOutputArgs struct {
	// Max results. Defaults to `100`.
	MaxResults pulumi.IntPtrInput `pulumi:"maxResults"`
	// Pagination token.
	Token pulumi.StringPtrInput `pulumi:"token"`
}

func (GetPredefinedUrlCategoriesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPredefinedUrlCategoriesArgs)(nil)).Elem()
}

// A collection of values returned by getPredefinedUrlCategories.
type GetPredefinedUrlCategoriesResultOutput struct{ *pulumi.OutputState }

func (GetPredefinedUrlCategoriesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPredefinedUrlCategoriesResult)(nil)).Elem()
}

func (o GetPredefinedUrlCategoriesResultOutput) ToGetPredefinedUrlCategoriesResultOutput() GetPredefinedUrlCategoriesResultOutput {
	return o
}

func (o GetPredefinedUrlCategoriesResultOutput) ToGetPredefinedUrlCategoriesResultOutputWithContext(ctx context.Context) GetPredefinedUrlCategoriesResultOutput {
	return o
}

// List of predefined URL categories.
func (o GetPredefinedUrlCategoriesResultOutput) Categories() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetPredefinedUrlCategoriesResult) []string { return v.Categories }).(pulumi.StringArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetPredefinedUrlCategoriesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetPredefinedUrlCategoriesResult) string { return v.Id }).(pulumi.StringOutput)
}

// Max results. Defaults to `100`.
func (o GetPredefinedUrlCategoriesResultOutput) MaxResults() pulumi.IntPtrOutput {
	return o.ApplyT(func(v GetPredefinedUrlCategoriesResult) *int { return v.MaxResults }).(pulumi.IntPtrOutput)
}

// Next pagination token.
func (o GetPredefinedUrlCategoriesResultOutput) NextToken() pulumi.StringOutput {
	return o.ApplyT(func(v GetPredefinedUrlCategoriesResult) string { return v.NextToken }).(pulumi.StringOutput)
}

// Pagination token.
func (o GetPredefinedUrlCategoriesResultOutput) Token() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetPredefinedUrlCategoriesResult) *string { return v.Token }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetPredefinedUrlCategoriesResultOutput{})
}
