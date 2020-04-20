"""Command line interface for {{cookiecutter.project_slug}}."""

{%- if cookiecutter.command_line_interface|lower == 'argh' %}
import argh


def greet() -> None:
    r"""Say hello, {{ cookiecutter.project_slug }}"""
    print(f'Hello, world!')


def main():
    parser = argh.ArghParser()
    parser.add_commands([greet])
    parser.dispatch()
{%- endif %}


if __name__=='__main__':
    main()
