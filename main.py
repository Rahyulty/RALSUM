import tkinter as tk


def get_estimate(function, direction):
    if type(direction) == str and type(function) == str:
        # change it to lowercase 
        # so we dont have to check
        # for cap cases

        direction = direction.lower()
        function = function.lower()
        
        # now we do the logic
        if direction == "left" and function == "increasing":
             return "underestimate"
        elif direction == "left" and function == "decreasing":
            return "overestimate"
        elif direction == "left" and function == "concave up":
            return "overestimate"
        elif direction == "left" and function == "concave down":
            return "underestimate"
        elif direction == "right" and function == "increasing":
            return "overestimate"
        elif direction == "right" and function == "decreasing":
            return "underestimate"
        elif direction == "right" and function == "concave up":
            return "underestimate"
        elif direction == "right" and function == "concave down":
            return "overestimate"
        elif direction == "midpoint" and function == "increasing":
            return "exact"
        elif direction == "midpoint" and function == "decreasing":
            return "exact"
        elif direction == "midpoint" and function == "concave up":
            return "exact"
        elif direction == "midpoint" and function == "concave down":
            return "exact"
        else:
            return "Invalid input"   
    else:
        return "bad type"


root = tk.Tk()
root.title("Riemann Sums")
print(get_estimate("increasing", "left"))

def estimate():
    function = function_entry.get()
    direction = direction_entry.get()
    result_label.config(text=get_estimate(function, direction))

root = tk.Tk()
root.title("Riemann Sums")
root.geometry("400x400")

function_label = tk.Label(root, text="Function:")
function_label.grid(row=0, column=0)

function_entry = tk.Entry(root)
function_entry.grid(row=0, column=1)

direction_label = tk.Label(root, text="Direction:")
direction_label.grid(row=1, column=0)

direction_entry = tk.Entry(root)
direction_entry.grid(row=1, column=1)

estimate_button = tk.Button(root, text="Estimate", command=estimate)
estimate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()