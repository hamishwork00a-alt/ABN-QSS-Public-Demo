# 在文件开头添加导入
import matplotlib.pyplot as plt
from .font_utils import safe_plot_with_chinese, setup_chinese_font

# 在 HealthMonitoringSystem 类中添加可视化方法
class HealthMonitoringSystem:
    """健康监测系统 - 基于自平衡计算网络"""
    
    # ... 现有代码保持不变
    
    def plot_health_analysis(self, baseline_state, current_state):
        """绘制健康分析图表 - 支持中文"""
        def _plot_function():
            # 网络节点强度对比
            nodes = list(baseline_state["network_structure"]["node_strengths"].keys())
            baseline_strengths = list(baseline_state["network_structure"]["node_strengths"].values())
            current_strengths = list(current_state["current_state"]["node_strengths"].values())
            
            x = np.arange(len(nodes))
            width = 0.35
            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
            
            # 节点强度对比
            ax1.bar(x - width/2, baseline_strengths, width, label='基线状态', alpha=0.7)
            ax1.bar(x + width/2, current_strengths, width, label='当前状态', alpha=0.7)
            ax1.set_xticks(x)
            ax1.set_xticklabels(['心脏', '呼吸', '代谢', '神经', '免疫', '内分泌', '体温'])
            ax1.legend()
            
            # 系统和谐度
            metrics = ['系统韧性', '和谐指数', '网络稳定性']
            values = [
                baseline_state['resilience_score'],
                baseline_state['harmony_index'], 
                current_state['system_harmony']
            ]
            
            ax2.bar(metrics, values, color=['lightgreen', 'lightblue', 'lightcoral'])
            ax2.set_ylim(0, 1)
            
            # 在柱状图上显示数值
            for i, v in enumerate(values):
                ax2.text(i, v + 0.01, f'{v:.3f}', ha='center', va='bottom')
        
        # 使用安全绘图函数
        safe_plot_with_chinese(
            title='健康状态分析',
            xlabel='生理系统',
            ylabel='强度/评分',
            plot_function=_plot_function,
            grid=True
        )

# 更新演示函数
def demo_health_monitoring():
    """健康监测演示 - 修复中文显示"""
    print("🩺 ABN-QSS 健康监测系统演示")
    print("=" * 60)
    print("🎵 聆听身体交响乐，感知健康状态...")
    
    # 初始化健康监测系统
    health_system = HealthMonitoringSystem()
    
    # 模拟用户基线数据
    baseline_data = {
        "heart_rate": 72,
        "hrv": 45,
        "blood_oxygen": 98,
        "skin_conductance": 2.5,
        "temperature": 36.8,
        "impedance": 480
    }
    
    print("\n1. 建立健康基态...")
    baseline = health_system.initialize_baseline(baseline_data)
    print(f"   🎯 系统韧性: {baseline['resilience_score']:.3f}")
    print(f"   🎵 和谐指数: {baseline['harmony_index']:.3f}")
    
    # 模拟当前状态（轻微偏离）
    current_data = {
        "heart_rate": 78,  # 轻微升高
        "hrv": 38,        # 变异性降低
        "blood_oxygen": 96,
        "skin_conductance": 3.2,  # 压力反应
        "temperature": 36.9,
        "impedance": 475
    }
    
    print("\n2. 实时状态分析...")
    current_state = health_system.real_time_monitoring(current_data)
    
    print(f"   📊 网络偏离度: {current_state['deviation_score']:.3f}")
    print(f"   🎶 系统和谐度: {current_state['system_harmony']:.3f}")
    
    if current_state['metastable_alerts']:
        print("\n   ⚠️ 健康洞察:")
        for alert in current_state['metastable_alerts']:
            print(f"      {alert}")
    
    print("\n3. 代谢之镜分析...")
    metabolic_analysis = MetabolicMirror.non_invasive_metabolic_analysis(current_data)
    
    print(f"   🩸 血糖趋势: {metabolic_analysis['glucose_trend']['value']} mg/dL")
    print(f"   🥛 乳酸水平: {metabolic_analysis['lactate_level']} mmol/L")
    print(f"   🔥 代谢灵活性: {metabolic_analysis['metabolic_flexibility']:.3f}")
    
    print("\n4. 可视化分析...")
    # 绘制健康分析图表
    health_system.plot_health_analysis(baseline, current_state)
    
    print("\n" + "=" * 60)
    print("🎉 健康监测演示完成!")
    print("💡 这展示了ABN-QSS在无创健康监测中的潜力")
    print("🔬 从'观察症状'到'感知状态'的范式转变")
    
    return {
        "baseline": baseline,
        "current_state": current_state,
        "metabolic_analysis": metabolic_analysis
    }
