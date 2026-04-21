---
---

## About us

StatAI Lab, led by Dr. Fan Zhou at Shanghai University of Finance and Economics, focuses on the **deep integration of artificial intelligence and statistics**. Our research explores how statistical principles can enhance the interpretability and uncertainty quantification of AI systems, while also investigating how modern AI can advance statistical reasoning and data analysis.

{%
  include button.html
  type="github"
  text="On GitHub"
  link="StatAI-Lab"
%}

{% include section.html %}

## Our Research Focus

Our research spans the intersection of statistical theory, machine learning, and large language models. We focus on developing reliable methods to ensure robust decision-making, interpretability, and reliable uncertainty quantification in modern AI systems.

+ **AI for Statistics**: We connect foundation models with statistical inference by **developing benchmark datasets** to evaluate and enhance the statistical reasoning capabilities of large language models, and by **designing agentic systems** for **automated statistical reasoning**, including AI agents that assist in **theorem proving**. More broadly, we use statistical principles to improve the **reliability**, **security**, and **interpretability** of LLMs.

+ **Methodology and Theory of Reinforcement Learning**: We develop both theoretical foundations and practical methodologies for RL, focusing on **error analysis** and **variance control** in deep reinforcement learning, as well as **principled distributional modeling of rewards**; our work addresses challenges such as data dependence in offline settings and the validity of quantile-based representations, enabling statistically robust policy evaluation, consistent value estimation, and reliable decision-making under distribution shifts.

+ **Two-Sided Market and Spatio-temporal System**: We develop **data-driven models and decision frameworks** for dynamic two-sided markets, including supply–demand equilibrium metics, reinforcement learning based matching policy, and a suite of A/B testing methods. These approaches enable efficient matching, robust policy evaluation, and improved system performance in complex, time-evolving environments.

+ **Uncertainty Quantification**: Reliable AI requires principled uncertainty assessment. We develop **statistically grounded methods** for understanding uncertainty, reliability, and distributional behavior in modern learning systems, with applications ranging from robust statistical prediction and influence-based model assessment to trustworthy large language models and quantile-based learning for sequential decision-making.

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

We **enthusiastically welcome prospective PhD and Master's students from diverse universities** who are passionate about research at the intersection of LLMs and statistics. Whether you are from a local or international institution, we value the unique perspective you bring to our team. We are **always open to fostering collaborations and inquiries from researchers and practitioners across all universities, institutions, and companies**.

### Prospective Students

**PhD Candidates**

- Aspiring to an academic career in the future
- Strong mathematical and statistical foundations, self-motivated, and passionate about research
- Familiar with Python and GPU computing; programming skills are a plus

**Master's Students**

- Interested in pursuing further PhD studies or working in industry roles related to algorithms and research
- Master's students will participate in systematic research training led by PhD students and may be recommended for PhD positions at top domestic or international universities, or for internships at AI research divisions

If you are interested in our projects and would like to join StatAI Lab as a **full-time** member, please send your **CV** along with a **brief statement** of your **research interests** to zhoufan@mail.shufe.edu.cn

### Collaboration & Partnerships

We are also open to collaborations with **enterprises, institutions, schools, and individuals** who share an interest in LLMs and statistical research. If you are interested in working with us, please fill out the registration form below and we will get back to you.

{%
  include button.html
  link="https://docs.google.com/forms/placeholder"
  text="Register your interest"
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
