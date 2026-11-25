"""Entry for make.fun: The Funniest Office Joke, Judged Head to Head.

Writes a single original one-line office joke to entry.txt.
"""

import os

JOKE = "We replaced our weekly status meeting with an email, and productivity rose so fast that management scheduled a meeting to find out why."


def validate(text):
    """Check the entry against the gate: 1-200 chars, one line, clean UTF-8."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text or "\t" in text:
        raise ValueError("entry must be a single line with no newline or tab")
    if text.splitlines() != [text]:
        raise ValueError("entry must be exactly one line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if text.encode("utf-8").decode("utf-8") != text:
        raise ValueError("entry must round-trip through UTF-8")
    return text


def main():
    text = validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "rb") as f:
        raw = f.read()
    if raw != text.encode("utf-8"):
        raise ValueError("entry.txt is not byte-identical to the intended entry")
    if raw.decode("utf-8") != text:
        raise ValueError("entry.txt does not decode back to the intended entry")
    print("wrote {} ({} characters)".format(path, len(text)))


if __name__ == "__main__":
    main()
