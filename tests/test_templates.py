import unittest
import os

class TestTemplates(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Resolve paths relative to the project root
        cls.project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        cls.skill_md_path = os.path.join(cls.project_root, "SKILL.md")
        cls.result_template_path = os.path.join(cls.project_root, "RESULT-TEMPLATE.md")
        cls.source_register_path = os.path.join(cls.project_root, "SOURCE-REGISTER.md")

    def _check_expected_strings(self, filepath, expected_strings):
        self.assertTrue(os.path.exists(filepath), f"{os.path.basename(filepath)} does not exist")
        found_strings = set()
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                for expected in expected_strings:
                    if expected in line:
                        found_strings.add(expected)
                if len(found_strings) == len(expected_strings):
                    break

        for expected in expected_strings:
            self.assertIn(expected, found_strings, f"Expected string '{expected}' not found in {filepath}")

    def test_skill_md_exists_and_contains_expected_headers(self):
        expected_strings = [
            "# 音樂與 MV 製作入門",
            "## 把聲音與畫面放在同一張企劃",
            "## 留下可接手的製作紀錄",
            "## 用具體問題收回饋",
            "## 完成時交付"
        ]
        self._check_expected_strings(self.skill_md_path, expected_strings)

    def test_result_template_md_exists_and_contains_expected_structure(self):
        expected_strings = [
            "# 歌曲與 MV 成果卡",
            "## 聲音與畫面企劃",
            "| 段落／時間 | 歌詞或聲音線索 | 情緒／節奏 | 畫面與鏡頭 | 負責人 | 素材 ref |",
            "## 製作與交付",
            "## 回饋與下一步"
        ]
        self._check_expected_strings(self.result_template_path, expected_strings)

    def test_source_register_md_exists_and_contains_expected_structure(self):
        expected_strings = [
            "# 素材來源紀錄",
            "| 素材／檔名 | 作者或來源 | 原始連結／私人證據 ref | 可使用範圍與限制 | 署名方式 | 本次用途 | 核對者／日期 |"
        ]
        self._check_expected_strings(self.source_register_path, expected_strings)

if __name__ == '__main__':
    unittest.main()
