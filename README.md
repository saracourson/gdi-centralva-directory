# GDI Directory

[![Build Status](https://travis-ci.org/GirlDevelopItCentralVA/gdi-centralva-directory.svg?branch=master)](https://travis-ci.org/GirlDevelopItCentralVA/gdi-centralva-directory)

This repo has two purposes:

- Provide a directory listing of the people involved with the GirlDevelopIt Central VA chapter
- Serve as a learning tool for learning Git and GitHub

## Add yourself

1. Add a JSON file with your name as the filename, e.g. `taylor-swift.json`, to the `people/` directory. Fill out your information.
2. Send a PR.

Example JSON file:

```json
{
    "name": "Taylor Swift",
    "twitter": "SwiftOnSecurity"
}
```

Valid keys:

- `name` (required)
- `email`
- `github`
- `twitter`
- `personal`

## Build the site

- Install requirements:

```
pip install -r requirements.txt
```

- Build the site (and open it in your browser):

```
inv build -b
```
