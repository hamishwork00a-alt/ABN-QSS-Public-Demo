#!/usr/bin/env python3
"""
ABN-QSS 公开演示使用示例
展示量子增强科研计算的基本用法
"""
import sys
import os

# 添加当前目录到路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from abn_qss_demo.health_monitoring import HealthMonitoringSystem, MetabolicMirror
from abn_qss_demo.safe_core import QuantumResearchPlatform, MaterialScienceTools, PharmaResearchTools

def demo_material_science():
    """材料科学演示"""
    print("=" * 60)
    print("🔬 ABN-QSS 材料科学演示")
    print("=" * 60)
    
    # 初始化平台
    platform = QuantumResearchPlatform(domain="materials")
    
    # 材料筛选演示
    print("\n1. 量子增强材料筛选")
    target_props = {
        "band_gap": (1.0, 2.0),
        "stability": "high", 
        "efficiency": ">80%"
    }
    
    results = platform.demo_material_screening(target_props)
    
    print(f"✅ 找到 {len(results['candidates'])} 个候选材料")
    print(f"🎯 最佳效率: {results['best_efficiency']}%")
    print(f"⚡ 量子增强: +{results['quantum_enhancement']}%")
    
    # 显示候选材料
    print("\n📊 候选材料列表:")
    for candidate in results["candidates"]:
        print(f"   {candidate['material_id']}: {candidate['efficiency']}% 效率, " 
              f"{candidate['stability']} 稳定性")
    
    # 性质预测演示
    print("\n2. 量子性质预测")
    composition = "Perovskite_CsPbI3"
    properties = ["band_gap", "conductivity", "stability"]
    
    predictions = platform.quantum_property_prediction(composition, properties)
    
    print(f"🎯 材料: {predictions['composition']}")
    for prop, value in predictions["predictions"].items():
        print(f"   {prop}: {value}")
    print(f"📈 预测置信度: {predictions['quantum_confidence']}")
    
    # 可视化结果
    print("\n3. 结果可视化")
    MaterialScienceTools.plot_material_properties(results)
    
    return results

def demo_pharma_research():
    """药物研发演示"""
    print("\n" + "=" * 60)
    print("💊 ABN-QSS 药物研发演示") 
    print("=" * 60)
    
    tools = PharmaResearchTools()
    
    # 分子对接演示
    print("\n1. 量子增强分子对接筛选")
    docking_results = tools.quantum_docking_screen(
        target_pdb="7T9L",  # 示例靶点
        compound_library="ZINC20_Fragment",
        top_k=3
    )
    
    print(f"🎯 靶点: {docking_results['target']}")
    print(f"📚 化合物库: {docking_results['library']}")
    print(f"⚡ {docking_results['quantum_improvement']}")
    
    print("\n🏆 最佳候选化合物:")
    for compound in docking_results["top_compounds"]:
        print(f"   {compound['compound_id']}:")
        print(f"     对接分数: {compound['docking_score']}")
        print(f"     量子增强: +{compound['quantum_enhancement']}")
        print(f"     结合亲和力: {compound['binding_affinity']}")
        
        # ADMET预测
        admet = tools.admet_prediction(compound)
        print(f"     ADMET综合评分: {admet['overall_score']}")
    
    return docking_results

def demo_health_monitoring():
    """健康监测系统演示"""
    print("\n" + "=" * 60)
    print("🩺 ABN-QSS 健康监测系统演示")
    print("=" * 60)
    
    try:
        from abn_qss_demo.health_monitoring import demo_health_monitoring as health_demo
        return health_demo()
    except ImportError:
        print("❌ 健康监测模块未找到")
        return None

def main():
    """主演示函数 - 更新版本"""
    try:
        print("🚀 启动 ABN-QSS 量子增强科研平台演示")
        print("📍 注意: 此为公开演示版本，展示技术潜力")
        
        # 运行材料科学演示
        material_results = demo_material_science()
        
        # 运行药物研发演示  
        pharma_results = demo_pharma_research()
        
        # 运行健康监测演示
        health_results = demo_health_monitoring()
        
        print("\n" + "=" * 60)
        print("🎉 所有演示完成!")
        print("=" * 60)
        print("💡 应用领域:")
        print("   🔬 材料科学 - 加速新材料发现")
        print("   💊 药物研发 - 提升筛选效率") 
        print("   🩺 健康监测 - 无创生理状态感知")
        print("\n📞 合作咨询: landsingchang@gmail.com")
        print("🔗 GitHub: https://github.com/hamishwork00a-alt/ABN-QSS-Public-Demo")
        
    except Exception as e:
        print(f"❌ 演示过程中出现错误: {e}")
        print("💡 请确保已安装所有依赖: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
