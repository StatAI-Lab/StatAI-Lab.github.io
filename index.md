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

## Latest News

<ul class="news-list">
  {% for post in site.posts limit: 5 %}
    <li>
      <span class="news-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      <a href="{{ post.url | relative_url }}" class="news-title">{{ post.title }}</a>
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

{% include section.html %}

## Highlights

{% capture text %}

Our lab investigates statistical theory in the era of large language models,
with a particular focus on interpretability, uncertainty quantification, and AI-assisted statistical inference.

{%
  include button.html
  link="projects"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  icon="fa-solid fa-book"
  link="projects"
  title="Publications"
  text=text
%}

{% capture text %}

We develop statistical methods and computational tools for analyzing complex data,
with emphasis on robust inference, causal discovery, and uncertainty quantification.

{%
  include button.html
  link="research"
  text="Browse our research"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  icon="fa-solid fa-wrench"
  link="research"
  title="Research"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

Meet the researchers behind StatAI Lab.

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  icon="fa-solid fa-user-group"
  link="team"
  title="Our Team"
  text=text
%}

{% include section.html %}

## Contact Us

We are always open to collaborations and inquiries from researchers and students interested in the intersection of LLMs and statistics.

{%
  include button.html
  type="email"
  text="zhoufan@mail.shufe.edu.cn"
  link="zhoufan@mail.shufe.edu.cn"
%}
{%
  include button.html
  type="email"
  text="statai@163.com"
  link="statai@163.com"
%}
{%
  include button.html
  type="address"
  tooltip="Shanghai University of Finance and Economics"
  link="https://www.google.com/maps/search/Shanghai+University+of+Finance+and+Economics"
%}