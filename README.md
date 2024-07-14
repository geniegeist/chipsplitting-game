# Chipsplitting Games

A library for computing chip-splitting games as defined in [Classifying one-dimensional discrete models with maximum likelihood degree one](https://arxiv.org/abs/2205.09547) by Arthur Bik and Orlando Marigliano.

Work in progress...

## Progress

- Proof for n=4 ✅
- Proof for n=5 ✅
- Validate results of section 8 ✅
- Extend table in section 8 (n=6) ✅

## Number of fundamental models

```
| n \ d   |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |  11  |
| ------- | ----------------------------------------------------------------- |
| 1       |  1  |     |     |     |     |     |     |     |     |      |      |
| 2       |     |  3  |  1  |     |     |     |     |     |     |      |      |
| 3       |     |     | 12  |  4  |  2  |     |     |     |     |      |      |
| 4       |     |     |     | 82  | 38  |  10 |  4  |     |     |      |      |
| 5       |     |     |     |     | 602 | 254 |  88 |  24 |  2  |      |      |
| 6       |     |     |     |     |     | 6710| 2421| 643 | 198 |  32  |  4   |
```
