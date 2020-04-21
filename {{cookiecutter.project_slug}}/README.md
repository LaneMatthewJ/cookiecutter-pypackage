{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{% for _ in cookiecutter.project_name %}={% endfor %}

<h1>{{ cookiecutter.project_name }}<img src='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/master/img/snek.jpg' align='right' width='180' height='104'></h1>


{% if is_open_source %}
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_slug}})

[![Build Status](https://travis-ci.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=master)](https://travis-ci.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})

{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
[![Updates](https://pyup.io/repos/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/shield.svg)](https://pyup.io/repos/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/)

{% endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

#### Features

{%- if cookiecutter.command_line_interface|lower == 'argh' %}

{{ cookiecutter.project_name }} comes with a built in command line interface:

```python
python -m {{ cookiecutter.project_slug }}.cli greet
```

{%- endif %}
