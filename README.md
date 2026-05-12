<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020817,30:0a1628,60:0d2137,100:00d9ff&height=280&section=header&text=Pedamallu%20Sai%20Mrudula&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=42&desc=CSE%20(AI)%20%E2%80%94%20NLP%20%C2%B7%20Computer%20Vision%20%C2%B7%20Cybersecurity%20%C2%B7%20Signal%20Processing&descAlignY=60&descSize=15&descColor=7dd3fc" />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=16&duration=2600&pause=900&color=00D9FF&center=true&vCenter=true&width=700&lines=First-author+%E2%86%92+IEEE+Access+%7C+Smart+Grid+IDS;Real-time+3D+motion+capture+%40+25%E2%80%9330+FPS+%C2%B7+%C2%B11%E2%80%932cm;99.29%25+accuracy+%C2%B7+94.8%25+recall+on+unseen+attacks;EEG+reconstruction+%C2%B7+65%25+RMSE+reduction;Building+systems+that+actually+work." />

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sai-mrudula-pedamallu-1b44a3345)
[![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mrudulasankar2007@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mrudula-itsjuzme)
[![Open to Work](https://img.shields.io/badge/Open%20to-Internships%20%26%20Research-22c55e?style=for-the-badge)](mailto:mrudulasankar2007@gmail.com)

![](https://komarev.com/ghpvc/?username=Mrudula-itsjuzme&style=flat-square&color=00d9ff&label=profile+views)

<br/>

<!-- NAV BAR -->
[`⚡ whoami`](#-whoami) · [`🔬 projects`](#-projects--proof-required) · [`🛠️ stack`](#%EF%B8%8F-stack) · [`📌 pinned`](#-pinned-repos) · [`📊 stats`](#-github--stats) · [`🏆 record`](#-record)

</div>

---

## ⚡ whoami

```python
class SaiMrudula:
    institution = "Amrita Vishwa Vidyapeetham · B.Tech CSE (AI) · 2024–2028"
    cgpa        = 8.33
    location    = "Visakhapatnam, India"
    domains     = ["Computer Vision", "NLP / Speech", "Cybersecurity Analytics", "Signal Processing"]
    pub         = "IEEE Access — first author · Energy Conversion & Management — co-author"
    looking_for = ["AI/ML internships", "research collaborations", "teams building real systems"]

    def build(self):
        return "Measurable systems. Not polished screenshots."
```

> I have a **first-author IEEE Access publication**, a dual-camera motion capture system at **25–30 FPS**, a spoken language intelligence platform with real-time NLP feedback, and an IDS pipeline at **99.29% accuracy** — all built from scratch.

---

## 🔬 projects · proof required

<details open>
<summary>&nbsp;<b>🔒 [01] Smart Grid Intrusion Detection &nbsp;·&nbsp; <i>IEEE Access — First Author</i></b></summary>
<br/>

> Privacy-aware IDS for **IEC 60870-5-104 SCADA** networks — the protocol running real power grids.

```diff
+ Accuracy   ████████████████████  99.29%
+ Recall     ███████████████████░  94.80%
- FPR        ▒░░░░░░░░░░░░░░░░░░░   4.10%   ← low is good
```

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=flat-square&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-02569B?style=flat-square&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white)
`SHAP` `RFE` `PCA`

Hybrid anomaly-detection + classification pipeline with SHAP-driven feature selection on SCADA traffic. Generalizes to unseen attack patterns. Also published in **Energy Conversion & Management**.

[![View Repo](https://img.shields.io/badge/→%20Repository-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mrudula-itsjuzme/cyberattack-on-smart-grids)

</details>

<details open>
<summary>&nbsp;<b>🎥 [02] Real-Time Markerless Multimodal Motion Capture</b></summary>
<br/>

> Dual-camera 3D motion capture. No suit. No markers. **Runs live.**

```yaml
throughput:         25–30 FPS
accuracy_3d:        ±1–2 cm
gpu_triangulation:  5 ms / frame
stream_latency:     < 100 ms     # ZMQ
reprojection_error: < 1 px       # ArUco calibration
pipeline_stages:    8            # frames → biomechanical features
```

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=flat-square&logo=google&logoColor=white)
`ZMQ` `ArUco` `SQLite` `1-Euro Filter`

8-stage pipeline: raw frames → 33-point 3D pose → joint kinematics → biomechanical feature extraction. Adaptive filtering + structured SQLite storage for longitudinal analysis.

[![View Repo](https://img.shields.io/badge/→%20Repository-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mrudula-itsjuzme/Motion-capture)

</details>

<details open>
<summary>&nbsp;<b>🎙️ [03] MisSpoke — Real-Time Spoken Language Intelligence</b></summary>
<br/>

> Feedback on your speech *while you're talking.* Not after.

![Agora](https://img.shields.io/badge/Agora-099DFD?style=flat-square&logoColor=white)
`Speech Processing` `NLP` `Streaming Pipeline`

Streaming NLP pipeline for continuous transcription — fluency scoring, filler-word detection, confidence analysis. Contextual suggestions on pacing, clarity, articulation. No batch delay.

> 🔒 Repository currently private — coming soon

</details>

<details open>
<summary>&nbsp;<b>🧠 [04] EEG Signal Reconstruction via Graph Learning (ADMM)</b></summary>
<br/>

> Recovering neural signals under 10–90% missing data.

```diff
+ RMSE Reduction   65%      (1.0 → 0.35)
+ Max SNR          9.34 dB
+ Missing Data     10%–90% handled
```

![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)
`Graph Signal Processing` `ADMM`

EEG as a graph-regularized optimization problem. ADMM solver with smoothness priors modeling inter-channel relationships for stable neural signal recovery across highly corrupted channels.

[![View Repo](https://img.shields.io/badge/→%20Repository-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mrudula-itsjuzme/MFC3_D3_EEG_Recon_ADMM)

</details>

<details>
<summary>&nbsp;<b>🧬 [05] Cancer Driver Gene Classification</b></summary>
<br/>

> ML pipeline for classifying oncogenic driver genes from genomic data.

![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=flat-square&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
`LightGBM` `Scikit-learn`

[![View Repo](https://img.shields.io/badge/→%20Repository-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mrudula-itsjuzme/cancer-driver-gene-classification-ml)

</details>

<details>
<summary>&nbsp;<b>🎮 [06] Double DQN · Solar Fault Detection · AI Greenhouse</b></summary>
<br/>

> RL agent with experience replay + target network. Applied ML for energy fault detection and agri automation.

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
`IoT` `Reinforcement Learning`

[![DQN](https://img.shields.io/badge/→%20DQN%20Agent-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mrudula-itsjuzme/tic-tac-toe-double-dqn)
[![Solar](https://img.shields.io/badge/→%20Solar%20Faults-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mrudula-itsjuzme/solarpanel-fault-detection)
[![Greenhouse](https://img.shields.io/badge/→%20AI%20Greenhouse-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mrudula-itsjuzme/ai_greenhouse)

</details>

---

## 🛠️ stack

<div align="center">

**Languages**<br/>
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

**ML / DL / Vision**<br/>
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=for-the-badge&logo=google&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

**NLP / GenAI**<br/>
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Rasa](https://img.shields.io/badge/Rasa-5A17EE?style=for-the-badge&logoColor=white)

**Infra**<br/>
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)

</div>

---

## 📌 pinned repos

<div align="center">

[![smart-grid](https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=Mrudula-itsjuzme&repo=cyberattack-on-smart-grids&bg_color=0d1117&title_color=00d9ff&text_color=c9d1d9&icon_color=00d9ff&border_color=21262d)](https://github.com/Mrudula-itsjuzme/cyberattack-on-smart-grids)
[![motion-capture](https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=Mrudula-itsjuzme&repo=Motion-capture&bg_color=0d1117&title_color=00d9ff&text_color=c9d1d9&icon_color=00d9ff&border_color=21262d)](https://github.com/Mrudula-itsjuzme/Motion-capture)

[![eeg-recon](https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=Mrudula-itsjuzme&repo=MFC3_D3_EEG_Recon_ADMM&bg_color=0d1117&title_color=00d9ff&text_color=c9d1d9&icon_color=00d9ff&border_color=21262d)](https://github.com/Mrudula-itsjuzme/MFC3_D3_EEG_Recon_ADMM)
[![cancer-genes](https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=Mrudula-itsjuzme&repo=cancer-driver-gene-classification-ml&bg_color=0d1117&title_color=00d9ff&text_color=c9d1d9&icon_color=00d9ff&border_color=21262d)](https://github.com/Mrudula-itsjuzme/cancer-driver-gene-classification-ml)

[![dqn](https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=Mrudula-itsjuzme&repo=tic-tac-toe-double-dqn&bg_color=0d1117&title_color=00d9ff&text_color=c9d1d9&icon_color=00d9ff&border_color=21262d)](https://github.com/Mrudula-itsjuzme/tic-tac-toe-double-dqn)
[![solar](https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=Mrudula-itsjuzme&repo=solarpanel-fault-detection&bg_color=0d1117&title_color=00d9ff&text_color=c9d1d9&icon_color=00d9ff&border_color=21262d)](https://github.com/Mrudula-itsjuzme/solarpanel-fault-detection)

</div>

---

## 📊 github · stats

<div align="center">

<img src="https://streak-stats.demolab.com?user=Mrudula-itsjuzme&hide_border=true&background=0d1117&stroke=21262d&ring=00d9ff&fire=ff6b6b&currStreakLabel=00d9ff&sideNums=ffffff&currStreakNum=ffffff&dates=8b949e&sideLabels=8b949e&card_width=650" />

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mrudula-itsjuzme/Mrudula-itsjuzme/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mrudula-itsjuzme/Mrudula-itsjuzme/output/github-contribution-grid-snake.svg" />
  <img alt="contribution snake" src="https://raw.githubusercontent.com/Mrudula-itsjuzme/Mrudula-itsjuzme/output/github-contribution-grid-snake-dark.svg" />
</picture>

</div>

---

## 🏆 record

<div align="center">

| | |
|:---:|:---|
| 📄 | **IEEE Access** — First-author · Smart Grid Privacy-Aware IDS |
| 📄 | **Energy Conversion & Management** — Co-author publication |
| 🏆 | **GDG Agora Hackathon** — 4th Place |
| 🚀 | **NASA Space Settlement Contest 2022** — Literary Merit · 2nd Prize |
| 📖 | **Co-author** — *XX: Story from Foetus to Foeticide* · ISBN 978-93-5605-245-1 |
| 🎓 | **Init Club** — Co-founder & VP · Amrita Vishwa Vidyapeetham |
| 🎓 | **IETE · NSS · Poetree** — Active member · Class Representative |

</div>

---

## 💼 experience

```
┌──────────────────────────────────────────────────────────────┐
│  AI Chatbots Intern  ·  Academy of Robotics Pvt. Ltd.        │
│  Visakhapatnam, India  ·  Jul 2024 – Sep 2024                │
├──────────────────────────────────────────────────────────────┤
│  → Built Rasa conversational agents from scratch             │
│  → Intent classification · entity recognition · NLU         │
│  → Prompt-engineered dialogue flows & interactions           │
│  → Shipped working chatbots, not prototypes                  │
└──────────────────────────────────────────────────────────────┘
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00d9ff,50:0a2a4a,100:020817&height=130&section=footer&text=builds%20real%20systems%20%C2%B7%20measures%20everything%20%C2%B7%20open%20to%20research&fontSize=13&fontColor=7dd3fc&fontAlignY=65&animation=fadeIn" />

</div>
