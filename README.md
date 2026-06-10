##  CRM 接口测试（Postman + Newman + Python 脚本）
- 这是前后端分离的CRM客户管理系统，核心模块为合同管理和课程管理，迭代频繁，手工回归耗时长。
- 使用 Postman+Newman 完成接口测试，并基于 Python+requests 对核心接口进行脚本验证；同时同步完成 Jenkins+Newman 持续集成落地方案规划（仅输出流程图，受本地环境限制未部署服务），用于长期优化回归效率。

## 技术栈
- 工具级：Postman、Newman、htmlextra
- 代码级：Python、requests、pytest、pytest-html
- 持续集成：Jenkins（方案设计）

## 项目内容
1. 梳理合同、课程管理接口业务流程，设计 **15+ 条接口用例**（增删改查全场景）。
2. 使用环境变量管理多套配置（base_url、token），实现多环境快速切换。
3. 通过 Tests 脚本自动提取登录 token 并完成接口关联，对状态码、业务码、关键字段进行多维度断言。
4. 集成 Newman 命令行执行测试，生成 HTML 报告（包含通过率、失败详情、耗时），核心业务通过率 **100%**，单流程 **8 秒**（手工需 5 分钟）。
5. 使用 Python + requests + pytest 重写核心接口（登录、课程管理），生成 HTML 报告，通过率 **100%**。
6. 调研持续集成流程，输出 Jenkins+Newman CI 流水线流程图（存放于 docs 文件夹），梳理「代码拉取→Newman 执行用例→生成报告→异常邮件推送」全套配置步骤，为项目后续自动化迭代提供可落地规划。

## 运行步骤
Postman 自动化：导入 collection 与环境变量，Newman 命令行批量执行生成报告；

Python 脚本：安装 requests/pytest/pytest-html 依赖，运行 test_core_api.py 生成可视化报告；

CI 方案：仅完成流程规划，梳理完整 Jenkins 插件、任务配置步骤。


## 技术亮点
- **接口关联**：自动提取登录 token 并传递给后续接口
- **多维度断言**：校验 HTTP 状态码、业务状态码、关键字段存在性
- **环境切换**：环境变量管理多套配置
- **代码级实现**：使用 Python + requests + pytest 对登录、课程管理等核心接口进行脚本验证，实现参数化断言并生成 HTML 报告。
- **CI 设计**：提供可落地的持续集成方案
