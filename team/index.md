---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

Meet the members of StatAI Lab.

{% include section.html %}

## Group Photo

{%
  include figure.html
  image="images/group-photo.jpg"
  caption="StatAI Lab members"
%}

{% include section.html %}

## Principal Investigator

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}

{% include section.html %}

## PhD Students

{% include list.html data="members" component="portrait" filter="role == 'phd'" %}

{% include section.html %}

## Master's Students

{% include list.html data="members" component="portrait" filter="role == 'master'" %}

{% include section.html %}

## Undergraduate Students

{% include list.html data="members" component="portrait" filter="role == 'undergrad'" %}

{% include section.html %}

## Alumni

StatAI Lab is proud of our former members who continue to advance the field of AI and statistics in various institutions worldwide.

{% include list.html data="members" component="portrait" filter="role == 'alumni'" %}
