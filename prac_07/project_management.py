import datetime

DATE_FORMAT = "%d/%m/%Y"
DEFAULT_FILE = "projects.txt"

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        if isinstance(start_date, str):
            self.start_date = datetime.datetime.strptime(start_date, DATE_FORMAT).date()
        else:
            self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def is_complete(self):
        return self.completion_percentage == 100

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime(DATE_FORMAT)}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def to_file_line(self):
        return (f"{self.name}\t{self.start_date.strftime(DATE_FORMAT)}\t"
                f"{self.priority}\t{self.cost_estimate:.2f}\t"
                f"{self.completion_percentage}")

def load_projects(filename):
    projects = []
    with open(filename, 'r', encoding="utf-8") as file:
        next(file)
        for line in file:
            if line.strip():
                name, date_str, priority, estimate, completion = line.strip().split('\t')
                projects.append(Project(name, date_str, priority, estimate, completion))
    return projects

def save_projects(filename, projects):
    with open(filename, 'w', encoding="utf-8") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for p in projects:
            file.write(p.to_file_line() + "\n")

def display_projects(projects):
    incomplete = sorted([p for p in projects if not p.is_complete()])
    completed = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects: ")
    for p in incomplete:
        print("  " + str(p))
    print("Completed projects: ")
    for p in completed:
        print("  " + str(p))

def filter_by_date(projects):
    date_input = input("Show projects that start after date (dd/mm/yy): ")
    try:
        if len(date_input.split('/')[-1]) == 2:
            filter_date = datetime.datetime.strptime(date_input, "%d/%m/%y").date()
        else:
            filter_date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
    except Exception:
        print("Invalid date format.")
        return
    filtered = [p for p in projects if p.start_date >= filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for p in filtered:
        print(p)

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    date_input = input("Start date (dd/mm/yy): ")
    try:
        if len(date_input.split('/')[-1]) == 2:
            start_date = datetime.datetime.strptime(date_input, "%d/%m/%y").date()
        else:
            start_date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
    except Exception:
        print("Invalid date format. Project not added.")
        return
    while True:
        try:
            priority = int(input("Priority: "))
            break
        except ValueError:
            print("Invalid priority, enter a number.")
    estimate_str = input("Cost estimate: $")
    try:
        cost_estimate = float(estimate_str)
    except ValueError:
        cost_estimate = 0.0
    while True:
        try:
            percent = int(input("Percent complete: "))
            break
        except ValueError:
            print("Invalid percentage, enter a number.")
    projects.append(Project(name, start_date, priority, cost_estimate, percent))

def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
    except (ValueError, IndexError):
        print("Invalid input.")
        return
    print(project)
    percent_str = input("New Percentage: ")
    if percent_str:
        try:
            project.completion_percentage = int(percent_str)
        except ValueError:
            print("Invalid input, percentage unchanged.")
    priority_str = input("New Priority: ")
    if priority_str:
        try:
            project.priority = int(priority_str)
        except ValueError:
            print("Invalid input, priority unchanged.")

def menu():
    print("Welcome to Pythonic Project Management")
    try:
        projects = load_projects(DEFAULT_FILE)
        print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
    except FileNotFoundError:
        print(f"Could not find {DEFAULT_FILE}, starting with empty project list.")
        projects = []

    while True:
        print("- (L)oad projects  ")
        print("- (S)ave projects  ")
        print("- (D)isplay projects  ")
        print("- (F)ilter projects by date")
        print("- (A)dd new project  ")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").strip().lower()
        if choice == "l":
            filename = input("Filename to load projects from: ")
            try:
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
            except FileNotFoundError:
                print(f"Could not find {filename}. Projects not loaded.")
        elif choice == "s":
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            answer = input(f"Would you like to save to {DEFAULT_FILE}? ").strip().lower()
            if answer in ("y", "yes"):
                save_projects(DEFAULT_FILE, projects)
                print(f"Saved to {DEFAULT_FILE}.")
            else:
                print("No changes saved.")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid menu choice.")

if __name__ == "__main__":
    menu()