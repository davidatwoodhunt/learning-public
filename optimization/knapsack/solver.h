#ifndef SOLVER_H
#define SOLVER_H
#include <vector>
using namespace std;
class Item{
    public:
        Item()=default;
        Item(int index,double value,double weight);
        int get_index();
        double get_value();
        double get_weight();
    private:
        int index;
        double value;
        double weight;
};

class TreeNode{
    public:
        TreeNode()=default;
        TreeNode(vector<Item> items,int index, double value,double weight);
        vector<Item> items;
        int index;
        double value;
        double weight;
};
#endif