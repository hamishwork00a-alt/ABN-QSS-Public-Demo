# 在文件开头添加导入
from typing import Dict, List, Optional  # 添加这行导入
from .font_utils import safe_plot_with_chinese, setup_chinese_font

# 修改 MaterialScienceTools 类中的 plot_material_properties 方法
class MaterialScienceTools:
    """材料科学工具集"""

    @staticmethod
    def plot_material_properties(results: Dict):  # 现在 Dict 已定义
        """绘制材料性质图表 - 修复中文显示"""
        # ... 其余代码保持不变
        def _plot_function():
            if "candidates" in results:
                materials = [c["material_id"] for c in results["candidates"]]
                efficiencies = [c["efficiency"] for c in results["candidates"]]
                stabilities = [c["stability"] for c in results["candidates"]]
                
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
                
                # 效率图表
                ax1.bar(materials, efficiencies, color='skyblue')
                ax1.tick_params(axis='x', rotation=45)
                
                # 稳定性图表
                ax2.bar(materials, stabilities, color='lightcoral')
                ax2.tick_params(axis='x', rotation=45)
        
        # 使用安全绘图函数
        safe_plot_with_chinese(
            title='材料性质分析',
            xlabel='材料编号',
            ylabel='数值',
            plot_function=_plot_function,
            grid=True
        )
    
    # ... 其他方法保持不变
