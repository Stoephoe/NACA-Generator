# NACA Airfoil Generator

This Python script generates 4-digit NACA airfoils, visualizes them, and saves the airfoil coordinates to `.dat` files. The airfoil profiles start and end at the trailing edge to ensure compatibility with Fusion 360.

## Features

- Generates 4-digit symmetric NACA airfoils
- Uses sine spacing for higher point density at the leading edge
- Ensures profiles converge to a single point at the trailing edge
- Visualizes the airfoil profile using Matplotlib
- Saves the airfoil coordinates in `.dat` files in a specified folder

## Prerequisites

- Python 3.x
- NumPy
- Pandas
- Matplotlib

You can install the required Python packages using pip:

```sh
pip install numpy pandas matplotlib
```

## Usage

1. **Clone the repository:**

```sh
git clone https://github.com/Stoephoe/naca-airfoil-generator.git
cd naca-airfoil-generator
```

2. **Run the script:**

```sh
python naca_airfoil_generator.py
```

3. **Input the NACA 4-digit airfoil code:**

   - The script will prompt you to enter a 4-digit NACA airfoil code (e.g., `0016`).

4. **View the airfoil plot:**

   - The script will display a plot of the generated airfoil.

5. **Find the generated `.dat` file:**

   - The airfoil coordinates will be saved in a `.dat` file in the `airfoils` folder within the project directory.

## Example

```sh
Enter NACA 4-digit Airfoil Code: 0016
```

The script will generate the NACA 0016 airfoil, display a plot, and save the coordinates to `airfoils/NACA_0016.dat`.

## Project Structure

```
naca-airfoil-generator/
│
├── airfoils/               # Folder where the generated .dat files are saved
│
├── naca_airfoil_generator.py  # Main script to generate and visualize NACA airfoils
│
├── README.md               # Project README file
│
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify the sections as per your project details and preferences.
