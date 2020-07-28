

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template <typename T>
void printArray(const vector<T>& x){
    // int n = x.size();
    for(T ele : x){
        cout<<ele<<endl;
    }

}
