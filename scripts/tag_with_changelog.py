import logging
import re
import subprocess
import toml

from colorama import Fore

from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from mistletoe.token import Token
from mistletoe.block_token import Heading, Document
from mistletoe.span_token import RawText
from mistletoe.markdown_renderer import MarkdownRenderer


SEMVER_REGEX = r"^\[(([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+)?)\]"

PROGRAM_NAME = Path(__file__).name


def get_heading_text(heading: Heading):
    return "".join(
        t.content for t in heading.children or [] if isinstance(t, RawText)
    ).strip()


def get_current_release(changelog_text: str, current_version: str):
    document = Document(changelog_text)

    renderer = MarkdownRenderer()

    if not document.children:
        raise ValueError("No children found in the document")

    release_headings: list[tuple[str, Heading]] = []

    document_nodes = list(document.children)

    for child in document_nodes:
        if isinstance(child, Heading):
            if not child.children:
                continue
            heading_text = get_heading_text(child)

            if match := re.match(SEMVER_REGEX, heading_text):
                release_headings.append((match.group(1), child))

    if not release_headings:
        raise ValueError("No release found in the document")

    current_release = next(
        (h for h in release_headings if h[0] == current_version), None
    )
    if not current_release:
        raise ValueError(
            f"Current release `{current_version}` not found in the document"
        )
    current_release_heading_index = release_headings.index(current_release)

    next_release = release_headings[current_release_heading_index + 1]

    current_release_index = document_nodes.index(current_release[1])
    next_release_index = document_nodes.index(next_release[1])

    if current_release_index + 1 == next_release_index:
        raise ValueError("Release is empty")

    latest_release_nodes = document_nodes[current_release_index:next_release_index]

    result_document = Document("")

    result_document.children = latest_release_nodes

    return renderer.render(result_document)


def main():
    with open("CHANGELOG.md", "r") as file:
        changelog = file.read()
    logger.info(
        f"[{PROGRAM_NAME}] Successfully read {Fore.YELLOW}`CHANGELOG.md`{Fore.RESET} file"
    )

    current_version = toml.load("pyproject.toml")["project"]["version"]
    logger.info(
        f"[{PROGRAM_NAME}] Current version is {Fore.YELLOW}`{current_version}`{Fore.RESET}"
    )

    latest_release = get_current_release(changelog, current_version)
    logger.info(
        f"[{PROGRAM_NAME}] latest_release extracted ({Fore.YELLOW}{len(latest_release)}{Fore.RESET} characters, {Fore.YELLOW}`{latest_release.splitlines()[0]}`{Fore.RESET}...)"
    )

    subprocess.run(["git", "tag", "-a", f"v{current_version}", "-m", latest_release])


if __name__ == "__main__":
    main()
