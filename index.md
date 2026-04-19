---
---

# StatAI Lab

StatAI Lab is dedicated to exploring the deep integration of large language models (LLMs) and statistics.
We focus on the applications of statistical theory in AI interpretability and uncertainty quantification,
while also investigating how AI can better empower statistical inference.

{%
  include button.html
  type="github"
  text="On GitHub"
  link="StatAI-Lab"
%}

{% include section.html %}

## Research

Our research spans several interconnected areas at the intersection of statistical theory and modern machine learning:

**Distributionally Robust Reinforcement Learning & Off-Policy Evaluation.** We develop rigorous methods for RL under distribution shift, including variance control, adversarial robustness, and off-policy evaluation in confounded MDPs. Work appears at ICML, IJCAI, NeurIPS.

**AI for Statistical Inference.** We investigate how LLMs can assist statistical reasoning — from influence-based prediction enhancement to uncertainty quantification in foundation models — and conversely, how statistical principles can improve the reliability and interpretability of LLMs.

**Two-Sided Markets & Platform Optimization.** We apply causal inference and stochastic optimization to ride-sharing platforms, matching markets, and recommendation systems, with publications in JASA and JCGS.

**Uncertainty Quantification & Nonparametric Statistics.** We develop scalable methods for uncertainty estimation in deep learning, including conformal prediction and robust graph/network analysis, with work published in JMLR and NeurIPS.

{%
  include button.html
  link="research"
  text="Learn more about our research"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% include section.html %}

## Join Our Team

**StatAI Lab** is located at **Shanghai University of Finance and Economics**.

We are always open to collaborations and inquiries from researchers and students interested in the intersection of LLMs and statistics.We welcome prospective PhD and Master's students who are passionate about research at the intersection of large language models and statistics.

### Requirements

**PhD Candidates**

- Aspiring to an academic career in the future
- Strong mathematical and statistical foundations, self-motivated, and passionate about research
- Familiar with Python and GPU computing; programming skills are a plus

**Master's Students**

- Interested in pursuing further PhD studies or working in industry roles related to algorithms and research
- Master's students will participate in systematic research training led by PhD students and may be recommended for PhD positions at top domestic or international universities, or for internships at AI research divisions

{%
  include button.html
  link="contact"
  text="See more details"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% include section.html %}

## Latest News

<ul class="news-list">
  {% for post in site.posts limit: 5 %}
    <li>
      <span class="news-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      <span class="news-excerpt">{{ post.excerpt | markdownify | remove: "<p>" | remove: "</p>" }}</span>
      <a href="{{ post.url | relative_url }}" class="news-more">Learn more →</a>
    </li>
  {% endfor %}
</ul>

{%
  include button.html
  link="blog"
  text="All News"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
