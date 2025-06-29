// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudngfwaws

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-cloudngfwaws/sdk/go/cloudngfwaws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource for prefix list manipulation.
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
//			_, err = cloudngfwaws.NewPrefixList(ctx, "example", &cloudngfwaws.PrefixListArgs{
//				Rulestack:   r.Name,
//				Name:        pulumi.String("tf-prefix-list"),
//				Description: pulumi.String("Also configured by Terraform"),
//				PrefixLists: pulumi.StringArray{
//					pulumi.String("192.168.0.0"),
//					pulumi.String("10.1.5.0"),
//				},
//				AuditComment: pulumi.String("initial config"),
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
// import name is <scope>:<rulestack>:<prefix_list_name>
//
// ```sh
// $ pulumi import cloudngfwaws:index/prefixList:PrefixList example Local:terraform-rulestack:tf-prefix-list
// ```
type PrefixList struct {
	pulumi.CustomResourceState

	// The audit comment.
	AuditComment pulumi.StringPtrOutput `pulumi:"auditComment"`
	// The description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The name.
	Name pulumi.StringOutput `pulumi:"name"`
	// The prefix list.
	PrefixLists pulumi.StringArrayOutput `pulumi:"prefixLists"`
	// The rulestack.
	Rulestack pulumi.StringOutput `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrOutput `pulumi:"scope"`
	// The update token.
	UpdateToken pulumi.StringOutput `pulumi:"updateToken"`
}

// NewPrefixList registers a new resource with the given unique name, arguments, and options.
func NewPrefixList(ctx *pulumi.Context,
	name string, args *PrefixListArgs, opts ...pulumi.ResourceOption) (*PrefixList, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PrefixLists == nil {
		return nil, errors.New("invalid value for required argument 'PrefixLists'")
	}
	if args.Rulestack == nil {
		return nil, errors.New("invalid value for required argument 'Rulestack'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource PrefixList
	err := ctx.RegisterResource("cloudngfwaws:index/prefixList:PrefixList", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPrefixList gets an existing PrefixList resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPrefixList(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PrefixListState, opts ...pulumi.ResourceOption) (*PrefixList, error) {
	var resource PrefixList
	err := ctx.ReadResource("cloudngfwaws:index/prefixList:PrefixList", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PrefixList resources.
type prefixListState struct {
	// The audit comment.
	AuditComment *string `pulumi:"auditComment"`
	// The description.
	Description *string `pulumi:"description"`
	// The name.
	Name *string `pulumi:"name"`
	// The prefix list.
	PrefixLists []string `pulumi:"prefixLists"`
	// The rulestack.
	Rulestack *string `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope *string `pulumi:"scope"`
	// The update token.
	UpdateToken *string `pulumi:"updateToken"`
}

type PrefixListState struct {
	// The audit comment.
	AuditComment pulumi.StringPtrInput
	// The description.
	Description pulumi.StringPtrInput
	// The name.
	Name pulumi.StringPtrInput
	// The prefix list.
	PrefixLists pulumi.StringArrayInput
	// The rulestack.
	Rulestack pulumi.StringPtrInput
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrInput
	// The update token.
	UpdateToken pulumi.StringPtrInput
}

func (PrefixListState) ElementType() reflect.Type {
	return reflect.TypeOf((*prefixListState)(nil)).Elem()
}

type prefixListArgs struct {
	// The audit comment.
	AuditComment *string `pulumi:"auditComment"`
	// The description.
	Description *string `pulumi:"description"`
	// The name.
	Name *string `pulumi:"name"`
	// The prefix list.
	PrefixLists []string `pulumi:"prefixLists"`
	// The rulestack.
	Rulestack string `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope *string `pulumi:"scope"`
}

// The set of arguments for constructing a PrefixList resource.
type PrefixListArgs struct {
	// The audit comment.
	AuditComment pulumi.StringPtrInput
	// The description.
	Description pulumi.StringPtrInput
	// The name.
	Name pulumi.StringPtrInput
	// The prefix list.
	PrefixLists pulumi.StringArrayInput
	// The rulestack.
	Rulestack pulumi.StringInput
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrInput
}

func (PrefixListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*prefixListArgs)(nil)).Elem()
}

type PrefixListInput interface {
	pulumi.Input

	ToPrefixListOutput() PrefixListOutput
	ToPrefixListOutputWithContext(ctx context.Context) PrefixListOutput
}

func (*PrefixList) ElementType() reflect.Type {
	return reflect.TypeOf((**PrefixList)(nil)).Elem()
}

func (i *PrefixList) ToPrefixListOutput() PrefixListOutput {
	return i.ToPrefixListOutputWithContext(context.Background())
}

func (i *PrefixList) ToPrefixListOutputWithContext(ctx context.Context) PrefixListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PrefixListOutput)
}

// PrefixListArrayInput is an input type that accepts PrefixListArray and PrefixListArrayOutput values.
// You can construct a concrete instance of `PrefixListArrayInput` via:
//
//	PrefixListArray{ PrefixListArgs{...} }
type PrefixListArrayInput interface {
	pulumi.Input

	ToPrefixListArrayOutput() PrefixListArrayOutput
	ToPrefixListArrayOutputWithContext(context.Context) PrefixListArrayOutput
}

type PrefixListArray []PrefixListInput

func (PrefixListArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PrefixList)(nil)).Elem()
}

func (i PrefixListArray) ToPrefixListArrayOutput() PrefixListArrayOutput {
	return i.ToPrefixListArrayOutputWithContext(context.Background())
}

func (i PrefixListArray) ToPrefixListArrayOutputWithContext(ctx context.Context) PrefixListArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PrefixListArrayOutput)
}

// PrefixListMapInput is an input type that accepts PrefixListMap and PrefixListMapOutput values.
// You can construct a concrete instance of `PrefixListMapInput` via:
//
//	PrefixListMap{ "key": PrefixListArgs{...} }
type PrefixListMapInput interface {
	pulumi.Input

	ToPrefixListMapOutput() PrefixListMapOutput
	ToPrefixListMapOutputWithContext(context.Context) PrefixListMapOutput
}

type PrefixListMap map[string]PrefixListInput

func (PrefixListMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PrefixList)(nil)).Elem()
}

func (i PrefixListMap) ToPrefixListMapOutput() PrefixListMapOutput {
	return i.ToPrefixListMapOutputWithContext(context.Background())
}

func (i PrefixListMap) ToPrefixListMapOutputWithContext(ctx context.Context) PrefixListMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PrefixListMapOutput)
}

type PrefixListOutput struct{ *pulumi.OutputState }

func (PrefixListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PrefixList)(nil)).Elem()
}

func (o PrefixListOutput) ToPrefixListOutput() PrefixListOutput {
	return o
}

func (o PrefixListOutput) ToPrefixListOutputWithContext(ctx context.Context) PrefixListOutput {
	return o
}

// The audit comment.
func (o PrefixListOutput) AuditComment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PrefixList) pulumi.StringPtrOutput { return v.AuditComment }).(pulumi.StringPtrOutput)
}

// The description.
func (o PrefixListOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PrefixList) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The name.
func (o PrefixListOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *PrefixList) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The prefix list.
func (o PrefixListOutput) PrefixLists() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *PrefixList) pulumi.StringArrayOutput { return v.PrefixLists }).(pulumi.StringArrayOutput)
}

// The rulestack.
func (o PrefixListOutput) Rulestack() pulumi.StringOutput {
	return o.ApplyT(func(v *PrefixList) pulumi.StringOutput { return v.Rulestack }).(pulumi.StringOutput)
}

// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
func (o PrefixListOutput) Scope() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PrefixList) pulumi.StringPtrOutput { return v.Scope }).(pulumi.StringPtrOutput)
}

// The update token.
func (o PrefixListOutput) UpdateToken() pulumi.StringOutput {
	return o.ApplyT(func(v *PrefixList) pulumi.StringOutput { return v.UpdateToken }).(pulumi.StringOutput)
}

type PrefixListArrayOutput struct{ *pulumi.OutputState }

func (PrefixListArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PrefixList)(nil)).Elem()
}

func (o PrefixListArrayOutput) ToPrefixListArrayOutput() PrefixListArrayOutput {
	return o
}

func (o PrefixListArrayOutput) ToPrefixListArrayOutputWithContext(ctx context.Context) PrefixListArrayOutput {
	return o
}

func (o PrefixListArrayOutput) Index(i pulumi.IntInput) PrefixListOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *PrefixList {
		return vs[0].([]*PrefixList)[vs[1].(int)]
	}).(PrefixListOutput)
}

type PrefixListMapOutput struct{ *pulumi.OutputState }

func (PrefixListMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PrefixList)(nil)).Elem()
}

func (o PrefixListMapOutput) ToPrefixListMapOutput() PrefixListMapOutput {
	return o
}

func (o PrefixListMapOutput) ToPrefixListMapOutputWithContext(ctx context.Context) PrefixListMapOutput {
	return o
}

func (o PrefixListMapOutput) MapIndex(k pulumi.StringInput) PrefixListOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *PrefixList {
		return vs[0].(map[string]*PrefixList)[vs[1].(string)]
	}).(PrefixListOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PrefixListInput)(nil)).Elem(), &PrefixList{})
	pulumi.RegisterInputType(reflect.TypeOf((*PrefixListArrayInput)(nil)).Elem(), PrefixListArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PrefixListMapInput)(nil)).Elem(), PrefixListMap{})
	pulumi.RegisterOutputType(PrefixListOutput{})
	pulumi.RegisterOutputType(PrefixListArrayOutput{})
	pulumi.RegisterOutputType(PrefixListMapOutput{})
}
