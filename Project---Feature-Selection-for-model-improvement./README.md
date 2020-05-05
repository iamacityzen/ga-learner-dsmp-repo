### Project Overview

  Predict the forest cover type (the predominant kind of tree cover) from strictly cartographic variables (as opposed to remotely sensed data).
 It includes four wilderness areas located in the Roosevelt National Forest of northern Colorado. These areas represent forests with minimal human- 
 caused disturbances, so that existing forest cover types are more a result of ecological processes rather than forest management practices.

The study area includes four wilderness areas located in the Roosevelt National Forest of northern Colorado. Each observation is a 30m x 30m patch.
 Predict an integer classification for the forest cover type. The seven types are:

1 - Spruce/Fir 2 - Lodgepole Pine 3 - Ponderosa Pine 4 - Cottonwood/Willow 5 - Aspen 6 - Douglas-fir 7 - Krummholz


### Learnings from the project

 After completing this project, one will have a better understanding of how feature selection affects the performance of a machine learning model. In this project,  we will apply the following concepts.

How are the features important to our model.
How to select the most significant features out of many.
How to perform univariate feature selection.
How to perform a multivariate feature selection.


### Approach taken to solve the problem

 1. Data loading and observe the statistics using describe function.
2. Exploring the individual features via graphical methods and the visualizations to understand about each features.
3. Measured the correlation between continuos variables.
4.  Data preprocessing which involves careful observation at the data in hand and what modification needs to be done to get cleaner data.Rescaling  
     and standardization may be necessary for some algorithm to be applied on it.
5. Feature Selection using Select percentile.
6. Observe the effect of feature selection on model prediction.



