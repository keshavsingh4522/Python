/*
https://www.codechef.com/IARCSJUD/problems/CYCLEPER
*/

#include <bits/stdc++.h>
using namespace std;

// <-- Template code for utility -->
#define watch(x) cout << (#x) << " is " << (x) << endl
#define forl(i, b, e) for (i = b; i < e; i++)
#define fore(i, b, e) for (i = b; i <= e; i++)

void input_arr(vector<int> &arr, int n)
{
    int i;
    forl(i, 0, n)
    {
        int num;
        cin>>num;
        arr.push_back(num);
    }
}

template <typename T1, typename T2>
inline std::ostream &operator<<(std::ostream &os, const std::pair<T1, T2> &p)
{
    return os << "(" << p.first << ", " << p.second << ")";
}

template <typename T>
inline std::ostream &operator<<(std::ostream &os, const std::vector<T> &v)
{
    bool first = true;
    os << "[";
    for (unsigned int i = 0; i < v.size(); i++)
    {
        if (!first)
            os << ", ";
        os << v[i];
        first = false;
    }
    return os << "]";
}

template <typename T>
inline std::ostream &operator<<(std::ostream &os, const std::set<T> &v)
{
    bool first = true;
    os << "[";
    for (typename std::set<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
    {
        if (!first)
            os << ", ";
        os << *ii;
        first = false;
    }
    return os << "]";
}

template <typename T1, typename T2>
inline std::ostream &operator<<(std::ostream &os, const std::map<T1, T2> &v)
{
    bool first = true;
    os << "[";
    for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
    {
        if (!first)
            os << ", ";
        os << *ii;
        first = false;
    }
    return os << "]";
}

// <-- Main funtion -->
// This is where the actual program is

int main(int argc, char *argv[])
{
    // <-- Fast I/O -->
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t = 1;
    // <-- Multiple test cases -->
    // cin>>t;
    while (t--) {
        int n;
        cin>>n;
        vector<int> per;
        input_arr(per, n);

        vector<int> visited(n, 0);
        vector<vector<int>> res;
        int i, j;
        forl(i, 0, n) {
            if(visited[i] == 0) {
                vector<int> row;
                j = i;
                while(visited[j] == 0) {
                    row.push_back(j+1);
                    visited[j] = 1;
                    j = per[j]-1;
                }
                row.push_back(i+1);
                res.push_back(row);
            }
        }

        cout<<res.size()<<"\n";
        forl(i, 0, res.size()) {
            forl(j, 0, res[i].size()) {
                cout<<res[i][j]<<' ';
            }
            cout<<'\n';
        }
    }
    return 0;
}