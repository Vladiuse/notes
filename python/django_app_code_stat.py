"""Standalone script counting code and test lines per app directory."""  # noqa: INP001

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def count_lines_in_dir(path: Path) -> tuple[int, int]:
    """Возвращает (строк_кода, строк_тестов) для указанной папки."""
    code_lines = 0
    test_lines = 0
    for file_path in path.rglob("*.py"):
        # пропускаем миграции
        if "migrations" in str(file_path.parent):
            continue
        with file_path.open(encoding="utf-8", errors="ignore") as file_obj:
            lines = sum(1 for _ in file_obj)
        if "test" in file_path.name.lower() or "tests" in str(file_path.parent).lower():
            test_lines += lines
        else:
            code_lines += lines
    return code_lines, test_lines


def main() -> None:
    total_code, total_tests = 0, 0
    for path in sorted(BASE_DIR.iterdir()):
        if not path.is_dir() or path.name.startswith((".", "__")):
            continue
        # считаем только папки, содержащие Python-код
        if not any(child.suffix == ".py" and child.is_file() for child in path.iterdir()):
            continue

        code, tests = count_lines_in_dir(path)
        if code or tests:
            print(f"{path.name}: code={code}, tests={tests}")  # noqa: T201
            total_code += code
            total_tests += tests

    print("-" * 40)  # noqa: T201
    print(f"TOTAL: code={total_code}, tests={total_tests}, all={total_code + total_tests}")  # noqa: T201


if __name__ == "__main__":
    main()
