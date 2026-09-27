<h1 align="center">你好 👋，我是 Daniel</h1>

<p align="center">
构建以人为本的具身智能体系统
</p>

<p align="center">
EEG 与多模态感知 → 状态建模 → 决策 → 机器人动作
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="https://amorfati.cn/">🌐 个人网站</a>
</p>

<br>

## 🔬 关于我与我的工作

我目前在 UCLA 攻读人工智能方向的工程硕士，预计于 2027 年 12 月毕业，本科毕业于北京交通大学计算机科学与技术专业。我的兴趣是具身智能与机器人学习，尤其关注如何把感知和学习方法接入实际系统。

我早期的项目主要围绕 EEG 意图识别与情绪识别，做过模型训练、评估，以及预测结果与车辆控制界面的对接。在 EBkernel 实习期间，我进一步参与了 EEG 任务事件、表情识别和肌电（EMG）手势与机器人的连接，以及 ALOHA 平台上的 π0.5／OpenPI 训练和部署。目前，我在 Philo Homes 参与住宅视频的三维重建，主要做研究代码适配、相机与场景数据转换，以及输出检查。

我也持续开发个人网站、后台服务和数据库项目，积累接口、数据存储和部署方面的经验。这些工作让我接触了模型之外的数据与系统问题，也构成了我继续深入机器人学习的基础。

### 能力示例

* EEG → 意图解码 → 决策 → STM32 小车控制
* 面部情绪 → 决策 → 通过安全门控执行 Astribot 动作
* EMG 手势 → 决策 → ZsiBot 机器人控制
* EEG 任务事件 → 人工确认 → 机器人任务请求
* 图像 + 机器人状态 + 语言指令 → π0.5（通过 OpenPI）→ ALOHA 双臂动作

<br>

## 🧠 研究方向

我的研究兴趣包括跨被试 EEG 泛化、EEG / 视觉 / 语言 / 音频的多模态融合，以及超越传统 BCI 场景的行为驱动人类状态建模。此外，我也关注如何将实时 AI 部署到以人为本的具身智能体系统中。

<br>

## 📌 代表性项目

### [EEG 情绪识别（MAET 模型）](https://github.com/Danielz-z/LGF-EEG-Emotion)

* 融合多重分形、图结构与 Transformer 的模型
* 在 SEED-VII 数据集上进行跨被试泛化
* 关注鲁棒性与泛化能力
* 论文：[Local-Global Feature Fusion for Subject-Independent EEG Emotion Recognition](https://arxiv.org/abs/2601.08094)
* 获 IEEE EMBC 2026 口头报告录用

### 具身智能与机器人控制（企业项目）

演示视频：[观看实习演示](https://amorfati.cn/personal-archive/internship/)

* 融合面部表情识别、EEG 信号和 BCI 范式进行多模态人类状态感知
* 基于 DeepFace 的情绪识别原型，用于实时机器人交互 — [笔记](https://github.com/Danielz-z/ai-engineering-notes-public/blob/main/deepface_robot_control.md)
* 探索基于 SSVEP 的机器人控制，并使用 EEGNet 进行运动想象分类
* 连接 EEG 任务事件、人工确认与机器人动作，加入回调重试和日志记录，便于排查消息传递失败
* 在 AgileX Aloha 平台上微调 π0.5 VLA 模型，完成双臂操作任务 — [笔记](https://github.com/Danielz-z/ai-engineering-notes-public/blob/main/pi05_aloha_finetune.md)
* 部署 OpenPI 策略服务，实现双臂 Piper 推理与失败恢复 — [笔记](https://github.com/Danielz-z/ai-engineering-notes-public/blob/main/openpi_aloha_inference_deployment.md)
* EMG 手势识别控制 ZsiBot ZSL-1W 轮腿机器人 — [笔记](https://github.com/Danielz-z/ai-engineering-notes-public/blob/main/zsibot_emg_robot_control.md)

### EAV 多模态情绪识别

* 42 被试 EEG-Audio-Video 数据集，采用防泄漏数据划分；构建了完整的单模态基线与后期融合，准确率达 0.5729

### [EEG-BCI-Car](https://github.com/Danielz-z/EEG-BCI-Car)

* 端到端 EEG 意图识别系统
* 模型训练（LSTM / SVM 等）+ 实时控制
* 与嵌入式系统联动（STM32 + 蓝牙）
* 荣获第 13 届 Cloud Programming World Cup 一等奖

### [个人网站与 AI 基础设施](https://amorfati.cn/)

* 基于 Docker 的个人网站，使用 Caddy 反向代理和 WordPress
* 基于 FastAPI 开发私有管理助手，支持项目文档检索、服务器状态查看，以及对话和任务历史记录
* 笔记：[Amor Fati AI 基础设施](https://github.com/Danielz-z/ai-engineering-notes-public/blob/main/amorfati-ai-infra-readme.md)

<br>

## ⚙️ 技术栈

* 编程：Python、C/C++、Java、JavaScript、SQL

* 机器学习与数据：PyTorch、scikit-learn、NumPy、Pandas、OpenCV

* Web 开发与数据库：FastAPI、Flask、LangGraph、MySQL、PostgreSQL、WordPress、Three.js

* 机器人：ROS、OpenPI

* 开发工具：Linux、Git、Docker、Bash、Nginx

<br>

## 🤝 希望合作的方向

欢迎围绕多模态智能体系统、具身 AI、EEG 与视觉融合、人类状态建模、可扩展的 Agent 架构，以及智能系统的真实场景部署等方向交流合作。

<br>

## 📫 联系方式

* 邮箱：[daniel.zhengzhou@gmail.com](mailto:daniel.zhengzhou@gmail.com)
* LinkedIn：[www.linkedin.com/in/zheng-zhou-cs](https://www.linkedin.com/in/zheng-zhou-cs)

<p align="center">
  <a href="https://github.com/Danielz-z" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="GitHub" height="35" width="35" />
  </a>
  
  <a href="https://www.linkedin.com/in/zheng-zhou-cs" target="_blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="35" width="35" />
  </a>
</p>

## 🛠 语言与工具

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,c,cpp,java,js,pytorch,sklearn,opencv,fastapi,flask,mysql,postgres,ros,linux,git,docker,wordpress,bash,nginx,threejs&perline=10" alt="Python, C, C++, Java, JavaScript, PyTorch, scikit-learn, OpenCV, FastAPI, Flask, MySQL, PostgreSQL, ROS, Linux, Git, Docker, WordPress, Bash, Nginx, Three.js" />
</p>

<br>

<p align="center">
Always learning to balance.
</p>
