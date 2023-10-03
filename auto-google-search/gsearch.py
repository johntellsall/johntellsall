#!/usr/bin/env python3

# gsearch.py -- semi-automated Google search
# uses Programmable Search Engine
# https://developers.google.com/custom-search/v1/overview

import json
import os
import sys

import click
import google_custom_search
import yaml
from dotenv import load_dotenv


load_dotenv()
ENGINE_ID = os.environ["GOOGLE_ENGINE_ID"]
API_KEY = os.environ["GOOGLE_API_KEY"]


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


def print_results(results, limit):
    if limit:
        results = results[:limit]
    for item in results:
        click.echo(f'ITEM.title: {item.title}')
        click.echo(f'ITEM.link: {item.data.get("link")}')


def write_results(results):
    output = [item.data for item in results]
    with open("results.json", "w") as f:
        json.dump(output, f, indent=2)


@click.command()
@click.option('--limit', default=3, type=int, help='Number of results to return')
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose mode')
@click.option('-n', '--dry-run', is_flag=True, help='Dry run')
@click.argument('input', type=click.File('r'), required=False)
def main(dry_run, verbose, input="example.yaml", limit=None, query=None):
    if not limit:
        limit = None
    if query is None:
        query = yaml.safe_load(input)

    query_str = format_query(query)
    
    if verbose or dry_run:
        click.echo(f'{query_str=}')
        if dry_run:
            sys.exit(0)
    
    google = google_custom_search.CustomSearch(apikey=API_KEY, engine_id=ENGINE_ID)

    results = google.search(query_str)
  
    if verbose:
        click.echo('RESULTS:')
        print_results(results, limit=limit)

    write_results(results)


if __name__ == "__main__":
    main()
