package math;

import java.io.*;
import java.util.*;

public class 소수구하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        ArrayList<Integer> primes = new ArrayList<>();

        for (int i=n; i<=m; i++) {
            if (is_prime(i)) primes.add(i);
        }

        for (int prime : primes) {
            System.out.println(prime);
        }
    }

    public static boolean is_prime(int number) {
        if (number == 1) return false;

        for (int i=2; i<=Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}