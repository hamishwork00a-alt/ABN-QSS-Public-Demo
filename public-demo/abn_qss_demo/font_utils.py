"""
字体配置工具 - 解决Matplotlib中文显示问题
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os

def setup_chinese_font():
    """
    配置Matplotlib中文字体支持
    自动检测系统并设置合适的中文字体
    """
    # 获取系统类型
    system = platform.system()
    
    # 不同系统的中文字体路径
    font_paths = {
        'Windows': [
            'C:/Windows/Fonts/simhei.ttf',  # 黑体
            'C:/Windows/Fonts/simkai.ttf',  # 楷体
            'C:/Windows/Fonts/simsun.ttc',  # 宋体
        ],
        'Darwin': [  # macOS
            '/System/Library/Fonts/PingFang.ttc',
            '/System/Library/Fonts/STHeiti Light.ttc',
            '/System/Library/Fonts/STHeiti Medium.ttc',
        ],
        'Linux': [
            '/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',
            '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
        ]
    }
    
    # 尝试找到可用的中文字体
    available_font = None
    for font_path in font_paths.get(system, []):
        if os.path.exists(font_path):
            available_font = font_path
            break
    
    if available_font:
        # 设置字体
        chinese_font = fm.FontProperties(fname=available_font)
        plt.rcParams['font.family'] = chinese_font.get_name()
        plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
        
        print(f"✅ 中文字体设置成功: {available_font}")
        return True
    else:
        # 如果没有找到系统字体，使用Matplotlib的默认设置
        plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial Unicode MS', 'SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        print("⚠️  使用备用字体配置，中文显示可能不完美")
        return False

def safe_plot_with_chinese(title, xlabel, ylabel, plot_function, **kwargs):
    """
    安全绘图函数 - 自动处理中文显示
    """
    # 设置中文字体
    setup_chinese_font()
    
    # 创建图形
    plt.figure(figsize=kwargs.get('figsize', (10, 6)))
    
    # 执行绘图函数
    plot_function()
    
    # 设置中文标题和标签
    plt.title(title, fontsize=kwargs.get('title_size', 14))
    plt.xlabel(xlabel, fontsize=kwargs.get('label_size', 12))
    plt.ylabel(ylabel, fontsize=kwargs.get('label_size', 12))
    
    # 其他可选设置
    if kwargs.get('grid', True):
        plt.grid(True, alpha=0.3)
    
    if kwargs.get('tight_layout', True):
        plt.tight_layout()
    
    plt.show()

# 初始化字体配置
setup_chinese_font()
