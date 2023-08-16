# Warehouse_budget_Management_Using_Lagrangian_Relaxation
This is an inventory control model with budget constraints. The objective function minimizes total warehouse costs and the decision variables are the number of pieces per order for each product (Q_i). This algorithm first calculates Q_i via the Wilson formula and then calculates the total cost imposed by this order amount. if This cost exceeds the budget, it will calculate the optimal Q_i by forming its Lagrange function.
 
