"""Tests for the convention sections"""

import collections
import re


def test_section_identifier_valid(section):
    assert re.match(r"[A-Z]+", section.identifier)


def test_section_identifiers_unique(sections):
    section_identifier_counts = collections.defaultdict(int)
    for section in sections:
        section_identifier_counts[section.identifier] += 1

    assert all(count == 1 for count in section_identifier_counts.values())


def test_section_identifier_follows_case_convention(section):
    section_title = ("**".join(section.header_text.split("**")[2:])).strip()
    assert section_title[0] == section_title[0].upper()