#helper function to split a tree into branches
#(takes 3 parameters the index that you're currently splitting on, the value that you're splitting on, and the dataset)
    #set up two lists called left_branches and right_branches
    #loop through each row in the dataset
        #if it is above the split value append it to the right
        #if its lower then append it to the left
    #after the loop return the lists of branches

def split_tree_in_two(column_index, value, dataset):
	left_branches, right_branches = list(), list()
	for row in dataset:
		if row[column_index] < value:
			left_branches.append(row)
		else:
			right_branches.append(row)
	return left_branches, right_branches

#helper function to calculate gini impurity
#we're going to call this function recursively until we have classified everything
#takes in two parameters, a list containing the leftgroups and rightgroups, and the prediction_column_values
    #counts the rows in each group of branches and stores it in a varaible called number_of_rows
    #we start with gini at zero
    #we loop through the two groups of branches
        #if either group has a length of zero skip forward one iteration
        #set a variable to track score
        #loop through the list of prediction_column_values
            #get the proportion of rows with the current prediction value
            #square it and add it to the score
        #done looping through the prediction_column_values and we have a score
        #finish adjusting gini coefficient
        #gini += (1.0 - score) * (size /number_of_rows)
    #done looping through all the groups of branches, return gini coefficient
def find_gini_index(groups_of_branches, prediction_column_values):
    number_of_rows = float(sum([len(group) for group in groups_of_branches]))
    gini = 0.0
    for group in groups_of_branches:
        number_of_columns = float(len(group))
        if number_of_columns == 0:
            continue
        score = 0.0
        for prediction_value in prediction_column_values:
            proportion = [row[-1] for row in group].count(prediction_value) / number_of_columns
            score += proportion * proportion
        gini += (1.0 - score) * (number_of_columns / number_of_rows)
    return gini

#helper function to loop through a dataset and find the best split
#takes in one parameter of a dataset
    #set prediction_column_values to be the last column of the dataset
    #set return values to be extremely high
    #loop through each column in the dataset
        #loop through each row in the dataset
            #set groups_of_rows to be a list containing the result of calling split_tree_in_two on the column number and the value of the column in the row you're on
            #set the gini coeffiecient to be the result of calling the gini function on the groups of rows and prediction_column_values
            #if the gini coefficient is lower than the result values than override the result values
     #once you've checked every column, return the column_index, the value, and the groups_of_branches for the optimal split in a hashmap

def get_the_best_split(dataset):
	prediction_column_values = list(set(row[-1] for row in dataset))
	res_index, res_value, res_gini, res_groups = 999, 999, 999, None
	for column_index in range(len(dataset[0])-1):
		for row in dataset:
			groups = split_tree_in_two(column_index, row[column_index], dataset)
			gini = find_gini_index(groups, prediction_column_values)
			if gini < res_gini:
				res_index, res_value, res_gini, res_groups =column_index, row[column_index], gini, groups
	return {'index':res_index, 'value':res_value, 'groups':res_groups}

#a terminal node value must be a valid final prediction. Because we are pruning both before and after we will sometimes have to set the values of our terminal nodes manually
#a helper function that counts all of the remaining prediction_column_values and returns the mode
def eat_group_poop_terminal_node_value(group):
    possible_terminal_node_values = [row[-1] for row in group]
    return max(set(possible_terminal_node_values), key=possible_terminal_node_values.count)

#a helper function that either splits the branch recursively or feeds it to the terminal function
#

#a helper function that builds a decision tree and returns the root node
#takes in three parameters, the dataset, the maximum depth, and the minimum number of samples for a branch to split on




########The Jupyter Notebook Starts Here

#Imports sci-kit-learn's decision tree, data, numpy, my deccision tree, and any helper functions
#import sk-learn.metrics accuracy_score

#Builds the skl decision tree and wires it up to the data

#builds up my decision tree and wires it up to the data

#runs evaluator functions on both trees and shows data