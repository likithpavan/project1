"""
Simple greeter utility for Git practice.

Suggested commit steps you can try:
- Add this file
- Change default name from "World" to something else
- Add another greeting style or an option flag
"""

from typing import Optional


def generate_greeting(name: str, excited: bool = False) -> str:
    """Return a friendly greeting for the provided name."""
    base = f"Hello, {name}"
    return base + ("!" if excited else ".")


def main(argv: Optional[list[str]] = None) -> None:
    """Run a tiny CLI that prints a greeting.

    Usage examples:
    - python example.py            -> Hello, World.
    - python example.py Alice      -> Hello, Alice.
    - python example.py Alice !    -> Hello, Alice!
    """
    import sys

    args = list(sys.argv[1:] if argv is None else argv)
    name = args[0] if args else "World"
    excited = len(args) > 1 and args[1] == "!"

    print(generate_greeting(name, excited))


if __name__ == "__main__":
    main()



