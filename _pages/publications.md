---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

My complete publication list is [available on my Google Scholar profile](https://scholar.google.com/citations?user=YS8gO1MAAAAJ&hl=en). Select publications are detailed below:

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
