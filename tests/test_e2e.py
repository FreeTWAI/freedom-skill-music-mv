import unittest

class TestE2EMusicVideo(unittest.TestCase):
    def test_storyboard_timeline_parsing(self):
        """Verify storyboard timeline parsing."""
        with open('RESULT-TEMPLATE.md', 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('## 聲音與畫面企劃', content)
        self.assertIn('| 段落／時間 | 歌詞或聲音線索 | 情緒／節奏 | 畫面與鏡頭 | 負責人 | 素材 ref |', content)

    def test_asset_cue_sheet_validation(self):
        """Verify asset cue sheet validation."""
        with open('SOURCE-REGISTER.md', 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('| 素材／檔名 | 作者或來源 | 原始連結／私人證據 ref | 可使用範圍與限制 | 署名方式 | 本次用途 | 核對者／日期 |', content)
        self.assertIn('待填', content)

    def test_production_spec_verification(self):
        """Verify production spec verification."""
        with open('RESULT-TEMPLATE.md', 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('## 製作與交付', content)
        self.assertIn('- 聲音製作方式與工具：', content)
        self.assertIn('- 影像製作方式與工具：', content)
        self.assertIn('- 成果連結／私人 ref：', content)
        self.assertIn('- 音訊規格：', content)
        self.assertIn('- 影片尺寸、幀率與字幕：', content)

if __name__ == '__main__':
    unittest.main()
