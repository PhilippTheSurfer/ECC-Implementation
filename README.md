# ECC Operations

This code implements mathematical operations on a valid Elliptic Curve.
__________________

The code defines two classes EllipticCurve and Point. The EllipticCurve class has three instance variables a, b, and p, which represent the parameters of a given elliptic curve. The class has two methods. The first method, calculatesPointsOnElipticcurve, calculates all the points on the curve and returns a list of tuples. The second method, givesOrderOfEllipticcurve, calculates the order of the curve, which is the number of points on the curve.
__________________

The Point class has two instance variables x and y, which represent a point on the curve. The class has two methods. The first method, checksIfPointOnCurve, checks if the given point lies on the elliptic curve. The second method, calculatesOrderOfPoint, is not implemented and is incomplete.
__________________

The code also defines four functions definesOperationToDo, addThePoint, doubleThePoint, and advencedEuclidAlgorithm. The definesOperationToDo function checks if two points are the same. The addThePoint function adds two points on the elliptic curve and returns the result as a tuple. The doubleThePoint function doubles a given point on the elliptic curve and returns the result as a tuple. The advencedEuclidAlgorithm function calculates the inverse of a given number using the advanced Euclidean algorithm.
__________________

Note that the code is incomplete and has some errors. For example, the calculatesOrderOfPoint method of the Point class is incomplete. The addThePoint and doubleThePoint functions have print statements inside them, which may not be desirable in a production setting. The definesOperationToDo function has a typo in its name (ToDo should be toDo). Finally, there are some unused variables and comments in the code that should be removed.