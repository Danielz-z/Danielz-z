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

## 🔬 目前在做什么

我目前正在构建以人为本的具身智能体系统，整合多模态感知、状态建模、决策与动作执行。我的工作聚焦于融合 EEG、视觉以及生理或行为信号的 AI 系统，并在 ALOHA、Astribot 和 ZsiBot 等具身平台上开展机器人系统集成。

这些系统遵循闭环架构：感知 → 状态估计 → 决策 → 动作执行 → 反馈。

### 能力示例

* EEG → 意图解码 → 决策 → STM32 小车控制
* 面部情绪 → 决策 → 通过安全门控执行 Astribot 动作
* EMG 手势 → 决策 → ZsiBot 机器人控制
* 视觉 + 机器人状态 + EEG 信号 → OpenPI 策略 → ALOHA 双臂动作

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

### [EEG-BCI-Car](https://github.com/Danielz-z/EEG-BCI-Car)

* 端到端 EEG 意图识别系统
* 模型训练（LSTM / SVM 等）+ 实时控制
* 与嵌入式系统联动（STM32 + 蓝牙）
* 荣获第 13 届 Cloud Programming World Cup 一等奖

### 具身智能与机器人控制（企业项目）

演示视频：即将上线

* 融合面部表情识别、EEG 信号和 BCI 范式进行多模态人类状态感知
* 基于 DeepFace 的情绪识别原型，用于实时机器人交互 — [笔记](https://github.com/Danielz-z/ai-engineering-notes/blob/main/deepface_robot_control.md)
* 探索基于 SSVEP 的机器人控制，并使用 EEGNet 进行运动想象分类
* 闭环系统（感知 → 状态估计 → 决策 → 动作 → 反馈），通过稳定的事件触发逻辑减少噪声或不稳定的机器人动作
* 在 AgileX Aloha 平台上微调 π0.5 VLA 模型，完成双臂操作任务 — [笔记](https://github.com/Danielz-z/ai-engineering-notes/blob/main/pi05_aloha_finetune.md)
* 部署 OpenPI 策略服务，实现双臂 Piper 推理与失败恢复 — [笔记](https://github.com/Danielz-z/ai-engineering-notes/blob/main/openpi_aloha_inference_deployment.md)
* EMG 手势识别控制 ZsiBot ZSL-1W 轮腿机器人（约 40ms 延迟）— [笔记](https://github.com/Danielz-z/ai-engineering-notes/blob/main/zsibot_emg_robot_control.md)

### EAV 多模态情绪识别

* 42 被试 EEG-Audio-Video 多模态情绪识别数据集，采用防泄漏数据划分；构建了完整的单模态基线与后期融合，准确率达 0.5729

### [个人网站与 AI 基础设施](https://amorfati.cn/)

* 基于 Docker 的个人网站，使用 Caddy 反向代理和 WordPress
* 迁移至 AI 就绪的基础设施，集成 FastAPI 与未来 Agent 服务
* 笔记：[Amor Fati AI 基础设施](https://github.com/Danielz-z/ai-engineering-notes/blob/main/amorfati-ai-infra-readme.md)

<br>

## ⚙️ 技术栈

* 编程：Python、C/C++、Java、SQL、JavaScript、Shell

* AI / 机器学习：
  PyTorch、TensorFlow、scikit-learn、OpenCV、MNE、Braindecode、EEGNet、Transformer 模型、NumPy、Pandas、Matplotlib

* AI 工程工作流：
  Claude Code、OpenAI Codex

* 系统与基础设施：
  Linux、Docker、Kubernetes、Git、SSH、VSCode Remote、MySQL、Jupyter、LaTeX

* 机器人与嵌入式：
  Astribot SDK、ALOHA、OpenPI、STM32 嵌入式控制

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
  <img src="https://skillicons.dev/icons?i=anaconda,aws,bash,blender,c,cpp,docker,fastapi,flask,git,githubactions,java,js,linux,matlab,mysql,nginx,photoshop,python,pytorch,qt,r,ros,scikitlearn,tensorflow,vscode,latex,opencv,kubernetes,arduino&perline=8" />
</p>

<br>

<p align="center">
Always learning to balance.
</p>
