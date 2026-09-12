#include <stdio.h>

float knapsack(float v[], float w[], int n, int cap) {
    float profit = 0, ratio;
    
    for (int i = 0; i < n; i++) {
        ratio = v[i] / w[i];
        
        for (int j = i + 1; j < n; j++) {
            if (v[j] / w[j] > ratio) {
                float t = v[i]; v[i] = v[j]; v[j] = t;
                t = w[i]; w[i] = w[j]; w[j] = t;
                ratio = v[i] / w[i];
            }
        }
        
        if (w[i] <= cap) {
            profit += v[i];
            cap -= w[i];
        } else {
            profit += ratio * cap;
            break;
        }
    }
    return profit;
}

int main() {
    float v[] = {60, 100, 120};
    float w[] = {10, 20, 30};
    int n = 3, cap = 50;

    printf("Maximum Profit = %.2f", knapsack(v, w, n, cap));
    return 0;
}
