import math


points = [[2.0, 0.0, -0.2],[3.5, 1.0, -0.3],[1.5, -0.8, -0.1]]


tx = 0.5
ty = 0.0
tz = 0.2


theta = -15

theta = math.radians(theta)


sin_theta = math.sin(theta)
cos_theta = math.cos(theta)

print("--- Transformed Obstacles (Base Frame) ---")

for i, point in enumerate(points, start=1):

    x, y, z = point

    
    x_rot = x * cos_theta + z * sin_theta
    y_rot = y
    z_rot = -x * sin_theta + z * cos_theta

    x_base = x_rot + tx
    y_base = y_rot + ty
    z_base = z_rot + tz

    print(
        f"Obstacle {i}: "
        f"[{x_base:.2f}, {y_base:.1f}, {z_base:.2f}]"
    )