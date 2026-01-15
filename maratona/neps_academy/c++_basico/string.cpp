#include <iostream>

using namespace std;

int main()
{
    string A = "Arnaldo";
    string B = "Bernaldo";

    bool tmp = (A < B); // tmp = true, pois, lexicograficamente, A é menor que B

    A = "BernaldoGreater";

    tmp = (A < B); // tmp = false, pois B é um prefixo de A

    A = "Bernaldo";

    tmp = (B > A); // tmp = false, pois A é igual a B
    tmp = (A == B); // tmp = true, pois A é exatamente igual a B
    tmp = (B >= A); // tmp = true, pois A é igual a B, logo maior ou igual também

    int sizeA = A.size(); // sizeA = 7
    int sizeB = B.size(); // sizeB = 8

    A.clear(); // A = ""
}
