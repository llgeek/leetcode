#
# Complete the 'find_intersections' function below.
#


def find_intersections(c_x, c_y, c_z, c_r,
                       ray_x, ray_y, ray_z, dir_x, dir_y, dir_z):
    """
    Args:
        c_x, c_y, c_z (float): coordinates of center point of the sphere.
        c_r (float): radius of the sphere.
        ray_x, ray_y, ray_z (float): coordinates of the origin of the ray.
        dir_x, dir_y, dir_z (float): direction vector of the ray.
    
    Returns:
        [] or list of floats
        
    """
    # Write your code here
    from math import sqrt
    a = dir_x ** 2 + dir_y**2 + dir_z ** 2
    b = 2 * dir_x * (ray_x-c_x) + 2 * dir_y * \
        (ray_y - c_y) + 2 * dir_z * (ray_z - c_z)
    c = (ray_x-c_x)**2 + (ray_y-c_y)**2 + (ray_z-c_z)**2 - c_r**2
    det = b**2 - 4*a*c
    if det < 0:
        return [0.0]
    t1 = (-b + sqrt(det)) / (2*a)
    t2 = (-b - sqrt(det)) / (2*a)
    ret = [sqrt((dir_x**2 + dir_y**2+dir_z**2) * t**2)
           for t in (t1, t2) if t >= 0]
    if not ret:
        ret.append(0.0)
    return sorted(ret)
