---
title: Research
nav:
  order: 1
  tooltip: Research projects and software
---

{%
  include feature.html
  image="images/research/ai-for-statistics.jpg"
  title="AI for Statistics"
  text="We investigate how statistical principles can enhance the reliability and interpretability of large language models, and conversely, how LLMs can be leveraged to advance statistical methodology. Our work includes developing benchmark datasets to evaluate and improve the statistical reasoning capabilities of LLMs ([StatEval](https://stateval.github.io/)) and designing agentic systems for automated statistical reasoning ([StatProver](https://statprover.com/))."
%}

{% include section.html %}

{%
  include feature.html
  image="images/research/rl-methodology-theory.jpg"
  title="Methodology and Theory of Reinforcement Learning"
  text="We develop rigorous methodological and theoretical foundations for reinforcement learning, focusing on distributional RL, off-policy evaluation, robustness under distribution shift, and sample-efficient learning. Our representative works include the design and analysis of quantile-based distributional reinforcement learning ([NeurIPS 2020](/assets/publications/NeurIPS-2020.pdf); [IJCAI 2021](/assets/publications/IJCAI21.pdf); [IEEE TNNLS 2024](/assets/publications/Monotonic_Quantile_Network_for_Worst-Case_Offline_Reinforcement_Learning.pdf); [ICML 2023](/assets/publications/ICML2023a.pdf)), theoretical studies of reinforcement learning in both online and offline settings ([JASA 2026](/assets/publications/JASA2026.pdf); [JASA 2024](/assets/publications/JASA2024.pdf); [JMLR 2023](/assets/publications/JMLR2023.pdf)) and off-policy evaluation in confounded environments ([NeurIPS 2024](/assets/publications/NIPS2024.pdf), [NeurIPS 2025](/assets/publications/NIPS2025.pdf))"
%}

{% include section.html %}

{%
  include feature.html
  image="images/research/two-sided-market.jpg"
  title="Two-Sided Market and Spatio-temporal System"
  text="We apply advanced machine learning methods to optimize complex real-world dynamic two-sided platforms. By integrating statistics, optimization, and reinforcement learning, we address challenges in ride-sharing equilibrium, recommendation systems, and spatio-temporal forecasting. Our representative work includes quantifying supply–demand equilibrium ([JASA 2021](/assets/publications/JASA2021.pdf)), spatio-temporal prediction and policy optimization ([JCGS 2026](/assets/publications/JCGS接收.pdf), [ICDM 2021](/assets/publications/ICDM2021.pdf)), and constrained policy optimization for recommendation systems ([KDD 2022](/assets/publications/MDP2Forest.pdf))."
%}

{% include section.html %}

{%
  include feature.html
  image="images/research/uncertainty-quantification.jpg"
  title="Uncertainty Quantification"
  text="Reliable off-policy evaluation (OPE) and uncertainty estimation are central to data-driven sequential decision-making. We tackle OPE under unmeasured confounding. Our two-way deconfounder models both observed and unobserved confounders using a neural tensor network, enabling consistent policy value estimation ([Two-way Deconfounder, NeurIPS 2024](/assets/publications/NIPS2024.pdf)). We further establish the first finite-sample error bounds for OPE in confounded POMDPs, showing that the error rate scales as O(T/√n) under mild conditions, and characterize the exponential error blow-up when using history-based proxies to infer hidden states ([Breaking the Order Barrier, NeurIPS 2025](/assets/publications/NIPS2025.pdf)). For value enhancement under offline RL, we propose a method that guarantees the output policy is no worse — and often better — than the initial policy, with theoretical convergence rates ([Value Enhancement, JASA 2024](/assets/publications/JASA2024.pdf)). Finally, we study optimal treatment allocation in online experiments, proposing three allocation strategies that minimize variance of treatment effect estimators in both non-Markov and Markov decision processes, with theoretical optimality guarantees ([Optimal Treatment Allocation, NeurIPS 2023](/assets/publications/NeurIPS2023b.pdf))."
%}

{% include section.html %}

{%
  include feature.html
  image="images/research/graph-network-analysis.jpg"
  title="Graph Representation Learning"
  text="Graph-structured data is ubiquitous in modern machine learning, and we develop novel statistical methods tailored to its unique challenges. Standard graph neural networks suffer when anisotropic structures are present, as isotropic noise in the forward diffusion process dilutes directional signals. We introduce directional diffusion models that use anisotropic, data-dependent noise in the forward process, preserving semantically meaningful graph representations. Extensive experiments on 12 datasets establish clear superiority over state-of-the-art baselines ([Directional Diffusion Models, NeurIPS 2023](/assets/publications/NeurIPS2023a.pdf)). Traditional semi-supervised learning on graphs assumes randomly sampled labeled nodes, which is violated in practice with nonignorable missing data. We propose GNM (Graph-based joint model with Nonignorable Missingness), which jointly models the graph structure and the missingness mechanism, achieving up to 7.5% improvement over baselines on the Cora dataset ([NeurIPS 2019](/assets/publications/NeurIPS-2019.pdf))."
%}
