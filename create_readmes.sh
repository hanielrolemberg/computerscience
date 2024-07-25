#!/bin/bash

# Lista de matérias em inglês
subjects=(
    "Computer_Architecture"
    "Fundamentals_of_Computer_Networks"
    "Introduction_to_Computer_Programming"
    "Introduction_to_Information_Security"
    "Database"
    "Cloud_Computing"
    "Web_Development_in_HTML5_CSS_JavaScript"
    "Programming_Languages_Paradigms"
    "Computational_Thinking"
    "Rapid_Application_Development"
    "Data_Structures"
    "Mathematics_and_Logic"
    "Computer_Network_Protocols"
    "Information_Systems_and_Society"
    "Operating_Systems"
    "Data_Analysis"
    "Differential_and_Integral_Calculus"
    "Data_Science_in_Python"
    "Systems_Modeling_in_UML"
    "Basic_Software_Programming"
    "Algorithms_and_Complexity"
    "Multivariable_Calculus"
    "Software_Engineering"
    "Analytical_Geometry_and_Linear_Algebra"
    "Distributed_Systems_and_Parallel_Computing"
    "Graph_Algorithms"
    "Formal_Languages_and_Automata"
    "Quantitative_Methods"
    "Microcontroller_Programming"
    "Object_Oriented_Programming"
    "Cloud_IoT_and_Industry_4.0_Applications"
    "Artificial_Intelligence"
    "Mathematical_Modeling"
    "Software_Design_Patterns"
    "Mobile_Devices_Programming"
    "Image_Processing_Algorithms"
    "Compilers"
    "Cybersecurity"
    "Big_Data_Topics_in_Python"
)

# Criar README.md para cada matéria
for subject in "${subjects[@]}"; do
    mkdir -p "$subject"
    cat <<EOL > "$subject/README.md"
# ${subject//_/ }

This directory contains projects and exercises related to the course **${subject//_/ }**. The purpose of these projects is to apply the concepts learned in this course to real-world scenarios, reinforcing knowledge and skills.

## Projects

- [Project 1](./project1)
- [Project 2](./project2)
- [Project 3](./project3)

## Objectives

- **Practice**: Reinforce the concepts and skills acquired during the course.
- **Retention**: Ensure long-term retention of knowledge by applying it to practical projects.
- **Community Support**: Provide valuable resources and projects that others can learn from and contribute to.

## Contribution

Contributions are welcome! If you have any ideas, suggestions, or improvements for any of the projects, feel free to create a pull request or open an issue.

## License

This repository is open source and available under the [MIT License](../LICENSE).

Thank you for visiting, and I hope these projects are helpful for your learning and development!
EOL
done

echo "README.md files created successfully."
