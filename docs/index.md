## TL;DR

I wanted a preconfigured Python environment with all the best tools and practices already set up, because doing this for every new project is a massive pain. Somehow this turned into a blog post about AI-assisted development. But hey, at least I now have atemplate that works out of the box!

## Quick Start

To get started with this project, see the [Getting Started](getting-started.md) guide.

## Why I Created This Project

When I first started using Cursor, it completely transformed my development workflow. The AI-assisted coding allowed me to develop much faster than ever before, though it wasn't without its challenges. I found myself starting many projects and coding at an unprecedented pace, but still encountering errors and inconsistencies that required manual intervention.

My journey with AI coding tools has evolved significantly over time – from the early days of ChatGPT, to GitHub Copilot, and finally to Cursor with Claude integration. Now with the latest amazing agents, we're entering a new era of development where the human-AI collaboration is deeper than ever before.

And of course, it's worth noting that all the code in this project – and even this documentation you're reading right now – was written by AI, guided by some carefully crafted prompts from me. This is a testament to how far AI coding assistants have come and how they can be leveraged to create complete, production-ready projects with minimal human intervention.

As AI tools evolved into agents, I noticed a fundamental shift in my approach to software development. Documentation and code readability became king. I found myself spending more time reading my own draft PRs and crafting prompts than writing actual code. And honestly, why should I work hard on repetitive tasks when an agent can handle all the linting and CI problems? I could simply instruct the agent to document, format, and pretty much do everything.

What's fascinating is how this has transformed my daily workflow. I've gone from spending 80% of my time writing code and 20% reviewing it, to almost the exact opposite. Now I spend most of my day reviewing AI-generated code, providing feedback, and refining prompts. (These numbers are completely random, by the way – I don't actually track these metrics, but the shift has been dramatic.) The actual coding process has become more of a collaborative dialogue with the AI, where I focus on architectural decisions and quality control rather than typing out implementation details. This shift has not only increased my productivity but has also improved the overall quality of my projects, as I can dedicate more attention to design patterns, edge cases, and user experience.

This shift in responsibilities is profound – code readability and documentation should be the AI's problem from now on. With everything properly configured, I can let the AI crack its head on implementation details while I focus on planning and solving higher-level problems. This is the future of development: humans handling the creative and strategic aspects while AI handles the technical implementation and maintenance.

One tool that has been absolutely transformative in this process is the Sequential Thinking MCP (Model Context Protocol). It's a must-have for any serious AI-assisted development. This approach allows the AI to break down complex problems into manageable steps, think through each one carefully, and revise its thinking when necessary. The results are dramatically better than traditional prompting – more thorough, more accurate, and more reliable. If you're working with AI agents, I can't recommend Sequential Thinking enough – it's truly amazing how it improves the quality of AI-generated solutions.

## The Preconfigured Environment Problem

One of the biggest pain points I've encountered is setting up a new project environment. Every time I start something new, I find myself spending hours configuring linters, formatters, test frameworks, documentation tools, and CI/CD pipelines. It's tedious, repetitive work that takes away from actual development time. With AI allowing me to work on more projects simultaneously and explore new ideas faster, this configuration overhead became an even bigger bottleneck.

I wanted something preconfigured with all the options and best practices already in place – a template that just works out of the box. Something that integrates all the modern Python tools like Ruff, Pyright, UV, pytest and many more in a way that they complement each other rather than conflict. Something that handles the boilerplate so I can focus on building features. That's exactly what this project aims to be – a comprehensive starting point that eliminates the setup pain and lets you dive straight into development.

## The Memory Bank Experiment

I've also experimented with other approaches to AI-assisted development, including the [Cline Memory Bank](https://docs.cline.bot/improving-your-prompting-skills/custom-instructions-library/cline-memory-bank) system. This approach uses a structured documentation system to maintain context across sessions, with files like `projectbrief.md`, `productContext.md`, and `activeContext.md` serving as the AI's "memory."

Initially, I was impressed with how well it worked – even better than Cursor in some ways. The structured approach to maintaining context seemed promising, especially for smaller projects. However, as my projects grew in complexity, I quickly discovered its limitations. The system started to feel "off" – the AI would forget critical details despite all the carefully maintained documentation files.

The fundamental issue I discovered is that while context size is important, the content of that context matters more. When working on a real project, I even tried switching from Claude to Gemini for its huge context window, but the problem only got worse.

When on a real project, you don't actually need to remember everything – just the general flow. When specific questions or issues arise, developers check the code, not the documentation (which is often outdated or incomplete).

I don't think having AI check documentation while writing code is the answer. Documentation isn't bad—it's essential—but there are ways to make it much easier to maintain, as demonstrated in this repo. The pyproject.toml configuration and CI workflow in ci.yml automate documentation checks, coverage reporting, and quality metrics, ensuring documentation stays accurate and useful without manual effort. This automation creates a cycle where good documentation becomes a natural part of development rather than an afterthought. And it's especially good when AI is the one to write it.

**Code is king** – and I believe this project template solves this problem in a more practical way:

- You get "AI-based docs" that are generated alongside the code
- You get the cleanest code possible through automated tooling
- You run every possible tool to ensure quality and correctness

Yes, development might be a bit slower, and the AI occasionally fails, but the safety net of preconfigured tools keeps you on track. Everything is set up to work together harmoniously, which is something the Memory Bank approach couldn't provide.

This approach isn't without trade-offs. It's sometimes slower, and I've disabled some features in my projects to find the right balance. But the key insight is: if something is slowing you down, just disable it!

I've always wanted that one project template that works everywhere – something that handles boilerplate stuff while still using cutting-edge tools. The challenge is that tools like Pyright, Ruff, UV, and the configurations in pyproject.toml can be hard to combine and configure correctly. Moreover, without the right configuration, your IDE becomes painfully slow.

So here it is: a project template designed to keep everything fast and safe while still working smoothly. It's the Python Starting Project – a comprehensive template that brings together best practices for configuration, logging, code quality, and project structure.

In the future, I plan to create branches with custom configurations that enable or disable specific features, providing predefined setups for different needs. But for now, here's the full release with everything I've found useful in my development journey.

Any help, contributions, or suggestions are welcome! If you have ideas for improvements or want to adapt this template for other languages, please feel free to contribute. Together, we can make this project even more useful for developers everywhere.

And by the way, I've noticed that the AI tends to make me sound way older and more formal than I actually am in this documentation. I'm actually quite young and don't usually write this formally, but I've let the AI keep its "professional documentation voice" because it seems to work well for this project. Just know there's a real human behind all this corporate-sounding text!

{%
include-markdown "../README.md"
%}

## Documentation

- [Getting Started](getting-started.md)
- [Architecture](architecture/configuration.md)
- [Development](development/pre-commit-hooks.md)
- [API Reference](api/index.md)
