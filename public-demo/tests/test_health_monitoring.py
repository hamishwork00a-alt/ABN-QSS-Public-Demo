"""
健康监测模块测试用例
"""
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from abn_qss_demo.health_monitoring import HealthMonitoringSystem, MetabolicMirror

class TestHealthMonitoring(unittest.TestCase):
    """健康监测系统测试"""
    
    def setUp(self):
        self.health_system = HealthMonitoringSystem()
        self.baseline_data = {
            "heart_rate": 72,
            "hrv": 45,
            "blood_oxygen": 98,
            "skin_conductance": 2.5,
            "temperature": 36.8,
            "impedance": 480
        }
    
    def test_system_initialization(self):
        """测试系统初始化"""
        baseline = self.health_system.initialize_baseline(self.baseline_data)
        
        self.assertIn("network_structure", baseline)
        self.assertIn("resilience_score", baseline)
        self.assertIn("dynamic_range", baseline)  # 新增检查
        self.assertGreater(baseline["resilience_score"], 0.5)
    
    def test_dynamic_range_calculation(self):
        """测试动态范围计算"""
        self.health_system.initialize_baseline(self.baseline_data)
        # 验证dynamic_range方法存在
        self.assertTrue(hasattr(self.health_system, '_calculate_dynamic_ranges'))
    
    def test_real_time_monitoring(self):
        """测试实时监测"""
        self.health_system.initialize_baseline(self.baseline_data)
        
        current_data = {
            "heart_rate": 75,
            "hrv": 42,
            "blood_oxygen": 97,
            "skin_conductance": 2.8,
            "temperature": 36.8,
            "impedance": 478
        }
        
        result = self.health_system.real_time_monitoring(current_data)
        
        self.assertIn("deviation_score", result)
        self.assertIn("system_harmony", result)
        self.assertIsInstance(result["metastable_alerts"], list)

class TestMetabolicMirror(unittest.TestCase):
    """代谢之镜测试"""
    
    def test_metabolic_analysis(self):
        """测试代谢分析"""
        physio_data = {
            "heart_rate": 75,
            "hrv": 42,
            "blood_oxygen": 97
        }
        
        result = MetabolicMirror.non_invasive_metabolic_analysis(physio_data)
        
        self.assertIn("glucose_trend", result)
        self.assertIn("lactate_level", result)
        self.assertIn("metabolic_flexibility", result)

def run_health_tests():
    """运行健康监测测试"""
    print("🧪 运行健康监测测试套件...")
    unittest.main(verbosity=2, exit=False)

if __name__ == "__main__":
    run_health_tests()
