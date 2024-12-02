// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package cloudngfwaws

import (
	"context"
	"fmt"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfgen"
	"path/filepath"
	"regexp"

	_ "embed" // to embed bridge metadata

	cloudngfwaws "github.com/paloaltonetworks/terraform-provider-cloudngfwaws/cloudngfwaws"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	tfbridgetokens "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"

	"github.com/pulumi/pulumi-cloudngfwaws/provider/pkg/version"
)

//go:embed cmd/pulumi-resource-cloudngfwaws/bridge-metadata.json
var bridgeMetadata []byte

// all of the token components used below.
const (
	mainPkg = "cloudngfwaws"
	mainMod = "index"
)

// Provider returns additional overlaid schema and metadata associated with the provider
func Provider(_ context.Context) tfbridge.ProviderInfo {
	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:                 shimv2.NewProvider(cloudngfwaws.Provider()),
		Name:              "cloudngfwaws",
		DisplayName:       "Palo Alto Networks Cloud NGFW for AWS",
		PluginDownloadURL: "github://api.github.com/pulumi/pulumi-cloudngfwaws",
		Description:       "A Pulumi package for creating and managing Cloud NGFW for AWS resources.",
		Keywords:          []string{"pulumi", "cloudngfwaws", "Palo Alto Networks", "ngfw", "category/network"},
		License:           "Apache-2.0",
		Homepage:          "https://pulumi.com",
		Repository:        "https://github.com/pulumi/pulumi-cloudngfwaws",
		UpstreamRepoPath:  "./upstream",
		Version:           version.Version,
		LogoURL:           "https://avatars.githubusercontent.com/u/4855743?s=200&v=4",
		MetadataInfo:      tfbridge.NewProviderMetadata(bridgeMetadata),
		DocRules:          &tfbridge.DocRuleInfo{EditRules: docEditRules},

		Resources: map[string]*tfbridge.ResourceInfo{
			"cloudngfwaws_ngfw_log_profile": {ComputeID: missingID},

			"cloudngfwaws_intelligent_feed":                 {ComputeID: missingID},
			"cloudngfwaws_custom_url_category":              {ComputeID: missingID},
			"cloudngfwaws_predefined_url_category_override": {ComputeID: missingID},
			"cloudngfwaws_account_onboarding_stack":         {ComputeID: missingID},
			"cloudngfwaws_certificate":                      {ComputeID: missingID},
			"cloudngfwaws_fqdn_list":                        {ComputeID: missingID},
			"cloudngfwaws_rulestack":                        {ComputeID: missingID},
			"cloudngfwaws_security_rule":                    {ComputeID: missingID},
			"cloudngfwaws_account":                          {ComputeID: missingID},
			"cloudngfwaws_commit_rulestack":                 {ComputeID: missingID},
			"cloudngfwaws_ngfw":                             {ComputeID: missingID},
			"cloudngfwaws_prefix_list":                      {ComputeID: missingID},
			"cloudngfwaws_account_onboarding":               {ComputeID: missingID},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@pulumi/cloudngfwaws",

			DevDependencies: map[string]string{
				"@types/node": "^10.0.0",
				"@types/mime": "^2.0.0",
			},
			RespectSchemaVersion: true,
		},
		Python: &tfbridge.PythonInfo{
			RespectSchemaVersion: true,
			PackageName:          "pulumi_cloudngfwaws",

			PyProject: struct{ Enabled bool }{true},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
			RespectSchemaVersion:           true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RespectSchemaVersion: true,
			RootNamespace:        "Pulumi",
			Namespaces: map[string]string{
				"cloudngfwaws": "CloudNgfwAws",
			},
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	prov.MustComputeTokens(
		tfbridgetokens.SingleModule(
			"cloudngfwaws_",
			mainMod,
			tfbridgetokens.MakeStandard(mainPkg),
		),
	)

	prov.MustApplyAutoAliases()

	prov.SetAutonaming(255, "-")

	return prov
}

var sectionRegexps = []*regexp.Regexp{
	regexp.MustCompile(`ezrulestack`),
	regexp.MustCompile(`Support`),
}

func docEditRules(defaults []tfbridge.DocsEdit) []tfbridge.DocsEdit {
	return append(
		defaults,
		skipSections()...,
	)
}

// Removes sections meant to address the TF maintainer community, see sectionRegexps
func skipSections() []tfbridge.DocsEdit {
	var edits []tfbridge.DocsEdit
	for _, sectionRegexp := range sectionRegexps {
		edits = append(
			edits,
			tfbridge.DocsEdit{
				Path: "index.md",
				Edit: func(_ string, content []byte) ([]byte, error) {
					return tfgen.SkipSectionByHeaderContent(content, func(headerText string) bool {
						return sectionRegexp.Match([]byte(headerText))
					})
				},
			},
		)
	}

	return edits
}

func missingID(context.Context, resource.PropertyMap) (resource.ID, error) {
	return "missing ID", nil
}
