#!/usr/bin/env python3
"""
Skid-Steering Kinematic Model
=============================

This script converts curvature (1/R) and linear velocity into 
left and right wheel speeds for a skid-steering or differential-drive robot.

Author: Camila C.
Date: 2025-10-18
"""

# ========================================
# Global constant: distance between wheels
# ========================================
WHEEL_BASE = 0.5  # [m] track width (distance between left and right wheels)


def compute_wheel_speeds(curvature, linear_speed=1.0):
    """
    Converts curvature (1/R) into left and right wheel speeds
    for a skid-steering robot.

    Parameters
    ----------
    curvature : float
        Path curvature (1/m). 
        Convention: 
            κ > 0 → turning right (clockwise)
            κ < 0 → turning left (counterclockwise)
            κ = 0 → straight motion
    linear_speed : float, optional
        Linear velocity of the robot’s center point [m/s].

    Returns
    -------
    tuple of float
        (left_wheel_speed, right_wheel_speed) in [m/s].
    """

    # Handle straight-line case to avoid floating-point artifacts
    if abs(curvature) < 1e-9:
        return linear_speed, linear_speed

    # Angular velocity [rad/s] = v * κ
    angular_speed = linear_speed * curvature

    # Compute left and right wheel speeds [m/s]
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
        print("Invalid input. Please enter numeric values. :(")
