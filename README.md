# Clusters of Things 
In this project, a model is created for generating simulations associated to groups and groups inside groups using pointers to generate a datafield and assign specific rules defined as functions and properties to the points in the datafields. An element 'e' containing sub elements 'e<sub>1</sub>, e<sub>2</sub>, and e<sub>3</sub>', for example, would adapt the following structure in this model: 

![](01.png)

Where the numbers before the arrows are the pointer numbers. Each data except the state and function have two pointers and follow the same rule as 'e'. As we assume that 'e' is a point on a larger datafield, we also assume that its 0th pointer either points to another individual element in the larger datafield, or if its the last point, to 'None'. 
