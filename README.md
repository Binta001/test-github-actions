# Test GitHub Actions Repository

This is a test repository demonstrating GitHub Actions workflows.

## Workflow Status

![CI Workflow](https://github.com/Binta001/test-github-actions/actions/workflows/ci.yml/badge.svg)

## About

This repository contains a simple GitHub Actions workflow that:
- Runs on push to main branch
- Runs on pull requests to main branch
- Can be manually triggered
- Displays system information
- Creates test files
- Simulates running tests

## Workflow File

The workflow is defined in `.github/workflows/ci.yml`

## Usage

The workflow will automatically run when you:
1. Push code to the main branch
2. Create a pull request to the main branch
3. Manually trigger it from the Actions tab in GitHub

## Try it out!

You can manually trigger the workflow by:
1. Going to the "Actions" tab in this repository
2. Selecting "CI Workflow" from the left sidebar
3. Clicking "Run workflow" button
