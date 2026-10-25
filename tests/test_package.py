import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PluginPackageTests(unittest.TestCase):
    def test_codex_and_claude_versions_match(self):
        codex = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        claude = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(codex["version"], claude["version"])

    def test_declared_skill_and_icon_exist(self):
        codex = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        claude = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / "skills" / "project-docs" / "SKILL.md").is_file())
        self.assertTrue((ROOT / claude["icon"].removeprefix("./")).is_file())
        self.assertTrue((ROOT / "assets" / "icon.png").is_file())
        self.assertEqual(codex["license"], claude["license"])


if __name__ == "__main__":
    unittest.main()