package cote;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Cote {

	public static void main(String[] args) {
		// 배열 크기 N, M번 더하여 가장 큰 수, 특정한 인덱스의 수는 K번까지만 더함
        Scanner sc = new Scanner(System.in);
        System.out.println("3개의 자연수(N, M, K)를 입력하세요.");
        int N = sc.nextInt();
        int M = sc.nextInt();
        int K = sc.nextInt();

        sc.nextLine();
        
        System.out.println("N개의 자연수를 입력하세요.(Space로 구분)");
        Integer[] intArr = new Integer[N];
        for (int i = 0; i < N; i++) {
            intArr[i] = sc.nextInt();
        }
        
        sc.close();
        
        Arrays.sort(intArr, Collections.reverseOrder());
        
        int sum=0;
        int count=0;

        int current = intArr[0];
        for (int i=0; i<M; i++) {
        	sum += current;
        	count += 1;
        	if( count == K ) current = intArr[1];
        	if( count == K+1) {
        		current = intArr[0];
        		count = 0;
        	}
        }
        
        System.out.println("sum = " + sum);
	}
}


