
N = RootFrame()
A = Frame(N, [0, 0, 0], [0, 0, 1])

p = Point(A, [1, 0, 0])
p.linear_velocity(N, N)

#v = SpatialVelocity(AngularVelocity(N, N, [0, 0, 0]),
#                    LinearVelocity(N, N, [0, 1, 0]))
#
#v2 = 
