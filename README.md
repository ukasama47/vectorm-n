# 行列演算関数

このリポジトリには、Pythonで行列の和と積を求めるための関数が含まれています。

## ファイルの概要

- `matrix_operations.py`: 行列演算の関数が定義されているPythonスクリプトです。
- `README.md`: この説明ファイルです。

## 関数の概要

### `m_sum(matrix1, matrix2)`
2つの同じサイズの行列を受け取り、それらの和を求めます。

#### 引数
- `matrix1`: 和を計算する行列の1つ目の要素。
- `matrix2`: 和を計算する行列の2つ目の要素。

#### 戻り値
和を表す新しい行列。

### `m_pow(matrix1, matrix2)`
2つの行列の積を求めます。

#### 引数
- `matrix1`: 行列の積の1つ目の行列。
- `matrix2`: 行列の積の2つ目の行列。

#### 戻り値
積を表す新しい行列。

## 使用方法

1. `matrix_operations.py`を自分のプロジェクトに取り込みます。
2. 適切な場所で関数をインポートして使用します。

```python
from matrix_operations import m_sum, m_pow

# 例: 行列の和の計算
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix2 = [
    [7, 8, 9],
    [10, 11, 12]
]
sum_matrix = m_sum(matrix1, matrix2)
print("行列の和:")
for row in sum_matrix:
    print(row)

# 例: 行列の積の計算
matrix3 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
prod_matrix = m_pow(matrix1,
