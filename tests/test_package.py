import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class PluginPackageTests(unittest.TestCase):
    def test_codex_and_claude_versions_match(self):
        codex = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        claude = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(codex["version"], claude["version"])

    def test_packaged_skills_and_icons_exist(self):
        codex = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        claude = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(
            {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")},
            {"project-docs", "project-docs-human", "project-docs-agent"},
        )
        self.assertTrue((ROOT / claude["icon"].removeprefix("./")).is_file())
        self.assertTrue((ROOT / "assets" / "icon.png").is_file())
        self.assertEqual(codex["license"], claude["license"])

    def test_local_markdown_link_targets_exist(self):
        documents = [ROOT / "README.md"]
        for directory in (ROOT / "docs", ROOT / "skills", ROOT / "tests" / "fixtures"):
            documents.extend(directory.rglob("*.md"))
        for document in documents:
            content = document.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", content):
                link = urlsplit(target)
                if link.scheme or link.netloc or not link.path:
                    continue
                with self.subTest(document=document.relative_to(ROOT), target=target):
                    self.assertTrue((document.parent / unquote(link.path)).exists())


if __name__ == "__main__":
    unittest.main()
