# Deliver
Create self-adjusting data structure and deliver packages

The Problem: The goal of this program is to deliver all 40 of the packages. The
constraints are that the trucks may not travel over 140 miles. The trucks travel 18mph.
Time delivering and loading the trucks are factored into the trucks travel speed. Each
truck may carry a total of 16 packages. Certain packages must meet a deadline. You
have 3 trucks and two drivers. A few packages will arrive at the hub late and some of
which will still have a deadline that must be met. One package has a wrong address and
the correct address will not be available until a certain time. The status of each package
must be available at all times

Pseudo Code:
shortest_path(graph, starting_vertex)
For current in all vertex
  Add to not-visited
  Set distance to infinity
Starting-vertex distance = 0

While not-visited ¬ empty
  smallest-index = 0
  
  For i ¬ length of not-visited
  next-index = start + 1
  Smallest-index-distance > next-index-distnace
  Smallest-index = next-index
  Current-vertex = not-visited at smallest
  Remove from not-visited
  
  For adjacent to graph[current-vertex]
  edge weight of current vertex and adjacent
  alternate path

  If alternate path < than adjacent
    Alternate is shortest distance

The programming environment used for this project:
OS - Linux X64 5.15.0-47-generic snap
Editor - Visual Studio Code
Version 1.72.0

Big O for the overall time complexity is O(V^2) - we are adding all vertices to not-visited and
setting their distance to infinity this comes out to O(V). Where V is the number of vertices in our
list. Next we call our method to get the edge weights between the current vertex and all of itsneighbors. Calling the method is O(1)-- constant time. A vertex will have at most V - 1 neighbors
so our time for this loops is O(1 * V) = O(V). An additional loop is used to find and compare the
shortest path which is O(V), however the time complexity over all is O(V^2) as we only have two
nested loops.

Big O for the space complexity is also O(V^2) as we have a V * V adjacency list and queue of
not visited vertices. One stores all of our current vertices while the other is keeping track of all
the vertices we have not visited.
Overall the program is O(V^3) as we compare the packages in the truck with a loop and nested
inside is the shortest path method which gives us O(V^2 * V).
The overall space complexity is also O(V^3). The shortest path method has a Big O of V^2 and
the loop that it is placed in has a space complexity of V.

Adding more packages is as simple as inputting the data. The overall complexity would not
change with more packages added. However N would increase. 

The software is easily accessible and broken up into different classes. We can make changes to
the project in one aspect without affecting the entire program. Dividing the project up into
classes helps when changes need to be accommodated.

Having a chaining hash table makes searching, inserting and deleting packages fast and
efficient with an O(1) with a unique id such as a package number. A set back with chaining is if
you do not know the package's unique id and you use another identifying feature searching
through the hash table becomes O(N^2). Where N is the number of packages.
