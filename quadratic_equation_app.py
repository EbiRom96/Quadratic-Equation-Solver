import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

class QuadraticEquationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quadratic Equation Program - EbiRom")
        self.root.geometry("800x700")
        self.root.configure(bg='#FFE4B5')  # Light yellow/orange color
        
        # Program header
        header_frame = tk.Frame(root, bg='#FF8C00', height=100)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="Comprehensive Quadratic Equation Program", 
                              font=('Arial', 18, 'bold'), bg='#FF8C00', fg='white')
        title_label.pack(expand=True)
        
        info_label = tk.Label(header_frame, 
                             text="Created by: EbiRom | Creation Time: 2012 | Email: Raptor@nixom.ir", 
                             font=('Arial', 10), bg='#FF8C00', fg='white')
        info_label.pack(expand=True)
        
        # Create notebook for different sections
        notebook = ttk.Notebook(root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # First tab: Solve quadratic equation
        self.solve_frame = tk.Frame(notebook, bg='#FFE4B5')
        notebook.add(self.solve_frame, text="Solve Quadratic Equation")
        self.create_solve_tab()
        
        # Second tab: Create equation from solutions
        self.create_frame = tk.Frame(notebook, bg='#FFE4B5')
        notebook.add(self.create_frame, text="Create Equation from Solutions")
        self.create_equation_tab()
        
        # Third tab: Plot graph
        self.graph_frame = tk.Frame(notebook, bg='#FFE4B5')
        notebook.add(self.graph_frame, text="Plot Graph")
        self.create_graph_tab()
    
    def create_solve_tab(self):
        # Coefficient inputs
        input_frame = tk.Frame(self.solve_frame, bg='#FFE4B5')
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Please enter the coefficients of the quadratic equation:", 
                font=('Arial', 12), bg='#FFE4B5').grid(row=0, column=0, columnspan=3, pady=10)
        
        tk.Label(input_frame, text="a (coefficient of x²):", font=('Arial', 10), bg='#FFE4B5').grid(row=1, column=0, padx=5, pady=5)
        self.a_entry = tk.Entry(input_frame, width=10)
        self.a_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="b (coefficient of x):", font=('Arial', 10), bg='#FFE4B5').grid(row=2, column=0, padx=5, pady=5)
        self.b_entry = tk.Entry(input_frame, width=10)
        self.b_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="c (constant term):", font=('Arial', 10), bg='#FFE4B5').grid(row=3, column=0, padx=5, pady=5)
        self.c_entry = tk.Entry(input_frame, width=10)
        self.c_entry.grid(row=3, column=1, padx=5, pady=5)
        
        solve_button = tk.Button(input_frame, text="Solve Equation", command=self.solve_equation,
                                bg='#FF8C00', fg='white', font=('Arial', 10, 'bold'))
        solve_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Results area
        self.solution_text = tk.Text(self.solve_frame, height=15, width=70, font=('Arial', 10))
        self.solution_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(self.solution_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.solution_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.solution_text.yview)
    
    def solve_equation(self):
        try:
            # Get coefficients
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
            
            # Clear previous results
            self.solution_text.delete(1.0, tk.END)
            
            # Display equation
            equation = f"Equation: {a}x² + {b}x + {c} = 0\n"
            self.solution_text.insert(tk.END, equation)
            self.solution_text.insert(tk.END, "="*50 + "\n")
            
            # Solution steps
            self.solution_text.insert(tk.END, "SOLUTION STEPS:\n\n")
            
            # Step 1: Calculate discriminant
            discriminant = b**2 - 4*a*c
            self.solution_text.insert(tk.END, f"Step 1: Calculate discriminant (D)\n")
            self.solution_text.insert(tk.END, f"D = b² - 4ac = ({b})² - 4×({a})×({c})\n")
            self.solution_text.insert(tk.END, f"D = {b**2} - {4*a*c} = {discriminant}\n\n")
            
            # Check discriminant value
            if discriminant > 0:
                self.solution_text.insert(tk.END, "Since D > 0, the equation has two distinct real roots.\n\n")
                
                # Step 2: Calculate roots
                root1 = (-b + math.sqrt(discriminant)) / (2*a)
                root2 = (-b - math.sqrt(discriminant)) / (2*a)
                
                self.solution_text.insert(tk.END, f"Step 2: Calculate roots using quadratic formula\n")
                self.solution_text.insert(tk.END, f"x = [-b ± √D] / (2a)\n")
                self.solution_text.insert(tk.END, f"x = [-({b}) ± √{discriminant}] / (2×{a})\n")
                self.solution_text.insert(tk.END, f"x = [{b} ± {math.sqrt(discriminant):.4f}] / {2*a}\n\n")
                
                self.solution_text.insert(tk.END, f"First root (x₁):\n")
                self.solution_text.insert(tk.END, f"x₁ = [{b} + {math.sqrt(discriminant):.4f}] / {2*a} = {root1:.4f}\n\n")
                
                self.solution_text.insert(tk.END, f"Second root (x₂):\n")
                self.solution_text.insert(tk.END, f"x₂ = [{b} - {math.sqrt(discriminant):.4f}] / {2*a} = {root2:.4f}\n\n")
                
                self.solution_text.insert(tk.END, "FINAL RESULTS:\n")
                self.solution_text.insert(tk.END, f"x₁ = {root1:.4f}\n")
                self.solution_text.insert(tk.END, f"x₂ = {root2:.4f}\n")
                
            elif discriminant == 0:
                self.solution_text.insert(tk.END, "Since D = 0, the equation has one real root (repeated).\n\n")
                
                # Step 2: Calculate root
                root = -b / (2*a)
                
                self.solution_text.insert(tk.END, f"Step 2: Calculate root\n")
                self.solution_text.insert(tk.END, f"x = -b / (2a)\n")
                self.solution_text.insert(tk.END, f"x = -({b}) / (2×{a})\n")
                self.solution_text.insert(tk.END, f"x = {root:.4f}\n\n")
                
                self.solution_text.insert(tk.END, "FINAL RESULT:\n")
                self.solution_text.insert(tk.END, f"x = {root:.4f} (double root)\n")
                
            else:
                self.solution_text.insert(tk.END, "Since D < 0, the equation has two complex roots.\n\n")
                
                # Step 2: Calculate complex roots
                real_part = -b / (2*a)
                imaginary_part = math.sqrt(-discriminant) / (2*a)
                
                self.solution_text.insert(tk.END, f"Step 2: Calculate complex roots\n")
                self.solution_text.insert(tk.END, f"x = [-b ± i√|D|] / (2a)\n")
                self.solution_text.insert(tk.END, f"x = [-({b}) ± i√{abs(discriminant)}] / (2×{a})\n")
                self.solution_text.insert(tk.END, f"x = [{b} ± i{math.sqrt(abs(discriminant)):.4f}] / {2*a}\n\n")
                
                self.solution_text.insert(tk.END, "FINAL RESULTS:\n")
                self.solution_text.insert(tk.END, f"x₁ = {real_part:.4f} + {imaginary_part:.4f}i\n")
                self.solution_text.insert(tk.END, f"x₂ = {real_part:.4f} - {imaginary_part:.4f}i\n")
                
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all coefficients.")
        except ZeroDivisionError:
            messagebox.showerror("Input Error", "Coefficient 'a' cannot be zero for a quadratic equation.")
    
    def create_equation_tab(self):
        # Inputs for roots
        input_frame = tk.Frame(self.create_frame, bg='#FFE4B5')
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Please enter the roots of the quadratic equation:", 
                font=('Arial', 12), bg='#FFE4B5').grid(row=0, column=0, columnspan=3, pady=10)
        
        tk.Label(input_frame, text="Root 1 (x₁):", font=('Arial', 10), bg='#FFE4B5').grid(row=1, column=0, padx=5, pady=5)
        self.root1_entry = tk.Entry(input_frame, width=10)
        self.root1_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Root 2 (x₂):", font=('Arial', 10), bg='#FFE4B5').grid(row=2, column=0, padx=5, pady=5)
        self.root2_entry = tk.Entry(input_frame, width=10)
        self.root2_entry.grid(row=2, column=1, padx=5, pady=5)
        
        create_button = tk.Button(input_frame, text="Create Equation", command=self.create_equation,
                                 bg='#FF8C00', fg='white', font=('Arial', 10, 'bold'))
        create_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Results area
        self.creation_text = tk.Text(self.create_frame, height=15, width=70, font=('Arial', 10))
        self.creation_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(self.creation_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.creation_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.creation_text.yview)
    
    def create_equation(self):
        try:
            # Get roots
            root1 = float(self.root1_entry.get())
            root2 = float(self.root2_entry.get())
            
            # Clear previous results
            self.creation_text.delete(1.0, tk.END)
            
            # Display roots
            self.creation_text.insert(tk.END, f"Given roots: x₁ = {root1}, x₂ = {root2}\n")
            self.creation_text.insert(tk.END, "="*50 + "\n")
            
            # Solution steps
            self.creation_text.insert(tk.END, "CREATION STEPS:\n\n")
            
            # Step 1: Use Vieta's formulas
            self.creation_text.insert(tk.END, "Step 1: Use Vieta's formulas\n")
            self.creation_text.insert(tk.END, "For a quadratic equation: ax² + bx + c = 0\n")
            self.creation_text.insert(tk.END, "Sum of roots: x₁ + x₂ = -b/a\n")
            self.creation_text.insert(tk.END, "Product of roots: x₁ × x₂ = c/a\n\n")
            
            # Step 2: Calculate sum and product
            sum_roots = root1 + root2
            product_roots = root1 * root2
            
            self.creation_text.insert(tk.END, f"Step 2: Calculate sum and product of roots\n")
            self.creation_text.insert(tk.END, f"Sum: {root1} + {root2} = {sum_roots}\n")
            self.creation_text.insert(tk.END, f"Product: {root1} × {root2} = {product_roots}\n\n")
            
            # Step 3: Form the equation
            self.creation_text.insert(tk.END, "Step 3: Form the quadratic equation\n")
            self.creation_text.insert(tk.END, "Using the standard form: x² - (sum of roots)x + (product of roots) = 0\n")
            self.creation_text.insert(tk.END, f"x² - ({sum_roots})x + ({product_roots}) = 0\n\n")
            
            # Final equation
            self.creation_text.insert(tk.END, "FINAL EQUATION:\n")
            self.creation_text.insert(tk.END, f"x² - {sum_roots}x + {product_roots} = 0\n")
            
            # Alternative forms
            self.creation_text.insert(tk.END, "\nALTERNATIVE FORMS:\n")
            self.creation_text.insert(tk.END, f"x² - {sum_roots}x + {product_roots} = 0\n")
            
            # Factored form
            self.creation_text.insert(tk.END, f"Factored form: (x - {root1})(x - {root2}) = 0\n")
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for both roots.")
    
    def create_graph_tab(self):
        # Inputs for coefficients
        input_frame = tk.Frame(self.graph_frame, bg='#FFE4B5')
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Please enter coefficients to plot the graph:", 
                font=('Arial', 12), bg='#FFE4B5').grid(row=0, column=0, columnspan=3, pady=10)
        
        tk.Label(input_frame, text="a (coefficient of x²):", font=('Arial', 10), bg='#FFE4B5').grid(row=1, column=0, padx=5, pady=5)
        self.graph_a_entry = tk.Entry(input_frame, width=10)
        self.graph_a_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="b (coefficient of x):", font=('Arial', 10), bg='#FFE4B5').grid(row=2, column=0, padx=5, pady=5)
        self.graph_b_entry = tk.Entry(input_frame, width=10)
        self.graph_b_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="c (constant term):", font=('Arial', 10), bg='#FFE4B5').grid(row=3, column=0, padx=5, pady=5)
        self.graph_c_entry = tk.Entry(input_frame, width=10)
        self.graph_c_entry.grid(row=3, column=1, padx=5, pady=5)
        
        plot_button = tk.Button(input_frame, text="Plot Graph", command=self.plot_graph,
                               bg='#FF8C00', fg='white', font=('Arial', 10, 'bold'))
        plot_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Graph area
        self.graph_frame_inner = tk.Frame(self.graph_frame, bg='#FFE4B5')
        self.graph_frame_inner.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
    
    def plot_graph(self):
        try:
            # Get coefficients
            a = float(self.graph_a_entry.get())
            b = float(self.graph_b_entry.get())
            c = float(self.graph_c_entry.get())
            
            # Clear previous graph
            for widget in self.graph_frame_inner.winfo_children():
                widget.destroy()
            
            # Create figure
            fig, ax = plt.subplots(figsize=(8, 6))
            
            # Generate x values
            x = np.linspace(-10, 10, 400)
            y = a*x**2 + b*x + c
            
            # Plot the quadratic function
            ax.plot(x, y, 'b-', linewidth=2, label=f'y = {a}x² + {b}x + {c}')
            
            # Calculate roots for marking
            discriminant = b**2 - 4*a*c
            if discriminant >= 0:
                root1 = (-b + math.sqrt(discriminant)) / (2*a)
                root2 = (-b - math.sqrt(discriminant)) / (2*a)
                
                if discriminant > 0:
                    ax.plot([root1, root2], [0, 0], 'ro', markersize=8, label='Roots')
                else:
                    ax.plot([root1], [0], 'ro', markersize=8, label='Root (double)')
            
            # Calculate vertex
            vertex_x = -b / (2*a)
            vertex_y = a*vertex_x**2 + b*vertex_x + c
            ax.plot([vertex_x], [vertex_y], 'go', markersize=8, label='Vertex')
            
            # Customize plot
            ax.axhline(y=0, color='k', linewidth=0.5)
            ax.axvline(x=0, color='k', linewidth=0.5)
            ax.grid(True, alpha=0.3)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title(f'Graph of y = {a}x² + {b}x + {c}')
            ax.legend()
            
            # Embed plot in tkinter window
            canvas = FigureCanvasTkAgg(fig, self.graph_frame_inner)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all coefficients.")
        except ZeroDivisionError:
            messagebox.showerror("Input Error", "Coefficient 'a' cannot be zero for a quadratic equation.")

def main():
    root = tk.Tk()
    app = QuadraticEquationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()