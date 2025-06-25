# GitHub Copilot CI/CD Exercise - Local GitHub Actions with Act

**⚠️ PREREQUISITES REQUIRED ⚠️**

This exercise requires the following to be installed and available on your system:

## 🔧 Required Software

### Essential Requirements
- **Docker Desktop** - Must be installed and running
  - Download: https://www.docker.com/products/docker-desktop/
  - Verify: `docker --version` should work
- **Git** - For repository operations
  - Verify: `git --version` should work
- **VS Code** with GitHub Copilot extension enabled

### Installation During Exercise
- **Act** - We'll install this together using Copilot's guidance
  - GitHub: https://github.com/nektos/act
  - Common methods: Homebrew (macOS), Chocolatey (Windows), or manual download

## 🚨 System Requirements

- **Operating System**: macOS, Linux, or Windows with WSL2
- **Memory**: At least 4GB RAM available for Docker containers
- **Storage**: ~2GB free space for Docker images
- **Internet**: Required for downloading Docker images and Act installation

---

## Exercise Overview

**Goal**: Set up Act to run GitHub Actions locally and optimize CI workflows with Copilot assistance.

**Difficulty**: Beginner to Intermediate  
**Focus**: DevOps tooling, local development workflows, CI/CD optimization

---

## Phase 1: Installation and Setup

### Step 1: Verify Prerequisites

First, let's confirm your system is ready:

```bash
# Verify Docker is running
docker --version
docker ps

# Verify Git is available
git --version

# Check if you're in the project directory
pwd
ls -la .github/workflows/
```

### Step 2: Act Installation with Copilot

Use Copilot to guide the installation process:

```
@terminal How do I install Act on my operating system to run GitHub Actions locally?

I need to understand:
1. The best installation method for my OS
2. Any additional configuration required
3. How to verify the installation works
```

**Common installation commands** (Copilot will help you choose):
```bash
# macOS with Homebrew
brew install act

# Windows with Chocolatey
choco install act-cli

# Linux (manual download)
curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```

### Step 3: Verify Act Installation

```bash
# Check Act version
act --version

# See available workflows
act -l
```

If you encounter issues, use Copilot:
```
Act installation failed with this error: #terminalLastCommand

Help me troubleshoot:
1. What caused this error?
2. What are alternative installation methods?
3. Are there any missing dependencies?
```

---

## Phase 2: Running Local CI Pipeline

### Step 1: Analyze Our Workflow

Let's understand what we're about to run:

```
#file:.github/workflows/ci.yml /explain

Analyze our CI workflow. What will happen when I run this locally with Act? 
- What Docker images will it use?
- Are there any potential issues?
- What should I expect to see?
```

### Step 2: First Act Run (Dry Run)

Always start with a dry run to see what would happen:

```bash
# Dry run - shows what would execute without running it
act -n

# If you want to see more details
act -n -v
```

Use Copilot to understand the output:
```
Act dry run shows this output: #terminalLastCommand

Explain:
1. What Docker images will be downloaded?
2. What steps will be executed?
3. Are there any warnings I should address?
```

### Step 3: Full CI Run

Now let's run the actual CI pipeline:

```bash
# Run the full CI pipeline
act

# If you want to see detailed logs
act -v
```

**Expected behavior:**
- Docker images will be downloaded (this may take a few minutes the first time)
- Python environments will be set up for multiple versions
- Tests, linting, and formatting checks will run

### Step 4: Troubleshooting Common Issues

If the run fails, use Copilot for diagnosis:

```
The Act run failed with this error: #terminalLastCommand

Help me understand and fix:
1. Is this a Docker issue, Python issue, or Act configuration issue?
2. What's the specific cause of this error?
3. How can I resolve this?
4. Are there any Act-specific configurations I need?
```

**Common issues and Copilot queries:**
- Docker image problems: `@terminal explain this Docker pull error #terminalLastCommand`
- Python version issues: `How do I configure Act to use the correct Python versions? #problems`
- Permission issues: `@terminal how to fix Docker permission denied errors #terminalLastCommand`

---

## Phase 3: Optimization and Integration

### Step 1: Create Local Development Commands

Use Copilot to create convenient commands:

```
/new Create a Makefile that uses Act to run different CI jobs locally

I want these commands:
- make test-local: run only the test steps
- make lint-local: run only linting and formatting
- make ci-full: run the complete CI pipeline
- make ci-quick: run a fast subset for development

Use our existing .github/workflows/ci.yml as the base.
```

### Step 2: Act Configuration

Let's optimize Act for our project:

```
How can I create a .actrc file to optimize Act for our Python project? #file:.github/workflows/ci.yml

I want to:
1. Use appropriate Docker images for Python
2. Set up proper environment variables
3. Optimize for faster local development
4. Handle secrets and environment configuration
```

### Step 3: VS Code Integration (Optional)

```
/new Create VS Code tasks.json entries for running Act commands

I want tasks for:
- Running full CI locally
- Running just tests
- Running just linting
- Debugging CI issues

Make them easy to run from VS Code's command palette.
```

---

## Success Criteria

By the end of this exercise, you should have:

- [ ] Act installed and working on your system
- [ ] Successfully run the GitHub Actions workflow locally
- [ ] Docker images downloaded and cached for future runs
- [ ] Understanding of Act output and common issues
- [ ] Local development commands (Makefile or scripts)
- [ ] Optional: VS Code integration for easy access

---

## Bonus Challenges 🏴‍☠️

If you finish early and want to explore more:

### Challenge 1: Multi-Workflow Support
```
Our project might have multiple workflows in the future. How can I configure Act to handle different types of workflows (CI, deployment, security scans)?
```

### Challenge 2: Custom Docker Images
```
How can I create or configure custom Docker images for Act that include all our project dependencies pre-installed for faster local runs?
```

### Challenge 3: Integration with Git Hooks
```
/new Create a pre-commit hook that runs a subset of our CI checks locally using Act before allowing commits.
```

---

## Troubleshooting Guide

### Common Issues and Solutions

**"Docker daemon not running"**
```
@terminal How do I start Docker Desktop and verify it's running properly?
```

**"Permission denied" errors**
```
@terminal How to fix Docker permission issues on my operating system #terminalLastCommand
```

**"Act command not found"**
```
Act installation seems incomplete. How can I verify and fix the installation? #terminalLastCommand
```

**Slow Docker image downloads**
```
How can I configure Docker to use faster mirrors or cache images for Act? #problems
```

**Python version conflicts**
```
Act is using the wrong Python version. How do I configure it to match our CI requirements? #file:.github/workflows/ci.yml
```

---

## What You've Learned

- How to run GitHub Actions locally for faster feedback
- Docker-based CI/CD workflows and troubleshooting
- Act configuration and optimization
- Integration of local CI tools with development workflow
- Using Copilot for DevOps tooling and troubleshooting

This exercise bridges the gap between development and deployment, giving you practical DevOps skills that you can immediately apply to any project with GitHub Actions!

*🏴‍☠️ Congratulations, matey! You've mastered the art of local CI/CD like a true DevOps pirate! ⚓*
