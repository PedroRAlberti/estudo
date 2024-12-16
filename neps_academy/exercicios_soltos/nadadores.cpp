#include <iostream>
#include <queue> 

using namespace std;

int main() {

    int A,B,C;

    cin >> A >> B >> C;

    priority_queue <pair<int,int> , vector <pair<int,int>> , greater<pair<int,int>> > pq;

    pq.push({A,1});
    pq.push({B,2});
    pq.push({C,3});
    
    for (int i = 0; i < 3; i ++){
        cout << pq.top().second << endl;
        pq.pop();
    }

    return 0;
}