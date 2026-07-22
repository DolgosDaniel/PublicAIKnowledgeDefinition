#!/usr/bin/env python3
"""Unit tests for tools/paik_validate.py.

Builds a tiny valid fixture paik/ folder, confirms it validates clean, then applies one
mutation at a time and asserts the mutated copy is now flagged - both PAIK-profile mutations
(a gap the v0.3 validator was found to miss) and the two OKF-base-conformance layer checks
(missing `type`, unrecognized `type`) introduced with the v0.4 OKF alignment.
Run with: python -m unittest tools.test_paik_validate
"""
import copy
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paik_validate as pv

PROJECT_MD = """---
type: paik-project
paik: "0.4"
id: fixture
title: Fixture
lifecycle: active
owner:
  name: Fixture team
description: a tiny fixture project
links:
  - kind: jira-project
    id: FIX
    url: https://example.atlassian.net/jira/software/projects/FIX
components:
  - components/a.md
environments:
  - environments/dev.md
---
# Fixture
"""

COMPONENT_A_MD = """---
type: paik-component
paik: "0.4"
id: a
title: A
lifecycle: active
owner:
  name: Fixture team
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/fixture/a
environments:
  - ../environments/dev.md
depends_on: []
---
# A
"""

ENVIRONMENT_DEV_MD = """---
type: paik-environment
paik: "0.4"
id: dev
title: Dev
lifecycle: active
purpose: fixture dev environment
app_url: https://dev.fixture.example
health_endpoint: https://dev.fixture.example/health
access: public
---
# Dev
"""


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="paik_test_")
        self.paik_dir = os.path.join(self.tmp, "paik")
        os.makedirs(os.path.join(self.paik_dir, "components"))
        os.makedirs(os.path.join(self.paik_dir, "environments"))
        self.files = {
            "project.md": PROJECT_MD,
            "components/a.md": COMPONENT_A_MD,
            "environments/dev.md": ENVIRONMENT_DEV_MD,
        }
        self.validators = pv.load_validators()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write(self, files):
        for rel, content in files.items():
            path = os.path.join(self.paik_dir, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)

    def run_validate(self):
        report = pv.Report()
        pv.validate_dir(self.paik_dir, self.validators, report)
        return report

    def test_clean_fixture_has_no_errors(self):
        self.write(self.files)
        report = self.run_validate()
        self.assertEqual(report.errors, [])

    def test_missing_type_field_is_rejected(self):
        files = copy.deepcopy(self.files)
        files["components/a.md"] = files["components/a.md"].replace("type: paik-component\n", "", 1)
        self.write(files)
        report = self.run_validate()
        self.assertTrue(
            any("OKF base conformance" in e and "'type'" in e for e in report.errors),
            f"expected an OKF base-conformance error, got: {report.errors}",
        )

    def test_unrecognized_type_value_is_rejected(self):
        files = copy.deepcopy(self.files)
        files["components/a.md"] = files["components/a.md"].replace(
            "type: paik-component\n", "type: some-other-okf-concept\n", 1
        )
        self.write(files)
        report = self.run_validate()
        self.assertTrue(
            any("unrecognized PAIK type" in e for e in report.errors),
            f"expected an unrecognized-type error, got: {report.errors}",
        )

    def test_component_and_environment_sharing_an_id_is_rejected(self):
        files = copy.deepcopy(self.files)
        files["components/a.md"] = files["components/a.md"].replace("id: a\n", "id: dev\n", 1)
        self.write(files)
        report = self.run_validate()
        self.assertTrue(
            any("duplicate id" in e for e in report.errors),
            f"expected a duplicate id error, got: {report.errors}",
        )

    def test_components_entry_pointing_at_an_environment_file_is_rejected(self):
        files = copy.deepcopy(self.files)
        files["project.md"] = files["project.md"].replace(
            "components:\n  - components/a.md", "components:\n  - environments/dev.md"
        )
        self.write(files)
        report = self.run_validate()
        self.assertTrue(
            any("expected 'paik-component'" in e for e in report.errors),
            f"expected a type-mismatch error, got: {report.errors}",
        )

    def test_component_missing_from_project_components_is_rejected(self):
        files = copy.deepcopy(self.files)
        files["components/b.md"] = files["components/a.md"].replace("id: a\n", "id: b\n", 1)
        self.write(files)
        report = self.run_validate()
        self.assertTrue(
            any("isn't listed in this project's 'components'" in e for e in report.errors),
            f"expected an unlisted-component error, got: {report.errors}",
        )

    def test_nonexistent_link_component_qualifier_is_rejected(self):
        files = copy.deepcopy(self.files)
        files["environments/dev.md"] = files["environments/dev.md"].replace(
            "access: public\n",
            "access: public\nlinks:\n  - kind: deploy-pipeline\n    component: does-not-exist\n    url: https://example.com/pipeline\n",
        )
        self.write(files)
        report = self.run_validate()
        self.assertTrue(
            any("is not a known component id" in e for e in report.errors),
            f"expected an unknown-component-qualifier error, got: {report.errors}",
        )

    def test_invalid_uri_is_rejected(self):
        files = copy.deepcopy(self.files)
        files["components/a.md"] = files["components/a.md"].replace(
            "url: https://github.com/fixture/a", "url: not a url"
        )
        self.write(files)
        report = self.run_validate()
        self.assertTrue(
            any("not a 'uri'" in e or "uri" in e.lower() for e in report.errors),
            f"expected a uri format error, got: {report.errors}",
        )

    def test_reference_outside_paik_dir_is_rejected(self):
        files = copy.deepcopy(self.files)
        # A malicious/careless "../../../etc/passwd"-shaped relative link.
        outside = os.path.join(self.tmp, "outside.md")
        with open(outside, "w", encoding="utf-8") as fh:
            fh.write("not a paik document\n")
        files["components/a.md"] = files["components/a.md"].replace(
            "environments:\n  - ../environments/dev.md",
            "environments:\n  - ../environments/dev.md\n  - ../../outside.md",
        )
        self.write(files)
        report = self.run_validate()
        self.assertTrue(
            any("resolves outside the paik/ folder" in e for e in report.errors),
            f"expected an outside-paik-dir error, got: {report.errors}",
        )

    def test_empty_link_kind_is_rejected(self):
        files = copy.deepcopy(self.files)
        files["components/a.md"] = files["components/a.md"].replace(
            "  - kind: repository\n", "  - kind: \"\"\n"
        )
        self.write(files)
        report = self.run_validate()
        self.assertTrue(
            any("empty or missing 'kind'" in e for e in report.errors),
            f"expected an empty-kind error, got: {report.errors}",
        )


if __name__ == "__main__":
    unittest.main()
