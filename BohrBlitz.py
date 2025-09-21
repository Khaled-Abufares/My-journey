#~~~Magic~~~~#
import numpy as np
import matplotlib.pyplot as plt
import warnings
import pandas as pd
import matplotlib.animation as animation
#~~~~~~~Periodic Table Data~~~~~~~#
periodic_table_data = {
    'Z': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    'Symbol': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn'],
    'Name': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin']
}
periodic_df = pd.DataFrame(periodic_table_data)
#~~~~~~~Element Class~~~~~~~#
class Element:
#~~~~~~~Constructor~~~~~~~#
    def __init__(self, Z, A=None, name=None):
        self.Z = Z
        self.A = A
        self.name = name
        self.protons = Z
        self.neutrons = A - Z if A is not None else round(1.3 * Z) 
        self.electrons = Z
        self.mass = A if A is not None else self.Z + self.neutrons if self.neutrons is not None else self.Z 
        self.shells = self.calculate_shells()
#~~~~~~~Calculate Shells~~~~~~~#
    def calculate_shells(self):
        shells = []
        electrons_left = self.electrons
        n = 1
        if self.electrons is None:
            return None
        elif self.electrons < 0:
            raise ValueError("Number of electrons cannot be negative")
        elif self.electrons == 0:
            warnings.warn("Element must have at least one electron")
            return []        
        else:
            while electrons_left > 0:
                capacity = 2 * (n**2)
                in_this_shell = min(capacity, electrons_left)
                shells.append(in_this_shell)
                electrons_left -= in_this_shell
                n += 1
            return shells
#~~~~~~~Get Shells String~~~~~~~#
    def get_shells_str(self):
        if self.shells:
            return "/".join(str(x) for x in self.shells)
        return "No electrons"
#~~~~~~~Draw Bohr Model Animated~~~~~~~#
    def draw_bohr_model_animated(self):
        if self.shells is None:
            raise ValueError("Cannot draw Bohr model without electron configuration")
        fig, ax = plt.subplots(figsize=(8, 8))
        orbit_gap = 1.5
        max_radius = (len(self.shells)+2) * orbit_gap
        plt.xlim(-max_radius, max_radius)
        plt.ylim(-max_radius, max_radius)
        nucleus_radius = 0.2 * np.cbrt(self.A or self.Z)
        nucleus = plt.Circle((0, 0), nucleus_radius, color='lightgrey', alpha=0.5)
        ax.add_artist(nucleus)
        shell_radii = []
        for i, e_count in enumerate(self.shells):
            r = (i + 1) * orbit_gap
            shell_radii.append(r)
            ax.add_artist(plt.Circle((0, 0), r, color='black', fill=False, linestyle='dashed'))
        electrons = []
        electrons_speeds = []
        for i, e_count in enumerate(self.shells):
            r = shell_radii[i]
            angles = np.linspace(0, 2 * np.pi, e_count, endpoint=False)
            for angle in angles:
                x = r * np.cos(angle)
                y = r * np.sin(angle)
                electron_size = max(0.05, 0.2 - 0.002*self.Z)
                electron = plt.Circle((x, y), electron_size, color='#7DF9FF', alpha=0.9)
                ax.add_artist(electron)
                electrons.append((electron, r, angle))
                electrons_speeds.append(0.05/(i+1))       
        protons = self.protons
        neutrons = self.neutrons if self.neutrons is not None else self.protons
        for i in range(protons):
          r = np.random.uniform(0, nucleus_radius * 0.8)
          theta = np.random.uniform(0, 2*np.pi)
          x, y = r*np.cos(theta), r*np.sin(theta)
          ax.add_artist(plt.Circle((x, y), 0.07, color='red'))  
        for i in range(neutrons):
         r = np.random.uniform(0, nucleus_radius * 0.8)
         theta = np.random.uniform(0, 2*np.pi)
         x, y = r*np.cos(theta), r*np.sin(theta)
         ax.add_artist(plt.Circle((x, y), 0.07, color='blue'))    
        ax.text(0, nucleus_radius+0.5, f'Protons: {protons}\nNeutrons: {neutrons}', 
        ha='center', va='center', fontsize=10, color='black')
        ax.text(0, -nucleus_radius-0.5, f'Z={self.Z}\nA={self.A or (self.Z + neutrons)}', 
        ha='center', va='center', fontsize=10, color='black')
        def update(frame):
          for j, (electron, r, angle) in enumerate(electrons):
            new_angle = angle + frame * electrons_speeds[j]
            x = r * np.cos(new_angle)
            y = r * np.sin(new_angle)
            electron.center = (x, y)  
          return [electron for electron, _, _ in electrons]  
        ani = animation.FuncAnimation(fig, update, frames=range(200), interval=50, blit=True)    
        ax.set_title(f'Bohr Model of {self.name if self.name else "Element"} (Z={self.Z})')
        plt.savefig(f"{self.name}_Bohr.png" if self.name else "Element_Bohr.png", dpi=300)
        plt.show()
#~~~~~~~Display Periodic Table~~~~~~~#
    @staticmethod 
    def display_periodic_table():
        print("Periodic Table of Elements (First 50 Elements):")
        print(periodic_df.to_string(index=False))
    plt.show()
#~~~~~~~Get User Input~~~~~~~#
    @staticmethod
    def get_user_input():
        print("Welcome to the Atomic Structure Visualizer!")
        print("You can enter an atomic number (Z) or an element symbol (e.g., H for Hydrogen).")
        choice = input("Enter atomic number (Z) or element symbol (or 'all' to list): ").strip().lower()
        if choice == 'all':
            Element.display_periodic_table()
            return None
        try:
            if choice.isdigit():
                Z = int(choice)
                if Z < 1 or Z > 50:
                    print("Please enter a valid atomic number between 1 and 50.")
                    return None
                element_data = periodic_df[periodic_df['Z'] == Z]
            else:
                element_data = periodic_df[periodic_df['Symbol'].str.upper() == choice.upper()]
            if element_data.empty:
                element_data = periodic_df[periodic_df['Name'].str.lower() == choice.lower()]

            if element_data.empty:
                print("Element not found. Please check your input.")
                return None

            row = element_data.iloc[0]
            Z = row['Z']
            name = row['Name']
            symbol = row['Symbol']

            print(f"Element found: {name} (Symbol: {symbol}, Z={Z})")
            A = input(f"Enter mass number (A) for {name} (or press Enter to skip): ").strip()
            A = int(A) if A.isdigit() else None
            return Element(Z, A, name)
        except Exception as e:
            print(f"Error: {e}")
            return None
#~~~~~~~Main Function~~~~~~~#
if __name__ == "__main__":
    element = Element.get_user_input()
    if element:
        print(f"Electron configuration (shells): {element.get_shells_str()}")
        element.draw_bohr_model_animated()
