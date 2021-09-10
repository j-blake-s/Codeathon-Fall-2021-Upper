#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <sstream>
#include <algorithm>

using namespace std;

const int MMAX = 8,
          NMAX = 1<<14,
          KMAX = 1<<20,
          STEPMAX = 1<<31-1,
          SCOREMAX = 1<<24;

int randRange(int minVal, int maxVal) {
    return minVal + rand() % max(maxVal - minVal, 1);
}

int getRand(int x, int numTests, int absMin, int absMax) {
    double base = pow(absMax - absMin, 1./numTests);
    int maxVal = min(absMin + (int)pow(base,x+1), absMax);
    int minVal = min(absMin + (int)pow(base,x), absMax);
    return randRange(minVal , maxVal);
}

string randFormula(int m) {
    int mask = randRange(1, 1<<m);  // Assumes m > 0
    stringstream s;
    int len = 0;

    for (int i = 0; i < m; i++) {
        if (mask % 2) {
            s.put('a' + i);
            len++;
        }
        mask /= 2;
    }
    char toShuffle[len+1];
    strcpy(toShuffle,s.str().c_str());
    random_shuffle(toShuffle, toShuffle+len);

    s.str("");
    s << toShuffle[0];
    for (int i = 1; i < len; i++) {
        s << "+" << toShuffle[i];
    }

    return s.str();
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        cerr << "Usage: testgen <i> <max test>" << endl;
        return 1;
    }
    int x = stoi(argv[1]);
    int numTests = stoi(argv[2])+1;

    srand(x);
    int m = randRange(min(x+1,MMAX), min(3*x+1,MMAX)+1);
    int n = getRand(x, numTests, 3, NMAX);
    int k = getRand(x, numTests, 1, KMAX);
    int maxStep = getRand(x, numTests, 4, STEPMAX);
    int maxScore = getRand(x, numTests, 10, SCOREMAX);

    cerr << "TEST " << x << ": m=" << m << ", n=" << n << ", k=" << k << ", maxStep=" << maxStep << ", maxScore=" << maxScore << endl;

    cout << n << " " << m << " " << k << endl;
    for (int i = 0; i < k; i++) {
        cout << randFormula(m) << " " << randRange(0, maxStep) << endl;
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (j != 0) cout << " ";
            cout << randRange(0, maxScore);
        }
        cout << endl;
    }
}