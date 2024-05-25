import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sine_spacing(num_points=50):
    beta = np.linspace(0, np.pi/2, num_points)
    x = 1 - np.cos(beta)  # Sine spacing to cluster points at the leading edge
    return x

def naca4(m, p, t, num_points=50):
    a0, a1, a2, a3, a4 = 0.2969, -0.1260, -0.3516, 0.2843, -0.1015
    x = sine_spacing(num_points)
    yt = 5 * t * (a0 * np.sqrt(x) + a1 * x + a2 * x**2 + a3 * x**3 + a4 * x**4)
    yc = np.zeros_like(x)
    dyc_dx = np.zeros_like(x)
    
    theta = np.arctan(dyc_dx)

    xu = x - yt * np.sin(theta)
    yu = yc + yt * np.cos(theta)
    xl = x + yt * np.sin(theta)
    yl = yc - yt * np.cos(theta)

    # Ensure the profile converges to a single point at the trailing edge
    xu[-1], yu[-1] = 1, 0
    xl[-1], yl[-1] = 1, 0

    # Combine upper and lower surfaces, starting and ending at the trailing edge
    x_combined = np.concatenate([xu[::-1], xl[1:]])
    y_combined = np.concatenate([yu[::-1], yl[1:]])

    return x_combined, y_combined

def plot_airfoil(x, y, airfoil_name):
    plt.figure()
    plt.plot(x, y, label=f'{airfoil_name} Airfoil Profile')
    plt.scatter(x, y, color='red', s=10)  # Add points to the plot
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'NACA {airfoil_name} Airfoil')
    plt.legend()
    plt.show()

def save_to_dat(x, y, filename, airfoil_code):
    with open(filename, 'w') as f:
        f.write(f'NACA {airfoil_code}\n')
        for i in range(len(x)):
            f.write(f'{x[i]:.6f} {y[i]:.6f}\n')
    print(f'Coordinates saved to {filename}')

def main():
    folder_name = "airfoils"
    os.makedirs(folder_name, exist_ok=True)

    airfoil_code = input("Enter NACA 4-digit Airfoil Code: ")
    if len(airfoil_code) == 4:
        m = int(airfoil_code[0]) / 100
        p = int(airfoil_code[1]) / 10
        t = int(airfoil_code[2:]) / 100
        x, y = naca4(m, p, t)
    else:
        print("Invalid NACA code.")
        return
    
    plot_airfoil(x, y, airfoil_code)
    
    filename = os.path.join(folder_name, f"NACA_{airfoil_code}.dat")
    save_to_dat(x, y, filename, airfoil_code)

if __name__ == "__main__":
    main()
