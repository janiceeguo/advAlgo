#include <iostream>
#include <random>

#define u128 __uint128_t
#define K 15

std::mt19937 engine(std::random_device{}());

u128 binPow(u128 a, u128 b, u128 m) {
	u128 r = 1;
	a %= m;
	while (b > 0) {
		if (b & 1) {
			r = (r * a) % m;
		}
		b >>= 1;
		a = (a * a) % m;
	}
	return r;
}

bool checkComposite(u128 n, u128 a, u128 s, u128 d) {
	u128 r = binPow(a, d, n);
	if (r == 1 || r == n - 1) return false;

	for (u128 i = 1; i < s; ++i) {
		r = binPow(r, 2, n);
		if (r == n - 1) return false;
	}

	return true;
}

bool isPrime(u128 n) {
	if (n < 4) return n == 2 || n == 3;

	u128 a, s = 0;
	u128 d = n - 1;
	while ((d & 1) == 0) {
		s++;
		d >>= 1;
	}

	std::uniform_int_distribution<u128> dist(2, n - 2);

	for (int i = 0; i < K; ++i) {
		a = dist(engine);
		if (checkComposite(n, a, s, d)) {
			return false;
		}
	}

	return true;
}

u128 fartcoinHash(std::string &s) {
	u128 h = 0;
	for (char c : s) {
		h <<= 1;
		h ^= c;
	}
	return h;
}

std::string u128_to_string(__uint128_t value) {
	if (value == 0) return "0";
	std::string result;
	while (value > 0) {
		result = char('0' + value % 10) + result;
		value /= 10;
	}
	return result;
}

int main(int argc, char *argv[]) {
	int n;
	std::cin >> n;
	int chainLength = 0;
	std::string chain = "fartcoin";

	std::string name, nonce, temp;
	u128 h;

	for (int i = 0; i < n; ++i) {
		std::cin >> name >> nonce;

		temp = chain + nonce;
		h = fartcoinHash(temp);
		std::cout << "Hash: " << u128_to_string(h) << std::endl;

		if (isPrime(h)) {
			chainLength++;
			chain = temp;
			std::cout << name << " accepted " << chainLength << std::endl;
		} else {
			std::cout << name << " rejected " << chainLength << std::endl;
		}
	}
	return 0;
}