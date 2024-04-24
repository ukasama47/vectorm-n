#1211201118 林優花

# m行n列の二つの行列の和を求める関数
def m_sum(matrix1, matrix2):
    m = len(matrix1)  # 行数
    n = len(matrix1[0])  # 列数

    # 和を計算する
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            sum_ij = matrix1[i][j] + matrix2[i][j]
            row.append(sum_ij)
        result.append(row)
    return result

# m行n列の行列とn行m列の行列の積を求める関数
def m_pow(matrix1, matrix2):
    m = len(matrix1)  # 行数
    n = len(matrix2[0])  # 列数
    p = len(matrix1[0])  

    # 積を計算する
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            pow_ij = 0
            for k in range(p):
                pow_ij += matrix1[i][k] * matrix2[k][j]
            row.append(pow_ij)
        result.append(row)
    return result

# 確認用スクリプト
if __name__ == '__main__':
    # 2行3列の行列A
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    # 2行3列の行列B
    matrix2 = [
        [7, 8, 9],
        [10, 11, 12]
    ]

    # 行列の和の計算と出力
    sum_matrix = m_sum(matrix1, matrix2)
    print("行列の和:")
    for row in sum_matrix:
        print(row)

    # 3行2列の行列C
    matrix3 = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    # 行列の積の計算と出力
    prod_matrix = m_pow(matrix1, matrix3)
    print("行列の積:")
    for row in prod_matrix:
        print(row)
