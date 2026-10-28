# YouTube Embed URL Extractor

A lightweight Python command-line utility that extracts a video ID from YouTube iframe HTML and converts it into a short shareable link.

## Example

Input:
```html
<iframe src="https://www.youtube.com/embed/abc123"></iframe>
```

Output:
```text
https://youtu.be/abc123
```

## Run locally

Requires Python 3; uses only the Python standard library.

```bash
python3 youtube.py
```

Paste the iframe HTML at the `HTML:` prompt.

## How it works

1. Searches the supplied text with a case-insensitive regular expression.
2. Captures the video ID after `youtube.com/embed/`.
3. Returns a `youtu.be` link.

## Supported input and limitations

- Supports HTTP or HTTPS embed URLs, with or without `www.`.
- The iframe's `src` attribute must use double quotes.
- Returns the first matching embed.
- Exits with an error message when no matching embed is found.
- Does not fetch pages, validate whether a video exists, or parse arbitrary HTML.

## Technical focus

Regular expressions, string processing, command-line input, and standard-library scripting.
