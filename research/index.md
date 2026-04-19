---
title: Research
nav:
  order: 1
  tooltip: Research projects and software
---

# {% include icon.html icon="fa-solid fa-wrench" %}Research

Our research spans the intersection of statistical theory, machine learning, and large language models,
with a focus on developing principled methods for robust decision-making, interpretability,
and uncertainty quantification in AI systems.

{% include section.html %}

{%
  include feature.html
  image="images/research/ai-for-statistics.jpg"
  title="AI for Statistics"
%}

We investigate how statistical principles can enhance the reliability and interpretability of large language models, and conversely, how LLMs can be leveraged to improve statistical analysis. Our work spans LLM security and robustness ([Breach in the Shield, EACL 2026](/assets/publications/2026.eacl-long.161.pdf)) and AI-augmented statistical prediction ([Enhancing Prediction Performance through Influence Measure, ICLR 2025](/assets/publications/ICLR2025.pdf)).

{% include section.html %}

{%
  include feature.html
  image="images/research/rl-methodology-theory.jpg"
  title="Methodology and Theory of Reinforcement Learning"
%}

We develop rigorous methodological and theoretical foundations for reinforcement learning, with a focus on off-policy evaluation, robust RL under distribution shift, and sample-efficient learning. Representative works include variance control and adversarial learning for distributional RL ([Variance Control, ICML 2023](/assets/publications/ICML2023a.pdf); [Adversarial Learning of DRL, ICML 2023](/assets/publications/ICML2023b.pdf)), quantile-based exploration ([Non-decreasing Quantile Function Network, IJCAI 2021](/assets/publications/IJCAI21.pdf); [Monotonic Quantile Network, IEEE TNNLS 2024](/assets/publications/Monotonic_Quantile_Network_for_Worst-Case_Offline_Reinforcement_Learning.pdf)), and non-crossing quantile regression for deep RL ([NeurIPS 2020](/assets/publications/NeurIPS-2020.pdf)).

{% include section.html %}

{%
  include feature.html
  image="images/research/two-sided-market.jpg"
  title="Two-Sided Market & Platform Optimization"
%}

We study machine learning and statistical methods for two-sided markets, including ride-sharing platforms and recommendation systems. Work includes equilibrium analysis for supply-demand systems ([Graph-Based Equilibrium Metrics, JASA 2021](/assets/publications/JASA2021.pdf)), spatio-temporal OD matrix prediction ([JCGS 2026](/assets/publications/JCGS接收.pdf)), and constrained policy optimization for recommendation ([MDP2 Forest, KDD 2022](/assets/publications/MDP2Forest.pdf)).

{% include section.html %}

{%
  include feature.html
  image="images/research/uncertainty-quantification.jpg"
  title="Off-Policy Evaluation & Uncertainty Quantification"
%}

Reliable uncertainty estimation and off-policy evaluation are central to data-driven decision-making. We develop methods for off-policy evaluation in confounded environments ([Two-way Deconfounder, NeurIPS 2024](/assets/publications/NIPS2024.pdf); [Breaking the Order Barrier, NeurIPS 2025](/assets/publications/NIPS2025.pdf)), robust trust region optimization ([Value Enhancement, JASA 2024](/assets/publications/JASA2024.pdf)), deep nonparametric regression for dependent data ([JMLR 2023](/assets/publications/JMLR2023.pdf)), and optimal treatment allocation in sequential decisions ([NeurIPS 2023](/assets/publications/NeurIPS2023b.pdf)).

{% include section.html %}

{%
  include feature.html
  image="images/research/graph-network-analysis.jpg"
  title="Graph Representation Learning"
%}

Graph-structured data is ubiquitous in modern machine learning. We develop statistical methods for graph analysis, including diffusion-based graph representation learning ([Directional Diffusion Models, NeurIPS 2023](/assets/publications/NeurIPS2023a.pdf)) and graph-based semi-supervised learning with nonignorable nonresponses ([NeurIPS 2019](/assets/publications/NeurIPS-2019.pdf)).

{% include section.html %}

## Softwares, Packages and More

{%
  include feature.html
  image="images/research/statprover.jpg"
  title="StatProver — Agentic Statistical Proof Assistant"
%}

We are glad to introduce **[StatProver](https://statprover.com)**, a brand new agentic statistical proving system. StatProver helps users clarify the problem, find references, outline skeleton steps, and write the proof. Learn more at **[https://statprover.com](https://statprover.com)**

We have also developed benchmark datasets for evaluating the statistical reasoning capabilities of large language models:

- **[StatEval-Foundational-Knowledge](https://huggingface.co/datasets/0v01111/StatEval-Foundational-knowledge)** — Foundational statistical knowledge evaluation benchmark
- **[StatEval-Statistical-Research](https://huggingface.co/datasets/0v01111/StatEval-Statistical-Research)** — Statistical research capabilities evaluation benchmark
- **[StatEval Website](https://stateval.github.io/)** — Official benchmark evaluation platform
