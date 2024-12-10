// aqui basicamente serao pair, min e max, swap e sort
#include <iostream>

using namespace std;

int main()
{
    pair<int,int> a = make_pair(1, 2); // a = {1, 2}
    pair<string,double> b = make_pair("Yan", 20.03); // b = {"Yan", 20.03}

    int c = a.first; // c = 1
    double d = b.second; // 20.03

    b.first = "New Yan";
    string e = b.first; // e = "New Yan"

    int a = 2, b = 5;
    int c = min(a, b); // c = 2
    int d = max(a, b); // d = 5

    string e = "Carol", f = "Bernardo";
    string g = min(e, f); // g = "Bernardo"
    string h = max(e, f); // h = "Carol"

    int a = 2, b = 5;
    swap(a, b); // a = 5, b = 2

    string c = "Carol", d = "Bernardo";
    swap(c, d); // c = "Bernardo", d = "Carol"

    int v[] = {4, 1, 3, 2};
    sort(v, v + 4); // v = {1, 2, 3, 4}

    double t[] = {1.4, 20.03, -1.4, -20.03, 23.03};
    sort(t, t + 5); // t = {-20.03, -1.4, 1.4, 20.03, 23.03}
}
