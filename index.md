---
---

## About us

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

## Our Research Focus

Our research spans the intersection of statistical theory, machine learning, and large language models. We focus on developing reliable methods to ensure robust decision-making, interpretability, and reliable uncertainty quantification in modern AI systems.

+ **AI for Statistics**: We connect foundation models with statistical inference. Our work explores how statistical principles can enhance the security, reliability, and interpretability of Large Language Models (LLMs), while **also using** LLMs to **improve** traditional statistical prediction.

+ **Methodology and Theory of Reinforcement Learning**: We build solid theoretical foundations for RL. Our focus is on enabling reliable decision-making in complex environments through variance control, robust learning under distribution shifts, and sample-efficient exploration strategies.

+ **Two-Sided Market and Spatio-temporal System**: We apply advanced machine learning to optimize complex, real-world platforms. By integrating causal inference and stochastic optimization, we solve challenges in ride-sharing equilibrium, recommendation systems, and spatio-temporal forecasting.

+ **Uncertainty Quantification**: Trustworthy AI requires reliable estimation. We develop robust methods for off-policy evaluation in confounded environments, deep nonparametric regression, and optimal treatment allocation, ensuring data-driven decisions are clear and accurate.

+ **Graph Representation Learning**: **Since network data is everywhere**, we develop novel statistical methods for complex graph structures. Our work includes **creating** diffusion-based representation learning and addressing semi-supervised learning challenges with non-ignorable missing data.

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

We **enthusiastically welcome prospective PhD and Master's students from diverse universities** who are passionate about research at the intersection of LLMs and statistics. Whether you are from a local or international institution, we value the unique perspective you bring to our team. We are **always open to fostering collaborations and inquiries from researchers and practitioners across all universities, institutions, and companies**. We thrive on building connections with those interested in advancing the field of LLMs and statistics together.

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
  {% assign visible_posts = site.posts | where_exp: "post", "post.draft != true" %}
  {% for post in visible_posts limit: 5 %}
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
