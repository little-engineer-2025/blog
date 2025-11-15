# AI Agents Guide

This document provides guidance for AI agents and tools working with this Pelican-based blog repository.

## Repository Overview

This is a static blog generated using **Pelican**, a static site generator written in Python. The repository includes:

- **Content**: Markdown files in `content/` directory for blog articles
- **Configuration**: `pelicanconf.py` for development and `publishconf.py` for production
- **Templates**: Blog templates in `templates/` directory
- **Scripts**: Helper scripts for content management in `scripts/`

## Development Environment

### Setup Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`
- Pelican static site generator
- Running in VS Code (Flatpak environment)

### Installation

```bash
pip install -r requirements.txt
```

## Key Workflows

### Creating New Articles

Use the provided script to create new articles:

```bash
./scripts/new-article.sh
```

Articles should be created as markdown files in the `content/` directory with the naming convention:
`YYYY-MM-DD--article-title.md`

### Building the Site

Generate the static site:

```bash
make html
```

### Preview the Site

Start the development server:

```bash
make serve
```

The site will be available locally for preview.

### Publishing

Build for production:

```bash
make publish
```

## Project Structure

- `content/` - Blog article files (markdown)
- `templates/` - Jinja2 templates for site rendering
- `scripts/` - Helper scripts (e.g., new-article.sh)
- `static/` - Static assets
- `pelicanconf.py` - Development configuration
- `publishconf.py` - Production configuration
- `Makefile` - Build automation
- `tasks.py` - Invoke tasks for automation
- `custom.mk` - Custom make rules

## Common Tasks for Agents

### Reading Articles

Articles are located in `content/` directory as markdown files. Each file contains:
- Front matter (metadata)
- Article content in markdown format

### Modifying Content

When editing or creating content:
1. Maintain the filename convention: `YYYY-MM-DD--title.md`
2. Ensure proper markdown formatting
3. Test by building locally with `make html`

### Working with Templates

Templates are in `templates/` directory. The blog uses theme templates that can be customized.

## Flatpak-Specific Considerations

When running VS Code in Flatpak:

- File paths should use standard Linux conventions
- Python virtual environments work within the Flatpak sandbox
- Terminal operations within VS Code run in the Flatpak environment
- External tools must be accessible within the Flatpak or properly configured

## Useful Commands

| Command | Purpose |
|---------|---------|
| `make html` | Build development site |
| `make serve` | Start development server |
| `make publish` | Build production site |
| `make clean` | Clean generated files |
| `make help` | Show available make targets |
| `./scripts/new-article.sh` | Create new article |

## Notes for AI Agents

- Always preserve the existing file structure and naming conventions
- Test changes by building the site before committing
- Refer to `pelicanconf.py` for configuration defaults
- Use the Makefile targets for common operations
- Maintain markdown formatting standards in article files 