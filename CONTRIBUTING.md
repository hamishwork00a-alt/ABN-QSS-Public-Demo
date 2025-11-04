# ABN-QSS 贡献指南

感谢您对ABN-QSS项目的关注！我们欢迎各种形式的贡献。

## 🎯 贡献方式

### 1. 报告问题
如果您发现了bug或有功能建议，请通过[GitHub Issues](https://github.com/hamishwork00a-alt/ABN-QSS-Public-Demo/issues)报告。

### 2. 代码贡献
**开发流程**
1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

**代码规范**
- 遵循 PEP 8 Python代码风格
- 添加适当的文档字符串
- 包含单元测试
- 确保所有测试通过

### 3. 文档改进
- 修正拼写错误或语法问题
- 改进文档结构和可读性
- 添加使用示例和教程

### 4. 社区支持
- 帮助回答其他用户的问题
- 分享使用经验和案例
- 推广项目到相关社区

## 🛠️ 开发环境设置

### 本地开发
```bash
# 1. 克隆仓库
git clone https://github.com/hamishwork00a-alt/ABN-QSS-Public-Demo.git
cd ABN-QSS-Public-Demo/public-demo

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行测试
python -m pytest tests/ -v

# 4. 验证示例
python example_usage.py
