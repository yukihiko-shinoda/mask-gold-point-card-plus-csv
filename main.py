"""Masks rows excluding target transaction row in Gold Point Card Plus CSV."""

import csv
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import _csv  # noqa: F401,RUF100


def mask(line: list[str]) -> list[str]:
    """Mask second and seventh (if not empty) columns in the line."""
    masked_line = line.copy()
    masked_line[1] = "****"
    if masked_line[6]:
        masked_line[6] = "****"
    return masked_line


class MaskingGoldPointCardPlusCSV:
    """Masks rows excluding target transaction row in Gold Point Card Plus CSV."""

    def __init__(self, input_file_name: Path, used_store_to_exclude: str) -> None:
        self.input_file_name = input_file_name
        self.used_store_to_exclude = used_store_to_exclude
        self.output_file_name = Path(str(self.input_file_name).replace(".csv", "_masked.csv"))

    def write_masked(self) -> None:
        with self.output_file_name.open("w", encoding="shift_jis_2004") as file:
            self._write_masked(csv.writer(file))

    def _write_masked(self, writer: "_csv._writer") -> None:
        with self.input_file_name.open("r", encoding="shift_jis_2004") as file:
            self.__write_masked(writer, iter(csv.reader(file)))

    def __write_masked(self, writer: "_csv._writer", lines: Iterator[list[str]]) -> None:
        # Copy the raw header line
        writer.writerow(next(lines))
        for line in lines:
            if self.used_store_to_exclude in line:
                writer.writerow(line)
                continue
            writer.writerow(mask(line))


def main() -> None:
    input_file_name = Path(sys.argv[1])
    used_store_to_exclude = sys.argv[2]
    MaskingGoldPointCardPlusCSV(input_file_name, used_store_to_exclude).write_masked()


if __name__ == "__main__":
    main()
