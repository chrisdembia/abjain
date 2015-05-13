class RootFrame(object):
    def __init__(self):

class Frame(object):
    def __init__(self, parent, origin, orientation):

class Vector(object):
    def __init__(self, eframe, x, y, z):
        self.value = np.matrix([x, y, z]).T
        self.eframe = eframe
    def cross(self, other):
        assert len(other) == 3
        return np.matrix([self.value[1] * other[2] - self.value[2] * other[1],
                          self.value[2] * other[0] - self.value[0] * other[2],
                          self.value[0] * other[1] - self.value[1] * other[0]).T

class Point(object):
    def __init__(self, eframe, x, y, z):
        self.eframe = eframe
        self.x = x
        self.y = y
        self.z = z
    def linear_velocity(self, dframe, eframe):

class SpatialVelocity(object):
    def __init__(self):
        
class RigidBodyTransformationMatrix(object):
    def __init__(self, frame_x, frame_y):
        self.frame_x = frame_x
        self.frame_y = frame_y
        self.r_YoXo = self.frame_y.origin - self.frame_x.origin
    def __mul__(self, other):
        result = np.empty((6, other.shape[1]))

        for icol in range(other.shape[1]):
            result[0:3, icol] = (other[0:3, icol] +
                    self.r_YoXo.cross(other[3:, icol]))
            result[3:, icol] = other[3:, icol]
        return result
    def transpose(self):
        return RigidBodyTransformationMatrixTranspose(frame_x, frame_y)

class RigidBodyTransformationMatrixTranspose(object):
    def __init__(self, frame_x, frame_y):
        self.frame_x = frame_x
        self.frame_y = frame_y

