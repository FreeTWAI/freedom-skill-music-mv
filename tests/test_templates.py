import unittest
import os

class TestTemplates(unittest.TestCase):
    def setUp(self):
        # Resolve paths relative to the project root
        self.project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.skill_md_path = os.path.join(self.project_root, "SKILL.md")
        self.result_template_path = os.path.join(self.project_root, "RESULT-TEMPLATE.md")
        self.source_register_path = os.path.join(self.project_root, "SOURCE-REGISTER.md")

    def test_skill_md_exists_and_contains_expected_headers(self):
        self.assertTrue(os.path.exists(self.skill_md_path), "SKILL.md does not exist")
        with open(self.skill_md_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("# 音樂與 MV 製作入門", content)
            self.assertIn("## 把聲音與畫面放在同一張企劃", content)
            self.assertIn("## 留下可接手的製作紀錄", content)
            self.assertIn("## 用具體問題收回饋", content)
            self.assertIn("## 完成時交付", content)

    def test_result_template_md_exists_and_contains_expected_structure(self):
        self.assertTrue(os.path.exists(self.result_template_path), "RESULT-TEMPLATE.md does not exist")
        with open(self.result_template_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("# 歌曲與 MV 成果卡", content)
            self.assertIn("## 聲音與畫面企劃", content)
            self.assertIn("| 段落／時間 | 歌詞或聲音線索 | 情緒／節奏 | 畫面與鏡頭 | 負責人 | 素材 ref |", content)
            self.assertIn("## 製作與交付", content)
            self.assertIn("## 回饋與下一步", content)

    def test_source_register_md_exists_and_contains_expected_structure(self):
        self.assertTrue(os.path.exists(self.source_register_path), "SOURCE-REGISTER.md does not exist")
        with open(self.source_register_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("# 素材來源紀錄", content)
            self.assertIn("| 素材／檔名 | 作者或來源 | 原始連結／私人證據 ref | 可使用範圍與限制 | 署名方式 | 本次用途 | 核對者／日期 |", content)

if __name__ == '__main__':
    unittest.main()
