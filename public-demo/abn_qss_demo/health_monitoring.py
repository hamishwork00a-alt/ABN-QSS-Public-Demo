from typing import Dict, List, Optional, Any
import numpy as np

class MetabolicMirror:
    """代谢镜像：无创代谢监测系统"""
    
    def __init__(self):
        self.metabolic_baseline = None
        
    def set_baseline(self, baseline_data: Dict) -> None:
        """设置代谢基线"""
        self.metabolic_baseline = baseline_data
        
    def analyze_metabolic_state(self, current_data: Dict) -> Dict:
        """分析当前代谢状态"""
        if self.metabolic_baseline is None:
            raise ValueError("请先设置代谢基线")
            
        # 简化的代谢状态分析算法
        impedance_ratio = current_data.get('impedance', 1) / self.metabolic_baseline.get('impedance', 1)
        heart_rate_ratio = current_data.get('heart_rate', 1) / self.metabolic_baseline.get('heart_rate', 1)
        
        metabolic_rate = (impedance_ratio + heart_rate_ratio) / 2
        
        return {
            "metabolic_rate": metabolic_rate,
            "state": "normal" if 0.9 < metabolic_rate < 1.1 else "abnormal",
            "confidence": 0.85
        }
    
    @staticmethod
    def non_invasive_metabolic_analysis(current_data: Dict) -> Dict:
        """无创代谢分析"""
        glucose_value = 95 + (current_data.get('heart_rate', 72) - 72) * 0.5
        lactate_level = 1.2 + (current_data.get('skin_conductance', 2.5) - 2.5) * 0.1
        
        return {
            "glucose_trend": {
                "value": glucose_value,
                "trend": "stable" if 70 <= glucose_value <= 110 else "variable"
            },
            "lactate_level": lactate_level,
            "ketone_bodies": 0.3,
            "metabolic_flexibility": 0.85
        }

class HealthMonitoringSystem:
    """健康监测系统：自平衡计算网络生理分析"""
    
    def __init__(self):
        self.baseline = None
        self.metabolic_mirror = MetabolicMirror()
        
    def initialize_baseline(self, baseline_data: Dict) -> Dict:
        """建立健康基线"""
        self.baseline = baseline_data
        self.metabolic_mirror.set_baseline(baseline_data)
        
        # 计算韧性分数
        resilience_score = self._calculate_resilience(baseline_data)
        harmony_index = self._calculate_harmony_index(baseline_data)
        
        return {
            **baseline_data,
            "resilience_score": resilience_score,
            "harmony_index": harmony_index,
            "status": "baseline_established"
        }
        
    def real_time_monitoring(self, current_data: Dict) -> Dict:
        """实时监测当前生理状态"""
        if self.baseline is None:
            raise ValueError("请先调用 initialize_baseline 初始化基线")
            
        # 计算偏离分数
        deviation_score = self._calculate_deviation(current_data)
        # 计算系统和谐度
        system_harmony = self._calculate_harmony(deviation_score)
        # 代谢分析
        metabolic_analysis = self.metabolic_mirror.analyze_metabolic_state(current_data)
        
        # 生成洞察提醒
        metastable_alerts = self._generate_insights(deviation_score, metabolic_analysis)
        
        return {
            "deviation_score": deviation_score,
            "system_harmony": system_harmony,
            "metabolic_analysis": metabolic_analysis,
            "metastable_alerts": metastable_alerts,
            "health_status": "optimal" if system_harmony > 0.8 else "suboptimal"
        }
        
    def _calculate_resilience(self, data: Dict) -> float:
        """计算系统韧性分数"""
        hrv = data.get('hrv', 0)
        impedance = data.get('impedance', 1)
        return (hrv / 100) + (impedance / 1000)
    
    def _calculate_harmony_index(self, data: Dict) -> float:
        """计算和谐指数"""
        heart_rate = data.get('heart_rate', 72)
        hrv = data.get('hrv', 45)
        # 简化的和谐指数计算
        return 0.7 + (hrv / 200) - (abs(heart_rate - 72) / 100)
        
    def _calculate_deviation(self, current_data: Dict) -> float:
        """计算与基线的偏离度"""
        if self.baseline is None:
            return 1.0
            
        total_deviation = 0
        count = 0
        for key in self.baseline:
            if key in current_data and key not in ['resilience_score', 'harmony_index', 'status']:
                baseline_val = self.baseline[key]
                current_val = current_data[key]
                if baseline_val != 0:
                    deviation = abs(current_val - baseline_val) / baseline_val
                    total_deviation += deviation
                    count += 1
        return total_deviation / count if count > 0 else 0
        
    def _calculate_harmony(self, deviation_score: float) -> float:
        """计算系统和谐度"""
        # 偏离度越小，和谐度越高
        return 1.0 / (1.0 + deviation_score * 10)
    
    def _generate_insights(self, deviation_score: float, metabolic_analysis: Dict) -> List[str]:
        """生成系统洞察"""
        alerts = []
        if deviation_score > 0.15:
            alerts.append("⚠️ 系统检测到显著生理偏离，建议适当休息")
        if metabolic_analysis['state'] == 'abnormal':
            alerts.append("🔍 代谢状态异常，建议关注血糖水平")
        if not alerts:
            alerts.append("✅ 系统运行在和谐状态")
        return alerts
