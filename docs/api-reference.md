# ABN-QSS API 参考手册

## 核心类概述

### QuantumResearchPlatform
主要的量子增强研究平台入口点。

**初始化**
```python
platform = QuantumResearchPlatform(domain="materials")
```

参数

· domain (str): 研究领域，可选 "materials" 或 "pharma"

方法

demo_material_screening(target_properties)

执行量子增强材料筛选。

参数

· target_properties (dict): 目标材料属性字典

返回

```python
{
    "candidates": [
        {
            "material_id": "MAT_001",
            "efficiency": 82.5,
            "stability": 0.891,
            "synthesis_complexity": "Medium"
        }
    ],
    "best_efficiency": 82.5,
    "quantum_enhancement": 12.3,
    "computation_time": "2-3 hours (simulated)"
}
```

quantum_property_prediction(composition, properties)

执行量子增强性质预测。

参数

· composition (str): 材料化学式
· properties (list): 需要预测的性质列表

返回

```python
{
    "composition": "Perovskite_CsPbI3",
    "predictions": {
        "band_gap": 1.45,
        "conductivity": "2.34e-3 S/m",
        "stability": 0.872
    },
    "quantum_confidence": 0.915
}
```

MaterialScienceTools

材料科学专用工具集。

静态方法

quantum_crystal_analysis(composition, target_properties)

量子增强晶体结构分析。

plot_material_properties(results)

绘制材料性质可视化图表。

PharmaResearchTools

药物研发专用工具集。

静态方法

quantum_docking_screen(target_pdb, compound_library, top_k=5)

量子增强分子对接筛选。

admet_prediction(compound_data)

ADMET性质预测。

使用示例

基础材料筛选

```python
from abn_qss_demo import QuantumResearchPlatform

platform = QuantumResearchPlatform(domain="materials")
results = platform.demo_material_screening({
    "band_gap": (1.0, 2.0),
    "stability": "high"
})
```

药物发现流程

```python
from abn_qss_demo import PharmaResearchTools

tools = PharmaResearchTools()
docking_results = tools.quantum_docking_screen(
    target_pdb="7T9L",
    compound_library="ZINC20_Fragment",
    top_k=3
)
```

错误处理

所有API方法都包含适当的错误处理，会返回结构化的错误信息：

```python
try:
    results = platform.demo_material_screening(properties)
except Exception as e:
    print(f"计算错误: {e}")
```

性能提示

1. 批量处理: 对于大量计算，建议使用批量接口
2. 缓存利用: 重复计算会自动使用缓存结果
3. 资源监控: 大型计算建议监控内存使用

---

此API参考适用于公开演示版本，完整功能请参考合作版本文档。
