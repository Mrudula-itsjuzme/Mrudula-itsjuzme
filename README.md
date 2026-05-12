<div align="center">

```
;-.  ,--. ,-.   ,.  .   ,  ,.  ,    ,    .  .
|  ) |    |  \ /  \ |\ /| /  \ |    |    |  |
|-'  |-   |  | |--| | V | |--| |    |    |  |
|    |    |  / |  | |   | |  | |    |    |  |
'    `--' `-'  '  ' '   ' '  ' `--' `--' `--`

 ,-.   ,.  ,          .   , ,-.  .  . ,-.  .  . ,     ,.
(   ` /  \ |          |\ /| |  ) |  | |  \ |  | |    /   `-.  |--| |          | V | |-<  |  | |  | |  | |    |--|
.   ) |  | |          |   | |  \ |  | |  / |  | |    |  |
 `-'  '  ' `--'       '   ' '  ' `--` `-'  `--` `--' '  '
```

</div>

<div align="center">

`AI Engineer` &nbsp;·&nbsp; `NLP` &nbsp;·&nbsp; `Computer Vision` &nbsp;·&nbsp; `Cybersecurity` &nbsp;·&nbsp; `Signal Processing`

B.Tech CSE (AI) — Amrita Vishwa Vidyapeetham &nbsp;·&nbsp; 2024–2028 &nbsp;·&nbsp; CGPA **8.33**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/sai-mrudula-pedamallu-1b44a3345)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mrudulasankar2007@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Mrudula-itsjuzme)
[![Status](https://img.shields.io/badge/Open_to-Internships_%26_Research-22c55e?style=flat-square)](mailto:mrudulasankar2007@gmail.com)

</div>

---

## `whoami`

I'm a CSE (AI) undergraduate at Amrita Vishwa Vidyapeetham, building systems that actually work — not just notebooks that run once.

My work spans **computer vision**, **NLP/speech**, **cybersecurity analytics**, and **signal processing**, with a hard preference for things you can measure: latency, accuracy, recall, error rates, and real-time performance.

I have a **first-author IEEE Access publication**, a dual-camera motion capture system running at **25–30 FPS**, and a spoken language intelligence platform built around real-time NLP feedback.

Currently looking for: **AI/ML internships, research collaborations, and teams building practical AI systems**.

---

## `./projects --proof-required`

### `[01]` Smart Grid Intrusion Detection &nbsp;·&nbsp; *IEEE Access (First Author)*

> Privacy-aware IDS for IEC 60870-5-104 SCADA networks — the protocol running real power grids.

```
Accuracy  ████████████████████  99.29%
Recall    ███████████████████░  94.80%
FPR       ▒░░░░░░░░░░░░░░░░░░░   4.10%   ← low is good
```

**Stack:** `Python` `XGBoost` `LightGBM` `SHAP` `RFE` `PCA` `Wireshark`

Hybrid anomaly-detection + classification pipeline with SHAP-driven feature selection on SCADA traffic. Generalizes to unseen attack patterns. Also published in **Energy Conversion & Management**.

[![Repo](https://img.shields.io/badge/→_Repository-181717?style=flat-square&logo=github)](https://github.com/Mrudula-itsjuzme/cyberattack-on-smart-grids)

---

### `[02]` Real-Time Markerless Multimodal Motion Capture

> Dual-camera 3D motion capture. No suit. No markers. Runs live.

```
Throughput          25–30 FPS
3D Accuracy         ±1–2 cm
GPU Triangulation      5 ms / frame
Stream Latency      < 100 ms      via ZMQ
Reprojection Error  < 1 px        ArUco calibration
```

**Stack:** `MediaPipe` `PyTorch` `OpenCV` `ZMQ` `ArUco` `SQLite`

8-stage pipeline: raw frames → 33-point 3D pose → joint kinematics → biomechanical features. Adaptive 1-Euro filtering. SQLite output for longitudinal analysis.

[![Repo](https://img.shields.io/badge/→_Repository-181717?style=flat-square&logo=github)](https://github.com/Mrudula-itsjuzme/Motion-capture)

---

### `[03]` MisSpoke — Real-Time Spoken Language Intelligence

> Feedback on your speech *while you're talking.* Not after.

**Stack:** `Speech Processing` `NLP` `Streaming Pipeline` `Agora`

Streaming NLP pipeline for continuous transcription — fluency scoring, filler-word detection, confidence analysis. Contextual suggestions on pacing, clarity, and articulation with no batch delay.

> 📎 Repository currently private / coming soon

---

### `[04]` EEG Signal Reconstruction via Graph Learning (ADMM)

> Recovering neural signals under 10–90% missing data.

```
RMSE Reduction   65%      (1.0 → 0.35)
Max SNR          9.34 dB
Missing Data     10%–90% handled
```

**Stack:** `Python` `NumPy` `SciPy` `Graph Signal Processing` `ADMM`

EEG reconstruction as a graph-regularized optimization problem. ADMM solver. Graph smoothness priors model inter-channel relationships for stable recovery across corrupted EEG channels.

[![Repo](https://img.shields.io/badge/→_Repository-181717?style=flat-square&logo=github)](https://github.com/Mrudula-itsjuzme/MFC3_D3_EEG_Recon_ADMM)

---

### `[05]` Cancer Driver Gene Classification

> ML pipeline for classifying oncogenic driver genes from genomic data.

**Stack:** `Python` `XGBoost` `LightGBM` `Scikit-learn` `Pandas`

[![Repo](https://img.shields.io/badge/→_Repository-181717?style=flat-square&logo=github)](https://github.com/Mrudula-itsjuzme/cancer-driver-gene-classification-ml)

---

### `[06]` Tic-Tac-Toe — Double DQN Agent &nbsp;·&nbsp; Solar Panel Fault Detection &nbsp;·&nbsp; AI Greenhouse

> RL agent with experience replay + target network. Applied ML for energy fault detection and agri automation.

**Stack:** `PyTorch` `TensorFlow` `OpenCV` `IoT` `Reinforcement Learning`

[![DQN](https://img.shields.io/badge/→_DQN_Agent-181717?style=flat-square&logo=github)](https://github.com/Mrudula-itsjuzme/tic-tac-toe-double-dqn)
[![Solar](https://img.shields.io/badge/→_Solar_Faults-181717?style=flat-square&logo=github)](https://github.com/Mrudula-itsjuzme/solarpanel-fault-detection)
[![Greenhouse](https://img.shields.io/badge/→_AI_Greenhouse-181717?style=flat-square&logo=github)](https://github.com/Mrudula-itsjuzme/ai_greenhouse)

---

## `./stack`

| Domain | Tools |
|---|---|
| **Languages** | Python · JavaScript · C++ · C · SQL |
| **ML / DL** | PyTorch · TensorFlow · XGBoost · LightGBM · Scikit-learn |
| **Vision & Signal** | OpenCV · MediaPipe · NumPy · SciPy |
| **NLP / GenAI** | LangChain · Rasa · Prompt Engineering |
| **Infra & Tools** | Flask · React · Docker · Supabase · Git · Linux · Wireshark · ZMQ |

---

## `./experience`

**AI Chatbots Intern — Academy of Robotics Pvt. Ltd.** &nbsp;`Jul–Sep 2024`

Built Rasa-based conversational agents: intent classification, entity recognition, dialogue flows, prompt-engineered interaction design. Shipped working chatbots, not prototypes.

---

## `./record`

| | |
|---|---|
| 📄 **IEEE Access** | First-author · Smart Grid Privacy-Aware IDS |
| 📄 **Energy Conversion & Management** | Co-author publication |
| 🏆 **GDG Agora Hackathon** | 4th Place |
| 🚀 **NASA Space Settlement Contest 2022** | Literary Merit · 2nd Prize |
| 📖 **Co-author** | *XX: Story from Foetus to Foeticide* · ISBN 978-93-5605-245-1 |
| 🎓 **Init Club** | Co-founder & VP · Amrita Vishwa Vidyapeetham |
| 🎓 **IETE · NSS · Poetree** | Active member · Class Representative |

---

## `./github --stats`

<div align="center">

<img height="175em" src="https://github-readme-stats.vercel.app/api?username=Mrudula-itsjuzme&show_icons=true&hide_border=true&bg_color=0d1117&title_color=00d9ff&text_color=c9d1d9&icon_color=00d9ff&include_all_commits=true&count_private=true&rank_icon=github&custom_title=Activity" />
&nbsp;
<img height="175em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Mrudula-itsjuzme&layout=donut&hide_border=true&bg_color=0d1117&title_color=00d9ff&text_color=c9d1d9&langs_count=6&custom_title=Languages" />

<br/><br/>

<img src="https://streak-stats.demolab.com?user=Mrudula-itsjuzme&hide_border=true&background=0d1117&stroke=00d9ff&ring=00d9ff&fire=ff6b6b&currStreakLabel=00d9ff&sideNums=c9d1d9&currStreakNum=ffffff&dates=8b949e&sideLabels=8b949e&card_width=600" />

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mrudula-itsjuzme/Mrudula-itsjuzme/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mrudula-itsjuzme/Mrudula-itsjuzme/output/github-contribution-grid-snake.svg" />
  <img alt="contribution snake" src="https://raw.githubusercontent.com/Mrudula-itsjuzme/Mrudula-itsjuzme/output/github-contribution-grid-snake-dark.svg" />
</picture>

<sub>↑ contribution snake — enable via <a href="https://github.com/Platane/snk">Platane/snk</a> GitHub Action in your profile repo</sub>

</div>

---

<div align="center">

`builds real systems` &nbsp;·&nbsp; `measures everything` &nbsp;·&nbsp; `open to research & internships`

[![Email](https://img.shields.io/badge/mrudulasankar2007%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mrudulasankar2007@gmail.com)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/Pedamallu_Sai_Mrudula-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/sai-mrudula-pedamallu-1b44a3345)

</div>
