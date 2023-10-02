#!/usr/bin/env python3

# gsearch.py -- semi-automated Google search
# uses Programmable Search Engine
# https://developers.google.com/custom-search/v1/overview

import json
import os
import sys

import click
import requests
import yaml
from dotenv import load_dotenv


load_dotenv()
ENGINE_ID = os.environ["GOOGLE_ENGINE_ID"]
API_KEY = os.environ["GOOGLE_API_KEY"]
SEARCH_URL = "https://www.googleapis.com/customsearch/v1"


def join_or(terms) -> str:
    """Join search terms with OR operator"""
    if not terms:
        return ''
    safe_terms = [f'"{term.strip()}"' for term in terms]
    return " OR ".join(safe_terms)


def join_and(phrases) -> str:
    """Join search phrases with AND operator"""
    def quote(words):
        if ' ' in words:
            return f"({words.strip()})"
        return words
    # strip empty sub-phrases
    safe_phrases = [quote(phrase) for phrase in phrases if phrase]
    return " AND ".join(safe_phrases)


def format_query(query):
    exclude = [f"-{x}" for x in query.get("exclude", [])]
    sites = [f"site:{x}" for x in query.get("sites", [])]
    full = [
        join_or(query["search"]),
        join_or(query["location"]),
        join_or(sites),
        join_or(query.get("require")),
        join_or(exclude)
    ]
    return join_and(full)


def print_results(results):
    results = results.copy()
    try:
        items = results.pop('items')
    except KeyError:
        click.echo('ERROR?   ')
        json.dump(results, sys.stdout, indent=2)
        return
    
    json.dump(results, sys.stdout, indent=2)
    click.echo(f'REQUEST.searchTerms: {results["queries"]["request"][0]["searchTerms"]}')
    click.echo(f'REQUEST.totalResults: {results["searchInformation"]["totalResults"]}')
    # click.echo(f'REQUEST.correctedQuery: {results["spelling"]["correctedQuery"]}')
    for item in items[:3]:
        click.echo(f'ITEM.title: {item["title"]}')
        click.echo(f'ITEM.link: {item["link"]}')

import urllib.parse

@click.command()
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose mode')
@click.option('-n', '--dry-run', is_flag=True, help='Dry run')
def main(dry_run, verbose):
    with open("example.yaml") as f:
        query = yaml.safe_load(f)

    query_str = format_query(query)
    search = SEARCH_URL
    params = {
        "q": query_str,
        "key": API_KEY,
        "cx": ENGINE_ID
    }
    # FIXME:
    params['q'] = urllib.parse.quote_plus(params['q'])

    if verbose or dry_run:
        click.echo(f'{query_str=}')
        # FIXME: params['key'] = 'REDACTED'
        click.echo(f'{params=}')
        if dry_run:
            sys.exit(0)
    
    results = requests.get(search, params=params).json()
    if "error" in results:
        sys.exit(f'Search failed: {results["error"]["message"]}')

    if verbose:
        click.echo('RESULTS:')
        print_results(results)

    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

    totalResults = results["searchInformation"]["totalResults"]
    click.echo(f"COUNT: {totalResults}")


if __name__ == "__main__":
    main()
