'''
RUNNING THE PROGRAM
to run the program download the zip and open the folder in VS Code then run the python code. The other files are photos used in the application so make sure you click open folder in VS Code and not open file, to make sure you open evrything and allow the photos to load into the python.

OPERATING THE PROGRAM
this program will take inputs for
1. the amount of items
2. the measurment amount of units per single item (which is multiplied by amount of items to find the total amount of units)
3. The total price (price of all items if more than 1)
4. click the calculate button to find the cost per single unit of measure (amount x units / price = price per unit) then displays and saves the calculation in a history window
5. a button to clear the input boxes
6. a button the open the history window
7. a exit button the close the program

the history window
1. any previous calculations done, will be saved and displayed in a list here
2. A button the clear the history, deleting the list of previous calculations
3. A exit button the close the history window (it really just hides the window and it remains open. to allow the history to be modified easier)

EXAMPLE USUAGE
I want to know if a 12 pack of cans for my favorite soda is better value than 2, 2 liter bottles of the same soda. so first how many ounces are in a single unit of both product 
looking at the nutritional facts of a can of soda there are 12oz in a can. a 2 liter is 67.628. ill just use 67.6oz for this example since its close enough 

first ill check the price per unit of the cans 
1. so in the first text box for amount ill put 12 because there are 12 cans in the box
2. the next box is units per single item, there are 12oz of soda per can so here ill put 12
3. next ill enter the price of the 12 pack of cans. this is meant to be used while shopping but for this example ill google wallmart prices. a 12 pack of coke is 5.98 right now. so ill enter 5.98
4. now i will click calculate and the result is $0.04153 per unit

now to check the price of the 2 liters
ill click clear inputs to clear all the entry fields
1. i want to test against 2, 2 liters. so for amount ill enter 2
2. a 2 liter has 67.6oz. so for units per single item ill enter 67.6
3. now a google search shows 1, 2 liter cost 2.99 but we got 2 so we need to calculate the total price. which is 5.98
4. now i calculate and get 0.04423

now I will open the history window and see both calculations
I notice that the can cost less per unit, which is the goal of the program, so i but that option or continue to test other options
but out of curiousity lets also see if cheaper means we get less total oz's of soda.
this is something i needed to calculate by multiplying 12 cans x 12 oz to get 144 total oz's at 5.98
then 2, 2 liter bottles x 67.6 oz's to get a total of 135.2 total oz's at 5.98
so they cost the same but with the cans you get more oz's of soda and thats why the price per unit is lower.

'''
