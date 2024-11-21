// solver implemented in cpp, rehash of branch and bound, to compare speed and see if ic an get syntax
#include <vector>
#include <queue>
#include "solver.h"
#include <iostream>
#include <fstream>
#include <sstream> 

using namespace std;

Item::Item(int index,double value,double weight){
    this->index = index;
    this->value = value;
    this->weight = weight;
}
int Item::get_index(){
    return index;
}
double Item::get_value(){
    return value;
}
double Item::get_weight(){
    return weight;
}

TreeNode::TreeNode(vector<Item>items ,int index ,double value ,double weight){
    this->items = items;
    this->index = index;
    this->value = value;
    this->weight = weight;
};
class linRelaxSolver{
    int capacity;
    vector<Item> items;
    double bestEst;
    vector<Item> solution;
    queue<TreeNode> node_queue;
    public:
        linRelaxSolver(int capacity,vector<Item> items){
            this->capacity=capacity;
            this->items = items;
            node_queue.push(TreeNode(vector<Item>(),0,0,0));
        };
        void format_solution(){
            vector<int> solution_formatted(items.size(),0); //init zeros

            for(int i=0;i<solution.size();i++){
                int index = solution[i].get_index();
                solution_formatted.insert(solution_formatted.begin() + index,1);
            };
            solution_formatted.resize(items.size());
            cout << bestEst << " " << 1 << endl;
            for(int i=0;i<solution_formatted.size();i++){
                cout << solution_formatted[i] << " ";
            }
            cout << endl;
        }
        double compute_bound(TreeNode node){
            double remaining_capacity = capacity - node.weight;
            double bound = node.value;

            for(int i=node.index; i < node.items.size(); i++){
                Item item = node.items[i];
                if (item.get_weight() <= remaining_capacity){
                    bound += item.get_value();
                    remaining_capacity -= item.get_weight();
                } else{
                    double frac = remaining_capacity / item.get_weight();
                    bound += frac * item.get_value();
                    break;
                }
            }
            return bound;
        };
        void branch_and_bound_search(){
            TreeNode bestNode;
            while(not node_queue.empty()){
                
                TreeNode node = node_queue.front();
                //cout << "Current Node:" << node.index <<" | "<<node.value << endl;
                if(node.index == items.size()){
                    // leaf node
                    if(node.value > bestEst){
                        //cout << bestEst << endl;
                        this->bestEst = node.value;
                        solution = node.items;
                    }
                }
                else{
                    Item item = items[node.index];
                    vector<Item> sub_item = node.items;
                    sub_item.push_back(item);
                    TreeNode include = TreeNode(
                        sub_item,
                        node.index +1,
                        node.value + item.get_value(),
                        node.weight + item.get_weight()
                    );
                    if(include.weight <= capacity and include.value + compute_bound(include) >= bestEst){
                        //cout << "pushing include" << endl;
                        node_queue.push(include);
                    }
                    TreeNode exclude = TreeNode(
                        node.items,
                        node.index + 1,
                        node.value,
                        node.weight
                    );
                    if(exclude.weight <= capacity and exclude.value + compute_bound(exclude) >= bestEst){
                        node_queue.push(exclude);
                        //cout << "pushing exclude" << endl;
                    }
                }
                node_queue.pop();
                
                //cout << "Popping " << node_queue.front().index <<endl;
            }
        }
};

linRelaxSolver read_file(std::string const &f_path){
    ifstream file(f_path);
    string line;
    int capacity;
    int num_items;
    const char delim = ' '; 
    bool firstLine = true;
    vector<Item> itemList;
    int index = 0;
    while(getline(file,line)){
        stringstream ss(line);
        string s;
        bool firstChar = true;

        int value;
        int weight;
        while(getline(ss,s,delim)){
            if(firstLine){
                if(firstChar){
                    //number of items
                    num_items = stoi(s);
                    itemList.resize(num_items);
                    firstChar = false;
                }else{
                    capacity = stoi(s);
                }
            }else{
                if(firstChar){
                    value = stoi(s);
                    firstChar = false;
                }else{
                    weight = stoi(s);
                }
            }     
        }
        if(!firstLine){
            Item item = Item(index,value,weight);
            itemList.insert(itemList.begin() + index,item);
            index++;
            }
        else{firstLine = false; // now start tiems
        }


        
    }
    file.close();
    itemList.resize(num_items);

    //display items
    //cout <<" entered items " << endl;
    //for(int i=0;i< itemList.size();i++){
    //    Item item = itemList[i];
    //    cout << item.get_index() << " | " << item.get_value() << " | " << item.get_weight() << endl;
    // }
    return linRelaxSolver(capacity,itemList);
};

int main(int argc, char *argv[]){
    //vector<Item> items{Item(0,8,4),Item(1,10,5),Item(2,15,8),Item(3,4,3)};
    cout << "entered file path " << argv[1] << endl;
    linRelaxSolver solver = read_file(argv[1]);
    solver.branch_and_bound_search();
    solver.format_solution();
        
};