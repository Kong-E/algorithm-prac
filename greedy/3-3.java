package cote;

import java.util.Scanner;

public class Cote {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int M = sc.nextInt();
		int N = sc.nextInt();
		int[] arr = new int[M*N];
		
		for (int i=0; i<arr.length; i++) {
			arr[i] = sc.nextInt();
		}
		
		int[] minArr = new int[N];
		int min = arr[0];
		int minIdx = 0;
		for (int i=0; i<M*N; i++) {
			if (i % M != 0 && arr[i] < min) {
				min = arr[i];
				minArr[minIdx] = min;
			}
			if (i % M == 0 && i != 0) {
				minIdx++;
				min = arr[i];
				minArr[minIdx] = min;
			}
		}
		
		int max = minArr[0];
		for (int i=0; i<minArr.length; i++) {
			if (minArr[i]>max) {
				max = minArr[i];
			}
		}
		
		System.out.println(max);
		
	}
}
