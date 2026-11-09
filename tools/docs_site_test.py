"""Unit tests for tools/docs_site.py — stdlib unittest only.

Run from the repository root:

    uv run python -m unittest discover -s tools -p "*_test.py"
"""

import importlib.util
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

# tools/ is not a package; load the module under test by file path so
# `python -m unittest discover -s tools` works without __init__.py.
_MODULE_PATH = Path(__file__).resolve().parent / "docs_site.py"
_SPEC = importlib.util.spec_from_file_location("docs_site", _MODULE_PATH)
docs_site = importlib.util.module_from_spec(_SPEC)
sys.modules["docs_site"] = docs_site
_SPEC.loader.exec_module(docs_site)

REPO_URL = "https://github.com/DUNE/hep-metadex"


class RewriteOutOfTreeLinksTest(unittest.TestCase):
    def test_rewrites_out_of_tree_link_to_github_blob_url(self):
        rewritten, _ = docs_site.rewrite_out_of_tree_links(
            "See the [domain glossary](../glossary/domain.md) for terms.", REPO_URL
        )
        self.assertEqual(
            rewritten,
            "See the [domain glossary]"
            "(https://github.com/DUNE/hep-metadex/blob/main/glossary/domain.md) for terms.",
        )

    def test_preserves_anchor_fragment_on_rewritten_link(self):
        rewritten, _ = docs_site.rewrite_out_of_tree_links(
            "Try the [README quick start](../README.md#quick-start).", REPO_URL
        )
        self.assertEqual(
            rewritten,
            "Try the [README quick start]"
            "(https://github.com/DUNE/hep-metadex/blob/main/README.md#quick-start).",
        )

    def test_keeps_leading_dot_of_dotfile_targets(self):
        rewritten, _ = docs_site.rewrite_out_of_tree_links(
            "CI runs [validate.yml](../.github/workflows/validate.yml).", REPO_URL
        )
        self.assertEqual(
            rewritten,
            "CI runs [validate.yml]"
            "(https://github.com/DUNE/hep-metadex/blob/main/.github/workflows/validate.yml).",
        )

    def test_rewrites_every_link_on_a_line_with_several(self):
        rewritten, _ = docs_site.rewrite_out_of_tree_links(
            "The [spec index](../glossary/technical.md) and "
            "[ADR-0003](../adr/0003-fenced-gherkin-single-source-validation-gate.md) both apply.",
            REPO_URL,
        )
        self.assertEqual(
            rewritten,
            "The [spec index](https://github.com/DUNE/hep-metadex/blob/main/glossary/technical.md) and "
            "[ADR-0003]"
            "(https://github.com/DUNE/hep-metadex/blob/main/"
            "adr/0003-fenced-gherkin-single-source-validation-gate.md) both apply.",
        )

    def test_strips_all_parent_prefixes_from_nested_targets(self):
        rewritten, _ = docs_site.rewrite_out_of_tree_links(
            "See [ADR-0001](../../adr/0001-serve-experiments-via-readonly-store-references.md).",
            REPO_URL,
        )
        self.assertEqual(
            rewritten,
            "See [ADR-0001]"
            "(https://github.com/DUNE/hep-metadex/blob/main/"
            "adr/0001-serve-experiments-via-readonly-store-references.md).",
        )

    def test_leaves_in_tree_relative_links_untouched(self):
        text = "Continue with [setup](setup.md), [usage](usage.md#anchor), or [top](#section)."
        rewritten, count = docs_site.rewrite_out_of_tree_links(text, REPO_URL)
        self.assertEqual(rewritten, text)
        self.assertEqual(count, 0)

    def test_leaves_absolute_urls_untouched(self):
        text = (
            "The site lives at [dune.github.io](https://dune.github.io/hep-metadex/) — "
            "see [the repo](https://github.com/DUNE/hep-metadex)."
        )
        rewritten, count = docs_site.rewrite_out_of_tree_links(text, REPO_URL)
        self.assertEqual(rewritten, text)
        self.assertEqual(count, 0)

    def test_uses_repo_url_ending_in_slash_without_doubling_it(self):
        rewritten, _ = docs_site.rewrite_out_of_tree_links(
            "See the [domain glossary](../glossary/domain.md) for terms.",
            "https://github.com/DUNE/hep-metadex/",
        )
        self.assertEqual(
            rewritten,
            "See the [domain glossary]"
            "(https://github.com/DUNE/hep-metadex/blob/main/glossary/domain.md) for terms.",
        )

    def test_leaves_links_inside_fenced_code_blocks_untouched(self):
        text = (
            "Before [link](../glossary/domain.md)\n"
            "```text\n"
            "cd ../glossary or see [sample](../glossary/domain.md)\n"
            "```\n"
            "After [link](../glossary/domain.md)\n"
        )
        rewritten, count = docs_site.rewrite_out_of_tree_links(text, REPO_URL)
        self.assertIn("cd ../glossary or see [sample](../glossary/domain.md)", rewritten)
        self.assertEqual(count, 2)

    def test_reports_the_number_of_links_rewritten(self):
        text = (
            "[a](../glossary/technical.md)\n"
            "[b](../glossary/domain.md) and [c](../README.md#quick-start)\n"
        )
        _, count = docs_site.rewrite_out_of_tree_links(text, REPO_URL)
        self.assertEqual(count, 3)


class LoadConfigTest(unittest.TestCase):
    def test_returns_the_parsed_settings(self):
        with tempfile.TemporaryDirectory() as tmp:
            config_path = Path(tmp) / "zensical.toml"
            config_path.write_text(
                "[project]\n"
                'site_name = "hep-metadex"\n'
                'repo_url = "https://github.com/DUNE/hep-metadex"\n'
                'docs_dir = "docs"\n',
                encoding="utf-8",
            )
            config = docs_site.load_config(config_path)
        self.assertEqual(config["project"]["site_name"], "hep-metadex")
        self.assertEqual(config["project"]["repo_url"], "https://github.com/DUNE/hep-metadex")
        self.assertEqual(config["project"]["docs_dir"], "docs")

    def test_fails_with_clear_message_when_config_is_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            config_path = Path(tmp) / "zensical.toml"
            with self.assertRaises(docs_site.DocsSiteError) as raised:
                docs_site.load_config(config_path)
        self.assertIn("zensical.toml", str(raised.exception))

    def test_fails_with_clear_message_when_repo_url_is_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            config_path = Path(tmp) / "zensical.toml"
            config_path.write_text(
                "[project]\n"
                'site_name = "hep-metadex"\n'
                'docs_dir = "docs"\n',
                encoding="utf-8",
            )
            with self.assertRaises(docs_site.DocsSiteError) as raised:
                docs_site.load_config(config_path)
        self.assertIn("repo_url", str(raised.exception))


class DeriveConfigTest(unittest.TestCase):
    def test_points_docs_dir_at_the_staging_tree(self):
        config = {
            "project": {
                "site_name": "hep-metadex",
                "repo_url": REPO_URL,
                "docs_dir": "docs",
            }
        }
        derived = tomllib.loads(docs_site.derive_config_text(config))
        self.assertEqual(derived["project"]["docs_dir"], ".site-src")

    def test_passes_every_other_setting_through_unchanged(self):
        config = {
            "project": {
                "site_name": "hep-metadex",
                "site_url": "https://dune.github.io/hep-metadex/",
                "repo_url": REPO_URL,
                "docs_dir": "docs",
                "site_dir": "site",
                "strict": True,
            }
        }
        derived = tomllib.loads(docs_site.derive_config_text(config))
        expected = {
            "project": {
                "site_name": "hep-metadex",
                "site_url": "https://dune.github.io/hep-metadex/",
                "repo_url": REPO_URL,
                "docs_dir": ".site-src",
                "site_dir": "site",
                "strict": True,
            }
        }
        self.assertEqual(derived, expected)

    def test_emits_theme_as_a_nested_project_table(self):
        config = {
            "project": {
                "site_name": "hep-metadex",
                "repo_url": REPO_URL,
                "docs_dir": "docs",
                "theme": {"name": "plin"},
            }
        }
        derived = tomllib.loads(docs_site.derive_config_text(config))
        self.assertEqual(derived["project"]["theme"], {"name": "plin"})

    def test_emits_nav_arrays_with_strings_and_inline_tables(self):
        config = {
            "project": {
                "site_name": "hep-metadex",
                "repo_url": REPO_URL,
                "docs_dir": "docs",
                "nav": ["index.md", {"Setup": "setup.md"}, "usage.md"],
            }
        }
        derived = tomllib.loads(docs_site.derive_config_text(config))
        self.assertEqual(
            derived["project"]["nav"], ["index.md", {"Setup": "setup.md"}, "usage.md"]
        )


class StageDocsTest(unittest.TestCase):
    def test_wipes_stale_files_from_previous_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            docs.mkdir()
            (docs / "index.md").write_text("# Home\n", encoding="utf-8")
            staging = root / ".site-src"
            staging.mkdir()
            (staging / "stale-page.md").write_text("# Stale\n", encoding="utf-8")
            docs_site.stage_docs(docs, staging, REPO_URL)
            self.assertFalse((staging / "stale-page.md").exists())
            self.assertTrue((staging / "index.md").is_file())

    def test_copies_the_whole_docs_tree_recursively(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            (docs / "sub").mkdir(parents=True)
            (docs / "index.md").write_text("# Home\n", encoding="utf-8")
            (docs / "sub" / "page.md").write_text("# Sub\n", encoding="utf-8")
            (docs / "sub" / "asset.png").write_bytes(b"\x89PNG fake")
            staging = root / ".site-src"
            docs_site.stage_docs(docs, staging, REPO_URL)
            self.assertTrue((staging / "index.md").is_file())
            self.assertTrue((staging / "sub" / "page.md").is_file())
            self.assertEqual(
                (staging / "sub" / "asset.png").read_bytes(), b"\x89PNG fake"
            )

    def test_rewrites_links_in_the_staged_copy_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            docs.mkdir()
            source = docs / "usage.md"
            source_text = "See the [glossary](../glossary/domain.md).\n"
            source.write_text(source_text, encoding="utf-8")
            staging = root / ".site-src"
            docs_site.stage_docs(docs, staging, REPO_URL)
            staged = (staging / "usage.md").read_text(encoding="utf-8")
            self.assertIn(
                "(https://github.com/DUNE/hep-metadex/blob/main/glossary/domain.md)",
                staged,
            )
            self.assertEqual(source.read_text(encoding="utf-8"), source_text)

    def test_reports_pages_staged_and_links_rewritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            docs.mkdir()
            (docs / "index.md").write_text(
                "[a](../glossary/domain.md)\n", encoding="utf-8"
            )
            (docs / "usage.md").write_text(
                "[b](../glossary/technical.md) [c](../README.md#quick-start)\n",
                encoding="utf-8",
            )
            (docs / "asset.png").write_bytes(b"\x89PNG fake")
            pages, rewritten = docs_site.stage_docs(
                docs, root / ".site-src", REPO_URL
            )
            self.assertEqual(pages, 2)
            self.assertEqual(rewritten, 3)

    def test_fails_with_clear_message_when_docs_dir_is_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(docs_site.DocsSiteError) as raised:
                docs_site.stage_docs(root / "docs", root / ".site-src", REPO_URL)
        self.assertIn("docs", str(raised.exception))


if __name__ == "__main__":
    unittest.main()
