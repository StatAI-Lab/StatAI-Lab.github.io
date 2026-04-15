---
title: Research
nav:
  order: 1
  tooltip: Research projects and software
---

# {% include icon.html icon="fa-solid fa-wrench" %}Research

Our research spans the intersection of large language models and statistical inference,
with a focus on developing principled methods for uncertainty quantification, interpretability,
and robust decision-making in AI systems.

{% include tags.html tags="software, resource, methodology" %}

{% include search-info.html %}

{% include section.html %}

## Featured Projects

{% include list.html component="card" data="projects" filter="group == 'featured'" %}

{% include section.html %}

## Ongoing Work

{% include list.html component="card" data="projects" filter="!group" style="small" %}
