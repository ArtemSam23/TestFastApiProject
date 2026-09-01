import asyncio
import sys

from app.harness import run


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit('пример: python -m app.cli "кто руководитель у Ковалёва"')
    answer = asyncio.run(run(sys.argv[1]))
    print("--- итог ---")
    print(answer)


if __name__ == "__main__":
    main()
