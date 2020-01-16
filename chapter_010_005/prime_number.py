"""
Name: prime_number.py
Description: 素数を計算する script
Created by: Masato Shima
Created on: 2020/01/15
"""

# **************************************************
# ----- Import Library
# **************************************************
import os
import math

import numpy as np

np.set_printoptions(threshold=10)


# **************************************************
# ----- Function main
# **************************************************
def main() -> None:
	# 環境変数より素数の計算範囲を受け取る
	n_start = eval(os.environ["A_START_NUM"])
	n_size = eval(os.environ["A_SIZE_NUM"])
	n_end = n_start + n_size
	array = np.arange(n_start, n_end)

	# 素数判定の関数を vector 化
	pvec = np.vectorize(is_prime)

	# 配列要素へ適用して, 判定表を作成
	primes_tf = pvec(array)

	# 素数だけを抽出
	primes = np.extract(primes_tf, array)
	print(primes)

	return


# **************************************************
# ----- Function is_prime
# **************************************************
def is_prime(n: int) -> bool:
	if n % 2 == 0 and n > 2:
		return False

	check = all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

	return check


# **************************************************
# ----- Main
# **************************************************
if __name__ == '__main__':
	os.chdir(os.path.dirname(os.path.abspath(__file__)))

	# For TEST
	# os.environ["A_START_NUM"] = "1"
	# os.environ["A_SIZE_NUM"] = "10"

	main()


# **************************************************
# ----- End
# **************************************************
