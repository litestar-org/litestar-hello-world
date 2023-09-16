"""Script to replace occurrences of 'project-template' with new name in all files of a directory."""

import re
from pathlib import Path

import click


def replace_template_name(directory: Path, new_name: str) -> None:
    """Replaces occurrences of 'project-template' with new name in all files of a directory.

    Args:
        directory (Path): The directory path to scan.
        new_name (str): The new name to replace 'project-template' with.
    """
    for file in directory.rglob("*"):
        if file.is_file():
            with Path(file).open(encoding="utf-8", errors="ignore") as f:
                content = f.read()

            new_content = re.sub(r"project-template", new_name, content)

            with Path(file).open("w", encoding="utf-8", errors="ignore") as f:
                f.write(new_content)


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--name", "-n", type=str, required=True, help="The new project name.")
@click.option("--directory", "-d", type=Path, default=Path(), help="The directory to scan.")
def main(name: str, directory: Path) -> None:
    """Rename a template project to a new project name.

    Args:
        name (str): The new project name.
        directory (Path): The directory to scan.
    """
    replace_template_name(directory, name)


if __name__ == "__main__":
    main()
