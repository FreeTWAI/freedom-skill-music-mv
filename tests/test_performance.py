import unittest
import os
import time

class TestPerformance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Resolve paths relative to the project root
        cls.project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        cls.skill_md_path = os.path.join(cls.project_root, "SKILL.md")
        cls.result_template_path = os.path.join(cls.project_root, "RESULT-TEMPLATE.md")
        cls.source_register_path = os.path.join(cls.project_root, "SOURCE-REGISTER.md")

    def _benchmark_file_read(self, filepath, max_latency_seconds=0.1):
        self.assertTrue(os.path.exists(filepath), f"{os.path.basename(filepath)} does not exist")

        start_time = time.perf_counter()

        # Read the file to benchmark latency
        with open(filepath, "r", encoding="utf-8") as f:
            for _ in f:
                pass

        end_time = time.perf_counter()
        latency = end_time - start_time

        self.assertLess(latency, max_latency_seconds, f"Reading {os.path.basename(filepath)} took {latency:.4f}s, which exceeds the threshold of {max_latency_seconds}s")

    def test_skill_md_read_latency(self):
        self._benchmark_file_read(self.skill_md_path)

    def test_result_template_md_read_latency(self):
        self._benchmark_file_read(self.result_template_path)

    def test_source_register_md_read_latency(self):
        self._benchmark_file_read(self.source_register_path)

if __name__ == '__main__':
    unittest.main()
