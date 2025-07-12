# Mask Gold Point Card Plus CSV

Masks rows excluding target transaction row in Gold Point Card Plus CSV.

## Usage

```bash
docker compose run --rm mask-gold-point-card-plus-csv <file name> <exclude string from masking>
```

## Example

```bash
docker compose run --rm mask-gold-point-card-plus-csv 202506.csv ソフトバンクでんき
```
