function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1.0;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%
min_prediction_mean = 1000.0;
test_values = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
for C_val = test_values
  for sigma_val = test_values
    model= svmTrain(X, y, C_val, @(x1, x2) gaussianKernel(x1, x2, sigma_val)); 
    yp = svmPredict(model,Xval);
    prediction_mean = mean(double(yp ~= yval));
    %printf ("This iteration %f   %f  min %f  current %f\n",C_val, sigma_val, min_prediction_mean, prediction_mean);
    if (prediction_mean < min_prediction_mean)
      printf ("Found MINIMUM HURRAY /n");
      min_prediction_mean = prediction_mean;
      printf ("New optimum points ==>  C: %f  sigma: %f  predicted %f\n",C_val, sigma_val, min_prediction_mean);
      C = C_val;
      sigma = sigma_val;
    end

  end
end

printf ("Predicted values %f   %f  %f\n",C, sigma,min_prediction_mean);



% =========================================================================

end
