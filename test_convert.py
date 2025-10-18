# Global constant for the distance between the wheels (track width)
WHEEL_BASE = 0.5  # meters

def compute_wheel_speeds(curvature, linear_speed=1.0):
    """
    Converts curvature (1/R) into left and right wheel speeds
    for a skid-steering robot.

    Parameters:
        curvature (float): 1 / turning radius (1/m)
        linear_speed (float): Linear speed of the robot (m/s)

    Returns:
        tuple: (left_wheel_speed, right_wheel_speed)
    """
    # Angular velocity = v * curvature
    angular_speed = linear_speed * curvature

    # Wheel speeds
    left_speed = linear_speed - (angular_speed * WHEEL_BASE / 2)
    right_speed = linear_speed + (angular_speed * WHEEL_BASE / 2)

    return left_speed, right_speed


# ==============================
# Example usage with user input
# ==============================

if __name__ == "__main__":
    try:
        kappa = float(input("Enter curvature (1/R, in 1/m): "))
        v = float(input("Enter the robot's linear speed (m/s): "))

        left, right = compute_wheel_speeds(kappa, v)

        print(f"\nLeft wheel speed:  {left:.3f} m/s")
        print(f"Right wheel speed: {right:.3f} m/s")
        print(f"(Wheel base used: {WHEEL_BASE} m)")

    except ValueError:
        print("⚠️ Invalid input. Please enter numeric values.")
#OBS
#κ>0→turning right
#κ<0→turning left
#κ<0→turning left
#κ=0→straight motion
