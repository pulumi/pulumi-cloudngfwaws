// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudngfwaws

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-cloudngfwaws/sdk/go/cloudngfwaws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource for custom url category manipulation.
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
//			r, err := cloudngfwaws.NewRulestack(ctx, "r", &cloudngfwaws.RulestackArgs{
//				Name:        pulumi.String("terraform-rulestack"),
//				Scope:       pulumi.String("Local"),
//				AccountId:   pulumi.String("123456789"),
//				Description: pulumi.String("Made by Pulumi"),
//				ProfileConfig: &cloudngfwaws.RulestackProfileConfigArgs{
//					AntiSpyware: pulumi.String("BestPractice"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = cloudngfwaws.NewCustomUrlCategory(ctx, "example", &cloudngfwaws.CustomUrlCategoryArgs{
//				Rulestack:   r.Name,
//				Name:        pulumi.String("tf-custom-category"),
//				Description: pulumi.String("Also configured by Terraform"),
//				UrlLists: pulumi.StringArray{
//					pulumi.String("example.com"),
//					pulumi.String("paloaltonetworks.com"),
//					pulumi.String("foobar.org"),
//				},
//				Action: pulumi.String("alert"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// import name is <scope>:<rulestack>:<category_name>
//
// ```sh
// $ pulumi import cloudngfwaws:index/customUrlCategory:CustomUrlCategory example Local:terraform-rulestack:tf-custom-category
// ```
type CustomUrlCategory struct {
	pulumi.CustomResourceState

	// The action to take. Valid values are `none`, `alert`, `allow`, `block`, `continue`, or `override`. Defaults to `none`.
	Action pulumi.StringPtrOutput `pulumi:"action"`
	// The audit comment.
	AuditComment pulumi.StringPtrOutput `pulumi:"auditComment"`
	// The description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The name.
	Name pulumi.StringOutput `pulumi:"name"`
	// The rulestack.
	Rulestack pulumi.StringOutput `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrOutput `pulumi:"scope"`
	// The update token.
	UpdateToken pulumi.StringOutput `pulumi:"updateToken"`
	// The URL list for this custom URL category.
	UrlLists pulumi.StringArrayOutput `pulumi:"urlLists"`
}

// NewCustomUrlCategory registers a new resource with the given unique name, arguments, and options.
func NewCustomUrlCategory(ctx *pulumi.Context,
	name string, args *CustomUrlCategoryArgs, opts ...pulumi.ResourceOption) (*CustomUrlCategory, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Rulestack == nil {
		return nil, errors.New("invalid value for required argument 'Rulestack'")
	}
	if args.UrlLists == nil {
		return nil, errors.New("invalid value for required argument 'UrlLists'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource CustomUrlCategory
	err := ctx.RegisterResource("cloudngfwaws:index/customUrlCategory:CustomUrlCategory", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCustomUrlCategory gets an existing CustomUrlCategory resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCustomUrlCategory(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CustomUrlCategoryState, opts ...pulumi.ResourceOption) (*CustomUrlCategory, error) {
	var resource CustomUrlCategory
	err := ctx.ReadResource("cloudngfwaws:index/customUrlCategory:CustomUrlCategory", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CustomUrlCategory resources.
type customUrlCategoryState struct {
	// The action to take. Valid values are `none`, `alert`, `allow`, `block`, `continue`, or `override`. Defaults to `none`.
	Action *string `pulumi:"action"`
	// The audit comment.
	AuditComment *string `pulumi:"auditComment"`
	// The description.
	Description *string `pulumi:"description"`
	// The name.
	Name *string `pulumi:"name"`
	// The rulestack.
	Rulestack *string `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope *string `pulumi:"scope"`
	// The update token.
	UpdateToken *string `pulumi:"updateToken"`
	// The URL list for this custom URL category.
	UrlLists []string `pulumi:"urlLists"`
}

type CustomUrlCategoryState struct {
	// The action to take. Valid values are `none`, `alert`, `allow`, `block`, `continue`, or `override`. Defaults to `none`.
	Action pulumi.StringPtrInput
	// The audit comment.
	AuditComment pulumi.StringPtrInput
	// The description.
	Description pulumi.StringPtrInput
	// The name.
	Name pulumi.StringPtrInput
	// The rulestack.
	Rulestack pulumi.StringPtrInput
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrInput
	// The update token.
	UpdateToken pulumi.StringPtrInput
	// The URL list for this custom URL category.
	UrlLists pulumi.StringArrayInput
}

func (CustomUrlCategoryState) ElementType() reflect.Type {
	return reflect.TypeOf((*customUrlCategoryState)(nil)).Elem()
}

type customUrlCategoryArgs struct {
	// The action to take. Valid values are `none`, `alert`, `allow`, `block`, `continue`, or `override`. Defaults to `none`.
	Action *string `pulumi:"action"`
	// The audit comment.
	AuditComment *string `pulumi:"auditComment"`
	// The description.
	Description *string `pulumi:"description"`
	// The name.
	Name *string `pulumi:"name"`
	// The rulestack.
	Rulestack string `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope *string `pulumi:"scope"`
	// The URL list for this custom URL category.
	UrlLists []string `pulumi:"urlLists"`
}

// The set of arguments for constructing a CustomUrlCategory resource.
type CustomUrlCategoryArgs struct {
	// The action to take. Valid values are `none`, `alert`, `allow`, `block`, `continue`, or `override`. Defaults to `none`.
	Action pulumi.StringPtrInput
	// The audit comment.
	AuditComment pulumi.StringPtrInput
	// The description.
	Description pulumi.StringPtrInput
	// The name.
	Name pulumi.StringPtrInput
	// The rulestack.
	Rulestack pulumi.StringInput
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrInput
	// The URL list for this custom URL category.
	UrlLists pulumi.StringArrayInput
}

func (CustomUrlCategoryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*customUrlCategoryArgs)(nil)).Elem()
}

type CustomUrlCategoryInput interface {
	pulumi.Input

	ToCustomUrlCategoryOutput() CustomUrlCategoryOutput
	ToCustomUrlCategoryOutputWithContext(ctx context.Context) CustomUrlCategoryOutput
}

func (*CustomUrlCategory) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomUrlCategory)(nil)).Elem()
}

func (i *CustomUrlCategory) ToCustomUrlCategoryOutput() CustomUrlCategoryOutput {
	return i.ToCustomUrlCategoryOutputWithContext(context.Background())
}

func (i *CustomUrlCategory) ToCustomUrlCategoryOutputWithContext(ctx context.Context) CustomUrlCategoryOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomUrlCategoryOutput)
}

// CustomUrlCategoryArrayInput is an input type that accepts CustomUrlCategoryArray and CustomUrlCategoryArrayOutput values.
// You can construct a concrete instance of `CustomUrlCategoryArrayInput` via:
//
//	CustomUrlCategoryArray{ CustomUrlCategoryArgs{...} }
type CustomUrlCategoryArrayInput interface {
	pulumi.Input

	ToCustomUrlCategoryArrayOutput() CustomUrlCategoryArrayOutput
	ToCustomUrlCategoryArrayOutputWithContext(context.Context) CustomUrlCategoryArrayOutput
}

type CustomUrlCategoryArray []CustomUrlCategoryInput

func (CustomUrlCategoryArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CustomUrlCategory)(nil)).Elem()
}

func (i CustomUrlCategoryArray) ToCustomUrlCategoryArrayOutput() CustomUrlCategoryArrayOutput {
	return i.ToCustomUrlCategoryArrayOutputWithContext(context.Background())
}

func (i CustomUrlCategoryArray) ToCustomUrlCategoryArrayOutputWithContext(ctx context.Context) CustomUrlCategoryArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomUrlCategoryArrayOutput)
}

// CustomUrlCategoryMapInput is an input type that accepts CustomUrlCategoryMap and CustomUrlCategoryMapOutput values.
// You can construct a concrete instance of `CustomUrlCategoryMapInput` via:
//
//	CustomUrlCategoryMap{ "key": CustomUrlCategoryArgs{...} }
type CustomUrlCategoryMapInput interface {
	pulumi.Input

	ToCustomUrlCategoryMapOutput() CustomUrlCategoryMapOutput
	ToCustomUrlCategoryMapOutputWithContext(context.Context) CustomUrlCategoryMapOutput
}

type CustomUrlCategoryMap map[string]CustomUrlCategoryInput

func (CustomUrlCategoryMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CustomUrlCategory)(nil)).Elem()
}

func (i CustomUrlCategoryMap) ToCustomUrlCategoryMapOutput() CustomUrlCategoryMapOutput {
	return i.ToCustomUrlCategoryMapOutputWithContext(context.Background())
}

func (i CustomUrlCategoryMap) ToCustomUrlCategoryMapOutputWithContext(ctx context.Context) CustomUrlCategoryMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomUrlCategoryMapOutput)
}

type CustomUrlCategoryOutput struct{ *pulumi.OutputState }

func (CustomUrlCategoryOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomUrlCategory)(nil)).Elem()
}

func (o CustomUrlCategoryOutput) ToCustomUrlCategoryOutput() CustomUrlCategoryOutput {
	return o
}

func (o CustomUrlCategoryOutput) ToCustomUrlCategoryOutputWithContext(ctx context.Context) CustomUrlCategoryOutput {
	return o
}

// The action to take. Valid values are `none`, `alert`, `allow`, `block`, `continue`, or `override`. Defaults to `none`.
func (o CustomUrlCategoryOutput) Action() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CustomUrlCategory) pulumi.StringPtrOutput { return v.Action }).(pulumi.StringPtrOutput)
}

// The audit comment.
func (o CustomUrlCategoryOutput) AuditComment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CustomUrlCategory) pulumi.StringPtrOutput { return v.AuditComment }).(pulumi.StringPtrOutput)
}

// The description.
func (o CustomUrlCategoryOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CustomUrlCategory) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The name.
func (o CustomUrlCategoryOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomUrlCategory) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The rulestack.
func (o CustomUrlCategoryOutput) Rulestack() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomUrlCategory) pulumi.StringOutput { return v.Rulestack }).(pulumi.StringOutput)
}

// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
func (o CustomUrlCategoryOutput) Scope() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CustomUrlCategory) pulumi.StringPtrOutput { return v.Scope }).(pulumi.StringPtrOutput)
}

// The update token.
func (o CustomUrlCategoryOutput) UpdateToken() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomUrlCategory) pulumi.StringOutput { return v.UpdateToken }).(pulumi.StringOutput)
}

// The URL list for this custom URL category.
func (o CustomUrlCategoryOutput) UrlLists() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *CustomUrlCategory) pulumi.StringArrayOutput { return v.UrlLists }).(pulumi.StringArrayOutput)
}

type CustomUrlCategoryArrayOutput struct{ *pulumi.OutputState }

func (CustomUrlCategoryArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CustomUrlCategory)(nil)).Elem()
}

func (o CustomUrlCategoryArrayOutput) ToCustomUrlCategoryArrayOutput() CustomUrlCategoryArrayOutput {
	return o
}

func (o CustomUrlCategoryArrayOutput) ToCustomUrlCategoryArrayOutputWithContext(ctx context.Context) CustomUrlCategoryArrayOutput {
	return o
}

func (o CustomUrlCategoryArrayOutput) Index(i pulumi.IntInput) CustomUrlCategoryOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *CustomUrlCategory {
		return vs[0].([]*CustomUrlCategory)[vs[1].(int)]
	}).(CustomUrlCategoryOutput)
}

type CustomUrlCategoryMapOutput struct{ *pulumi.OutputState }

func (CustomUrlCategoryMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CustomUrlCategory)(nil)).Elem()
}

func (o CustomUrlCategoryMapOutput) ToCustomUrlCategoryMapOutput() CustomUrlCategoryMapOutput {
	return o
}

func (o CustomUrlCategoryMapOutput) ToCustomUrlCategoryMapOutputWithContext(ctx context.Context) CustomUrlCategoryMapOutput {
	return o
}

func (o CustomUrlCategoryMapOutput) MapIndex(k pulumi.StringInput) CustomUrlCategoryOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *CustomUrlCategory {
		return vs[0].(map[string]*CustomUrlCategory)[vs[1].(string)]
	}).(CustomUrlCategoryOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CustomUrlCategoryInput)(nil)).Elem(), &CustomUrlCategory{})
	pulumi.RegisterInputType(reflect.TypeOf((*CustomUrlCategoryArrayInput)(nil)).Elem(), CustomUrlCategoryArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CustomUrlCategoryMapInput)(nil)).Elem(), CustomUrlCategoryMap{})
	pulumi.RegisterOutputType(CustomUrlCategoryOutput{})
	pulumi.RegisterOutputType(CustomUrlCategoryArrayOutput{})
	pulumi.RegisterOutputType(CustomUrlCategoryMapOutput{})
}
