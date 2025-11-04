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

测试要求

· 新功能必须包含测试用例
· 确保测试覆盖率不降低
· 所有测试必须在Python 3.8+环境下通过

📝 Pull Request 流程

1. 确保更改目标正确: 针对 develop 分支
2. 添加测试: 新功能必须包含测试用例
3. 更新文档: 相应更新README和API文档
4. 通过CI: 确保所有GitHub Actions检查通过
5. 代码审查: 等待维护者审查和反馈

🎨 项目结构

```text
public-demo/
├── abn_qss_demo/     # 核心演示代码
├── tests/            # 测试用例
├── docs/             # 文档
└── examples/         # 使用示例
```

🔬 研究合作

如果您是科研人员并希望：

· 在特定领域应用ABN-QSS
· 合作发表研究成果
· 获得完整版本访问权限

请联系: research@abn-qss.com

📄 许可证

通过贡献代码，您同意您的贡献将在MIT许可证下发布。

💬 沟通渠道

· GitHub Issues: 技术问题和功能请求
· Email: landsingchang@gmail.com (研究合作)
· LinkedIn: ABN-QSS技术平台

---

感谢您的贡献！🎉

