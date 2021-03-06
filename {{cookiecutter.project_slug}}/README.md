{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

<h1>{{ cookiecutter.project_name }}<img src='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/main/img/snek.png' align='right' width='180' height='104'></h1>


{% if is_open_source %}

[![Build Status](https://travis-ci.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=master)](https://travis-ci.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![pypi](https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.project_slug}})
{%- endif %}


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
