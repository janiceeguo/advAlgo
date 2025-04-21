import java.util.Random;
import java.util.Scanner;

public class FartCoin {
    
    // Fast modular exponentiation (equivalent to binpow in Python)
    public static long binpow(long a, long b, long m) {
        long r = 1;
        a %= m;
        while (b > 0) {
            if ((b & 1) == 1) {
                r = (r * a) % m;
            }
            b >>= 1;
            a = (a * a) % m;
        }
        return r;
    }
    
    // Check if a number is composite (part of Miller-Rabin test)
    public static boolean checkComposite(long n, long a, long d, int s) {
        long r = binpow(a, d, n);
        if (r == 1 || r == n - 1) {
            return false;
        }
        
        for (int i = 0; i < s - 1; i++) {
            r = (r * r) % n;
            if (r == n - 1) {
                return false;
            }
        }
        return true;
    }
    
    // Miller-Rabin primality test
    public static boolean isPrime(long n, int k) {
        if (n < 4) {
            return n == 2 || n == 3;
        }
        
        int s = 0;
        long d = n - 1;
        while ((d & 1) == 0) {
            d >>= 1;
            s++;
        }
        
        Random rand = new Random();
        for (int i = 0; i < k; i++) {
            long a = 2 + rand.nextInt((int)(n - 3));  // Random in range [2, n-2]
            if (checkComposite(n, a, d, s)) {
                return false;
            }
        }
        return true;
    }
    
    // Overload isPrime to use default k=5
    public static boolean isPrime(long n) {
        return isPrime(n, 5);
    }
    
    // Custom hash function for FartCoin
    public static long fartcoinHash(String s) {
        long h = 0;
        for (char c : s.toCharArray()) {
            h = h << 1;
            h = h ^ (long)c;
        }
        return h;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        
        String blockchain = "fartcoin";
        int acceptedCount = 0;
        
        for (int i = 0; i < n; i++) {
            String line = scanner.nextLine().trim();
            if (line.isEmpty()) {
                continue;
            }
            
            String[] parts = line.split("\\s+", 2);
            String username = parts[0];
            String nonce = parts.length > 1 ? parts[1] : "";
            
            if (nonce.length() < 5) {
                System.out.println(username + " rejected " + acceptedCount);
                continue;
            }
            
            String newBlockchain = blockchain + nonce;
            long h = fartcoinHash(newBlockchain);
            
            if (isPrime(h)) {
                acceptedCount++;
                blockchain = newBlockchain;
                System.out.println(username + " accepted " + acceptedCount);
            } else {
                System.out.println(username + " rejected " + acceptedCount);
            }
        }
        
        scanner.close();
    }
}
