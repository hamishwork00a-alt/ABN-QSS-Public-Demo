"""
ABN-QSS 基础测试用例
验证核心功能的基本正确性
"""
import unittest
import sys
import os

# 添加父目录到路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from abn_qss_demo import QuantumResearchPlatform, MaterialScienceTools, PharmaResearchTools

class TestQuantumPlatform(unittest.TestCase):
    """量子平台基础测试"""
    
    def setUp(self):
        self.platform = QuantumResearchPlatform(domain="materials")
    
    def test_platform_initialization(self):
        """测试平台初始化"""
        self.assertIsNotNone(self.platform)
        self.assertEqual(self.platform.domain, "materials")
    
    def test_material_screening(self):
        """测试材料筛选功能"""
        target_properties = {
            "band_gap": (1.0, 2.0),
            "stability": "high"
        }
        
        results = self.platform.demo_material_screening(target_properties)
        
        # 验证返回结构
        self.assertIn("candidates", results)
        self.assertIn("best_efficiency", results)
        self.assertIn("quantum_enhancement", results)
        
        # 验证数据类型
        self.assertIsInstance(results["candidates"], list)
        self.assertIsInstance(results["best_efficiency"], (int, float))
        self.assertGreater(len(results["candidates"]), 0)

class TestMaterialTools(unittest.TestCase):
    """材料科学工具测试"""
    
    def test_crystal_analysis(self):
        """测试晶体结构分析"""
        composition = "Perovskite_CsPbI3"
        target_properties = {"band_gap": "tunable"}
        
        results = MaterialScienceTools.quantum_crystal_analysis(
            composition, target_properties
        )
        
        self.assertIn("stable_phases", results)
        self.assertIn("recommended_phase", results)
        self.assertEqual(results["composition"], composition)

class TestPharmaTools(unittest.TestCase):
    """药物研发工具测试"""
    
    def test_docking_screen(self):
        """测试分子对接筛选"""
        results = PharmaResearchTools.quantum_docking_screen(
            target_pdb="7T9L",
            compound_library="ZINC20_Fragment",
            top_k=3
        )
        
        self.assertIn("top_compounds", results)
        self.assertIn("quantum_improvement", results)
        self.assertEqual(len(results["top_compounds"]), 3)
    
    def test_admet_prediction(self):
        """测试ADMET预测"""
        compound_data = {"compound_id": "TEST_001"}
        results = PharmaResearchTools.admet_prediction(compound_data)
        
        self.assertIn("absorption", results)
        self.assertIn("toxicity", results)
        self.assertIn("overall_score", results)

def run_tests():
    """运行所有测试"""
    print("🧪 运行 ABN-QSS 测试套件...")
    unittest.main(verbosity=2, exit=False)

if __name__ == "__main__":
    run_tests()
