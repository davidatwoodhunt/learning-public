#include "CbcModel.hpp"
#include "CoinModel.hpp"
// Using CLP as the solver
#include "OsiClpSolverInterface.hpp"
#include <CelModel.h>
#include <CelNumVar.h>
#include <CelIntVar.h>
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

int main(int argc, const char *argv[]){
    //read in file 
    string f_path = argv[1];
    cout << "Reading in Model from " << f_path << endl; 
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
    // maximize value subject to capacity constraints 
    printf("Initalizing model \n");
    OsiClpSolverInterface *solver = new OsiClpSolverInterface();
    celModel model(*solver);

    double* variableLowerbound = new double[num_items];
    double* variabelUpperBound = new double[num_items];
    char** variableNames = new char*[num_items];
    celNumVar* variables = new celNumVar[num_items];

    for(int i=0;i<num_items;i++){
        //binary choice 
        Item item = itemList[i];
        celNumVar item_var(item.get_index().to_string())
        variables[i] = item_var
    }
    //model.addVariables(num_items,variableLowerbound,variabelUpperBound,nullptr,variableNames);
    printf("Setting Objective \n");
    double* objectiveCoefficients = new double[num_items];
    for(int i=0; i < num_items;i++){
        Item item = itemList[i];
        objectiveCoefficients[i] =  variables[i] * item.get_value();
    }
    model.setObjective(objectiveCoefficients); // maximize
    printf("Setting Constraints");
    CoinPackedMatrix constraintMatrix;
    double* constraintLowerBound = new double[1];
    double* constraintUpperBound = new double[1];
    constraintLowerBound[0] = 0.0;
    constraintUpperBound[0] = capacity; // from 0 to cap
    constraintMatrix.appendRow(num_items, nullptr,nullptr); //initalize
    for(int i=0;i<num_items;i++){
        Item item = itemList[i];
        constraintMatrix.setElement(item.get_index(),0,item.get_weight());
        }
    model.addConstraint(1,&constraintLowerBound,&constraintUpperBound,nullptr,&constraintMatrix);
    
    printf("Solving");
    model.initialSolve();
    // Print the solution
    std::cout << "Objective value: " << model.getObjValue() << std::endl;
    const double* solution = model.getColSolution();
    for (int i = 0; i < num_items; i++) {
        std::cout << "Variable " << i << ": " << solution[i] << std::endl;
    }

}